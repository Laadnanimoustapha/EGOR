//const BASE_URL = "http://127.0.0.1:8000"; // LOCAL
const BASE_URL = 'https://dfifa-egor.hf.space'; 
const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '.env.local') }); 
const API_KEY = process.env.EGOR_API_KEY;
const HF_TOKEN = process.env.HF_TOKEN;

if (!API_KEY || !HF_TOKEN) {
    console.error("❌ Missing EGOR_API_KEY or HF_TOKEN in tests/.env.local");
    process.exit(1);
}

// Note: We use the direct Space URL for API calls. 
// https://huggingface.co/spaces/dfifa/EGOR is the UI wrapper page.
// The actual API container runs at https://dfifa-egor.hf.space.
// FULLY MAID WITH AI (GEMINI 3.1 THINKING)

async function testRoot() {
    console.log(`Testing root endpoint (${BASE_URL}/)...`);
    try {
        const response = await fetch(`${BASE_URL}/`, {
            headers: {
                'Authorization': `Bearer ${HF_TOKEN}`
            }
        });
        if (response.ok) {
            const data = await response.text();
            console.log(`Success! Status: ${response.status}`); // IF IT SUCCED
            console.log('Response: (HTML content received)\n');
            return true;
        } else {
            console.log(` HTTP Error: Status: ${response.status} ${response.statusText}\n`); // IF IT FAILED
            return false;
        }
    } catch (error) {
        console.log(`Failed to reach root: ${error.message}\n`);
        return false;
    }
}

async function testGenerate() {
    const endpoint = `${BASE_URL}/generate?length=16`; // Added length param, optional but good for testing
    console.log(`Testing /generate endpoint (${endpoint})...`);
    try {
        const response = await fetch(endpoint, {
            headers: {
                'x-api-key': API_KEY,
                'User-Agent': 'Node.js Test Client',
                'Authorization': `Bearer ${HF_TOKEN}`
            }
        });
        
        if (response.ok) {
            const data = await response.json();
            console.log(`Success! Status: ${response.status} (${data.status})`); // IF THE PASSWORD GET GENERATED
            const password = data.data && data.data.password ? data.data.password : undefined;
            console.log(`Generated Password: ${password}\n`);
            return true;
        } else {
            console.log(`HTTP Error ${response.status}: ${response.statusText}`); // IF NOT
            try {
                const errorData = await response.json();
                console.log('Error Detail:', errorData.detail);
            } catch (e) {
                // Ignore if not JSON
            }
            console.log();
            return false;
        }
    } catch (error) {
        console.log(`❌ Failed to reach /generate: ${error.message}\n`); // if non of the abve errors
        return false;
    }
}

async function testHealth() {
    console.log(`Testing /health endpoint (${BASE_URL}/health)...`);
    try {
        const response = await fetch(`${BASE_URL}/health`, {
            headers: {
                'Authorization': `Bearer ${HF_TOKEN}`
            }
        });
        
        if (response.ok) {
            const data = await response.json();
            console.log(`Success! Status: ${response.status} (${data.status})`); 
            console.log(`Database: ${data.database}\n`);
            return true;
        } else {
            console.log(`HTTP Error ${response.status}: ${response.statusText}\n`);
            return false;
        }
    } catch (error) {
        console.log(`❌ Failed to reach /health: ${error.message}\n`);
        return false;
    }
}

async function runTests() {
    console.log('-'.repeat(30));
    console.log(' EGOR SERVER HEALTH CHECK (JS) ');
    console.log('-'.repeat(30));
    
    console.log(`Target Space: https://huggingface.co/spaces/dfifa/EGOR`);
    console.log(`Target API:   ${BASE_URL}\n`);

    const rootOk = await testRoot();
    const genOk = await testGenerate();
    const healthOk = await testHealth();
    
    console.log('-'.repeat(30));
    if (rootOk && genOk && healthOk) {
        console.log('RESULT: SERVER IS FULLY OPERATIONAL ✅');
    } else if (rootOk && healthOk) {
        console.log('RESULT: SERVER AND HEALTH UP BUT /GENERATE IS FAILING ⚠️');
    } else if (rootOk) {
        console.log('RESULT: SERVER IS UP BUT SOME ENDPOINTS ARE FAILING ⚠️');
    } else {
        console.log('RESULT: SERVER IS DOWN OR UNREACHABLE ❌');
    }
    console.log('-'.repeat(30));
}

runTests();
