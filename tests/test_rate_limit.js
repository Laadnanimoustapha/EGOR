// 100% ai

const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '.env.local') });

//const API_URL = "http://127.0.0.1:8000/generate?length=12";    if tested localy 
const API_URL = "https://dfifa-egor.hf.space/generate?length=12";
const API_KEY = process.env.EGOR_API_KEY;
const HF_TOKEN = process.env.HF_TOKEN;

if (!API_KEY || !HF_TOKEN) {
    console.error("❌ Missing EGOR_API_KEY or HF_TOKEN in tests/.env.local");
    process.exit(1);
}
const NUM_REQUESTS = 7; // The limit is 5 requests per 60 seconds, so 7 will trigger the limit

async function testRateLimit() {
    console.log(`Starting to send ${NUM_REQUESTS} requests to test the rate limit...\n`);

    for (let i = 1; i <= NUM_REQUESTS; i++) {
        try {
            const response = await fetch(API_URL, {
                method: "GET",
                headers: {
                    "x-api-key": API_KEY,
                    "Authorization": `Bearer ${HF_TOKEN}`
                }
            });

            // Try to parse the JSON response
            const data = await response.json().catch(() => ({}));

            if (response.status === 200) {
                const password = data.data && data.data.password ? data.data.password : JSON.stringify(data);
                console.log(`Request ${i}: ✅ Success (Status ${response.status}) -> Password: ${password}`);
            } else if (response.status === 429) {
                console.log(`Request ${i}: ⏳ Rate Limited (Status ${response.status}) ->`, data);
            } else {
                console.log(`Request ${i}: ❌ Error (Status ${response.status}) ->`, data);
            }
        } catch (error) {
            console.error(`Request ${i}: ⚠️ Network Request Failed - ${error.message}`);
        }
        
        // Wait 200ms before sending the next one
        await new Promise(resolve => setTimeout(resolve, 200));
    }
    
    console.log('\nFinished testing rate limit.');
}

testRateLimit();
