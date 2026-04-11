require('dotenv').config({ path: __dirname + '/.env.local' });
const { URL } = require('url');
// 100% AI 
/**
 * Database Connection Tester
 * 
 * NOTE: Before running this script, ensure you have the required drivers installed:
 * 1. Initialize npm (if not already done): `npm init -y`
 * 2. Install postgres driver (if using Postgres): `npm install pg`
 * 3. Install mysql driver (if using MySQL): `npm install mysql2`
 * 
 * Run with: DATABASE_URL="your_url_here" node tests/check_db.js
 */

async function testDatabaseConnection() {
    const dbUrl = process.env.EGOR_DATA_BASE || process.env.DATABASE_URL;
    
    if (!dbUrl) {
        console.error("❌ Error: EGOR_DATA_BASE environment variable is not set.");
        console.error("💡 Hint: Run the script using: DATABASE_URL='your_database_url' node check_db.js");
        process.exit(1);
    }
    
    try {
        const parsedUrl = new URL(dbUrl);
        // Postgres sometimes uses postgresql:// instead of postgres://
        let protocol = parsedUrl.protocol.replace(':', '');
        if (protocol === 'postgresql') protocol = 'postgres';
        
        console.log(`⌛ Testing connection to ${protocol} database...`);
        console.log(`📍 Host: ${parsedUrl.hostname}`);
        
        if (protocol === 'postgres') {
            const { Client } = require('pg');
            const client = new Client({
                connectionString: dbUrl,
                ssl: { rejectUnauthorized: false } // Necessary for Aiven and most cloud services
            });
            
            await client.connect();
            console.log("✅ Successfully reached the server. Sending test query...");
            const res = await client.query('SELECT 1 as connected');
            await client.end();
            
            if (res.rows[0].connected === 1) {
                console.log("🎉 Database is up and running correctly!");
            }
            
        } else if (protocol === 'mysql') {
            const mysql = require('mysql2/promise');
            const connection = await mysql.createConnection({
                uri: dbUrl,
                ssl: { rejectUnauthorized: false } // Necessary for Aiven
            });
            
            console.log("✅ Successfully reached the server. Sending test query...");
            const [rows] = await connection.query('SELECT 1 as connected');
            await connection.end();
            
            if (rows[0].connected === 1) {
                console.log("🎉 Database is up and running correctly!");
            }
            
        } else {
            console.error(`❌ Unsupported database protocol: ${protocol}. The script currently supports 'postgres' and 'mysql'.`);
            process.exit(1);
        }
        
    } catch (error) {
        console.error("\n❌ Failed to connect to the database.");
        console.error("Error details:", error.message);
        
        // Let the user know if they forgot to install the NPM package //
        if (error.code === 'MODULE_NOT_FOUND') {
            console.error(`\n💡 Hint: It seems you are missing a package. Run the following command:`);
            if (dbUrl.includes('postgres')) {
                console.error(`npm install pg`);
            } else if (dbUrl.includes('mysql')) {
                console.error(`npm install mysql2`);
            }
        }
        process.exit(1);
    }
}

testDatabaseConnection();
