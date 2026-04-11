const BASE_URL = process.env.BASE_URL || 'https://dfifa-egor.hf.space'; 
const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '.env.local') }); 

const API_KEY = process.env.EGOR_API_KEY;
const HF_TOKEN = process.env.HF_TOKEN;

if (!API_KEY || !HF_TOKEN) {
    console.error("❌ Missing EGOR_API_KEY or HF_TOKEN in tests/.env.local");
    process.exit(1);
}

// 🦿 NEW function to test AI features
async function testSummarize() {
    const endpoint = `${BASE_URL}/api/summarize`;
    console.log(`Testing /api/summarize endpoint (${endpoint})...`);
    
    // Some sample text to summarize
    const sampleText = "Artificial Intelligence (AI) is intelligence demonstrated by machines, as opposed to intelligence of humans and other animals. Example tasks in which this is done include speech recognition, computer vision, translation between (natural) languages, as well as other mappings of inputs.";

    try {
        const response = await fetch(endpoint, {
            method: 'POST', // We use POST because we are sending data
            headers: {
                'x-api-key': API_KEY, // Verify our EGOR API key
                'Authorization': `Bearer ${HF_TOKEN}`, // Verification for huggingface
                'Content-Type': 'application/json' // Tell the server we are sending JSON text
            },
            body: JSON.stringify({
                text: sampleText
            })
        });
        
        if (response.ok) {
            const data = await response.json();
            console.log(`Success! Status: ${response.status}`);
            console.log(`\n-- AI OUTPUT --\n`);
            console.log(JSON.stringify(data, null, 2));
            console.log(`\n---------------\n`);
            return true;
        } else {
            console.log(`HTTP Error ${response.status}: ${response.statusText}`);
            try {
                const errorData = await response.json();
                console.log('Error Detail:', errorData.detail);
            } catch (e) {
                // Ignore if not JSON
            }
            return false;
        }
    } catch (error) {
        console.log(`❌ Failed to reach /api/summarize: ${error.message}\n`);
        return false;
    }
}

async function testSummarizeRateLimit() {
    const endpoint = `${BASE_URL}/api/summarize`;
    console.log(`\nTesting /api/summarize Rate Limit (Time Limit)...`);
    
    const sampleText = "Short text to test rate limit.";

    try {
        console.log("Sending immediate second request to trigger time limit...");
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'x-api-key': API_KEY,
                'Authorization': `Bearer ${HF_TOKEN}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                text: sampleText
            })
        });
        
        if (response.status === 429) {
            console.log(`Success! Caught expected Rate Limit. Status: ${response.status}`);
            return true;
        } else if (response.ok) {
            console.log(`❌ Expected Rate Limit Error (429) but got Success (${response.status}). Rate limit not enforcing properly!`);
            return false;
        } else {
            // Some limits return 400 or 403. Check detail
            try {
                const errorData = await response.json();
                console.log(`HTTP Error ${response.status}: ${errorData.detail || response.statusText}`);
                if (errorData.detail && typeof errorData.detail === 'string' && errorData.detail.toLowerCase().includes("limit")) {
                    console.log(`Success! Caught expected Rate Limit message.`);
                    return true;
                }
            } catch (e) {
                console.log(`Got HTTP Error ${response.status}: ${response.statusText}`);
            }
            return false;
        }
    } catch (error) {
        console.log(`❌ Failed to reach /api/summarize: ${error.message}\n`);
        return false;
    }
}

async function runTests() {
    console.log('-'.repeat(40));
    console.log(' EGOR SERVER AI FEATURES TEST (JS) ');
    console.log('-'.repeat(40));
    
    console.log(`Target API:   ${BASE_URL}\n`);

    const summarizeOk = await testSummarize();
    const rateLimitOk = await testSummarizeRateLimit();
    
    console.log('-'.repeat(40));
    if (summarizeOk && rateLimitOk) {
        console.log('RESULT: AI ENDPOINT AND RATE LIMIT FULLY OPERATIONAL ✅');
    } else if (summarizeOk) {
        console.log('RESULT: AI ENDPOINT IS UP, BUT RATE LIMIT IS FAILING ⚠️');
    } else {
        console.log('RESULT: AI ENDPOINT IS FAILING ❌');
    }
    console.log('-'.repeat(40));
}

runTests();
