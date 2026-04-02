const BASE_URL = 'https://dfifa-egor.hf.space'; 
const API_KEY = process.env.API_KEY || 'FUCK-ISREAL-76034217-LAERSI-KCUF';

// Note: We use the direct Space URL for API calls. 
// https://huggingface.co/spaces/dfifa/EGOR is the UI wrapper page.
// The actual API container runs at https://dfifa-egor.hf.space.

async function testRoot() {
    console.log(`Testing root endpoint (${BASE_URL}/)...`);
    try {
        const response = await fetch(`${BASE_URL}/`);
        if (response.ok) {
            const data = await response.json();
            console.log(`Success! Status: ${response.status}`); // IF IT SUCCED
            console.log('Response:', data, '\n');
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
                'User-Agent': 'Node.js Test Client' 
            }
        });
        
        if (response.ok) {
            const data = await response.json();
            console.log(`Success! Status: ${response.status}`); // IF THE PASSWORD GET GENERATED
            console.log(`Generated Password: ${data.password}\n`);
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

async function runTests() {
    console.log('-'.repeat(30));
    console.log(' EGOR SERVER HEALTH CHECK (JS) ');
    console.log('-'.repeat(30));
    
    console.log(`Target Space: https://huggingface.co/spaces/dfifa/EGOR`);
    console.log(`Target API:   ${BASE_URL}\n`);

    const rootOk = await testRoot();
    const genOk = await testGenerate();
    
    console.log('-'.repeat(30));
    if (rootOk && genOk) {
        console.log('RESULT: SERVER IS FULLY OPERATIONAL ');
    } else if (rootOk) {
        console.log('RESULT: SERVER IS UP BUT /GENERATE IS FAILING ');
    } else {
        console.log('RESULT: SERVER IS DOWN OR UNREACHABLE ');
    }
    console.log('-'.repeat(30));
}

runTests();
