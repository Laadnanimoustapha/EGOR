from fastapi.responses import HTMLResponse
import os

# THE MAINE HTML CONVERTED TO VIA PYTHON

def HTML_PAGE():
  hf_token = os.getenv("HF_TOKEN")

  HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>EGOR API Tester</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    /* ---- Page Switcher ---- */
    .page-switcher {
      position: fixed;
      top: 16px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      background: #1A1A1A;
      border: 1.5px solid #C9A227;
      border-radius: 30px;
      overflow: hidden;
      z-index: 100;
    }

    .switch-btn {
      padding: 8px 22px;
      background: transparent;
      border: none;
      color: #C9A227;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      cursor: pointer;
      letter-spacing: 1px;
      transition: all 0.25s ease;
      position: relative;
    }

    .switch-btn:hover { background: #C9A22712; }

    .switch-btn.active {
      background: #C9A227;
      color: #0D0D0D;
      font-weight: 600;
    }

    .switch-btn + .switch-btn {
      border-left: 1px solid #C9A22750;
    }

    /* ---- Page Views ---- */
    .page-view {
      display: none;
      animation: fadeIn 0.35s ease;
    }

    .page-view.active { display: flex; }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    /* ---- Landing Page ---- */
    .landing-view {
      width: 100%;
      min-height: 100vh;
      justify-content: center;
      align-items: center;
      flex-direction: column;
    }

    .landing-view pre {
      color: rgb(243, 240, 80);
      font-family: monospace;
      font-size: 18px;
      text-align: center;
      animation: glow 2s ease-in-out infinite alternate;
    }

    @keyframes glow {
      from { text-shadow: 0 0 5px #fff; }
      to   { text-shadow: 0 0 20px #ffd700, 0 0 30px #ffd700; }
    }

    body {
      background: #0D0D0D;
      color: #F5F5F5;
      font-family: 'Inter', sans-serif;
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      padding: 60px 20px;
    }

    .container {
      width: 100%;
      max-width: 520px;
    }

    /* ---- Title ---- */
    h1 {
      color: #C9A227;
      font-size: 1.8rem;
      font-weight: 600;
      text-align: center;
      margin-bottom: 8px;
      letter-spacing: 2px;
    }

    .subtitle {
      text-align: center;
      color: #777;
      font-size: 0.8rem;
      margin-bottom: 40px;
      letter-spacing: 1px;
    }

    /* ---- Labels ---- */
    label {
      display: block;
      font-size: 0.75rem;
      color: #888;
      margin-bottom: 6px;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    /* ---- API Key Input ---- */
    .api-key-input {
      width: 100%;
      background: transparent;
      border: none;
      border-bottom: 2px solid #C9A227;
      color: #F5F5F5;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.9rem;
      padding: 10px 0;
      outline: none;
      margin-bottom: 32px;
      transition: border-color 0.2s;
    }

    .api-key-input::placeholder { color: #444; }
    .api-key-input:focus { border-color: #e6be3a; }

    /* ---- Endpoint Buttons ---- */
    .endpoints {
      display: flex;
      gap: 8px;
      margin-bottom: 24px;
    }

    .endpoint-btn {
      flex: 1;
      padding: 10px 6px;
      border: 1.5px solid #C9A227;
      border-radius: 6px;
      background: transparent;
      color: #C9A227;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      cursor: pointer;
      transition: all 0.2s;
      text-align: center;
    }

    .endpoint-btn:hover { background: #C9A22715; }

    .endpoint-btn.active {
      background: #C9A227;
      color: #0D0D0D;
      font-weight: 600;
    }

    /* ---- Method badge ---- */
    .method {
      font-size: 0.6rem;
      display: block;
      margin-bottom: 2px;
      opacity: 0.7;
    }

    /* ---- Dynamic fields ---- */
    .field-group {
      margin-bottom: 24px;
      display: none;
    }

    .field-group.visible { display: block; }

    .length-input {
      width: 100%;
      background: transparent;
      border: none;
      border-bottom: 2px solid #333;
      color: #F5F5F5;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.9rem;
      padding: 10px 0;
      outline: none;
      transition: border-color 0.2s;
    }

    .length-input:focus { border-color: #C9A227; }

    .text-area {
      width: 100%;
      background: #1A1A1A;
      border: 1.5px solid #333;
      border-radius: 6px;
      color: #F5F5F5;
      font-family: 'Inter', sans-serif;
      font-size: 0.85rem;
      padding: 14px;
      outline: none;
      resize: vertical;
      min-height: 100px;
      transition: border-color 0.2s;
    }

    .text-area::placeholder { color: #444; }
    .text-area:focus { border-color: #C9A227; }

    /* ---- Send Button ---- */
    .send-btn {
      width: 100%;
      padding: 14px;
      background: #C9A227;
      color: #0D0D0D;
      border: none;
      border-radius: 6px;
      font-family: 'Inter', sans-serif;
      font-size: 0.95rem;
      font-weight: 600;
      cursor: pointer;
      letter-spacing: 1px;
      transition: opacity 0.2s;
      margin-bottom: 28px;
    }

    .send-btn:hover { opacity: 0.85; }

    .send-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    /* ---- Response Box ---- */
    .response-label {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }

    .status-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      padding: 2px 8px;
      border-radius: 4px;
      display: none;
    }

    .status-badge.success {
      display: inline-block;
      background: #1a3a1a;
      color: #4ade80;
    }

    .status-badge.error {
      display: inline-block;
      background: #3a1a1a;
      color: #f87171;
    }

    .response-box {
      width: 100%;
      background: #1A1A1A;
      border-radius: 8px;
      padding: 20px;
      min-height: 120px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      line-height: 1.6;
      color: #666;
      white-space: pre-wrap;
      word-break: break-word;
      border-left: 3px solid #333;
      transition: border-color 0.3s;
    }

    .response-box.success { border-left-color: #C9A227; }
    .response-box.error { border-left-color: #8B0000; }

    /* ---- Loading ---- */
    .loading { color: #C9A227; }

    /* ---- Footer ---- */
    .footer {
      text-align: center;
      margin-top: 40px;
      padding-top: 20px;
      border-top: 1px solid #1A1A1A;
      color: #444;
      font-size: 0.7rem;
      letter-spacing: 1px;
    }

    /* ---- Server URL ---- */
    .server-url-input {
      width: 100%;
      background: transparent;
      border: none;
      border-bottom: 1px solid #222;
      color: #666;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      padding: 8px 0;
      outline: none;
      margin-bottom: 28px;
      transition: border-color 0.2s;
    }

    .server-url-input:focus { border-color: #C9A227; color: #F5F5F5; }
    .server-url-input::placeholder { color: #333; }
  </style>
</head>
<body>

  <!-- Page Switcher -->
  <div class="page-switcher">
    <button class="switch-btn active" id="switchLanding" onclick="switchPage('landing')">EGOR</button>
    <button class="switch-btn" id="switchTester" onclick="switchPage('tester')">API TESTER</button>
  </div>

  <!-- Landing Page -->
  <div class="page-view landing-view active" id="landingView">
    <pre>
 ███████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔════╝░██╔══██╗██╔══██╗
█████╗░░██║░░██╗░██║░░██║██████╔╝
██╔══╝░░██║░░╚██╗██║░░██║██╔══██╗
███████╗╚██████╔╝╚█████╔╝██║░░██║
╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝
    </pre>
  </div>

  <!-- API Tester Page -->
  <div class="page-view" id="testerView" style="justify-content: center; align-items: flex-start; width: 100%;">
  <div class="container">

    <h1>EGOR</h1>
    <p class="subtitle">API Tester — v1.3.0</p>

    <!-- Server URL -->
    <label>Server URL</label>
    <input
      type="text"
      id="serverUrl"
      class="server-url-input"
      placeholder="https://dfifa-egor.hf.space"
      value="https://dfifa-egor.hf.space"
    >

    <!-- HF Token -->
    <label>HF Token (For Private Spaces)</label>
    <!-- keep the api key exposed couse the website is prvet and it is in the testing fase  -->
    <input
      type="text"
      id="hfToken"
      class="api-key-input"
      style="margin-bottom: 20px;"
      placeholder="hf_TOKEN_HERE"  
      value="%%HF_TOKEN%%"
    >

    <!-- API Key -->
    <label>API Key</label>
    <!-- keep the api key exposed couse the website is prvet and it is in the testing fase  -->
    <input
      type="text"
      id="apiKey"
      class="api-key-input"
      placeholder="FUCK-ISREAL-49136817-LAERSI-KCUF"
      value="FUCK-ISREAL-49136817-LAERSI-KCUF"
    >

    <!-- Endpoint Selection -->
    <label>Endpoint</label>
    <div class="endpoints">
      <button class="endpoint-btn active" data-endpoint="health" onclick="selectEndpoint(this)">
        <span class="method">GET</span>
        /health
      </button>
      <button class="endpoint-btn" data-endpoint="generate" onclick="selectEndpoint(this)">
        <span class="method">GET</span>
        /generate
      </button>
      <button class="endpoint-btn" data-endpoint="summarize" onclick="selectEndpoint(this)">
        <span class="method">POST</span>
        /api/summarize
      </button>
    </div>

    <!-- Length field (generate only) -->
    <div class="field-group" id="lengthField">
      <label>Password Length (8 – 100)</label>
      <input
        type="number"
        id="lengthInput"
        class="length-input"
        min="8"
        max="100"
        value="12"
        placeholder="12"
      >
    </div>

    <!-- Text field (summarize only) -->
    <div class="field-group" id="textField">
      <label>Text to Summarize</label>
      <textarea
        id="textInput"
        class="text-area"
        placeholder="Enter the text you want to summarize..."
      >Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals including humans. AI research has been defined as the field of study of intelligent agents, which refers to any system that perceives its environment and takes actions that maximize its chance of achieving its goals. The term "artificial intelligence" had previously been used to describe machines that mimic and display "human" cognitive skills that are associated with the human mind, such as "learning" and "problem-solving".</textarea>
    </div>

    <!-- Send -->
    <button class="send-btn" id="sendBtn" onclick="sendRequest()">SEND</button>

    <!-- Response -->
    <div class="response-label">
      <label>Response</label>
      <span class="status-badge" id="statusBadge"></span>
    </div>
    <div class="response-box" id="responseBox">Waiting for request...</div>

    <!-- Footer -->
    <div class="footer">EGOR Server — Built by LAADNANI</div>

  </div>
  </div>

  <script>
    let currentEndpoint = 'health';

    function switchPage(page) {
      document.getElementById('landingView').classList.toggle('active', page === 'landing');
      document.getElementById('testerView').classList.toggle('active', page === 'tester');
      document.getElementById('switchLanding').classList.toggle('active', page === 'landing');
      document.getElementById('switchTester').classList.toggle('active', page === 'tester');
    }

    function selectEndpoint(btn) {
      document.querySelectorAll('.endpoint-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentEndpoint = btn.dataset.endpoint;

      // Show/hide dynamic fields
      document.getElementById('lengthField').classList.toggle('visible', currentEndpoint === 'generate');
      document.getElementById('textField').classList.toggle('visible', currentEndpoint === 'summarize');
    }

    async function sendRequest() {
      const serverUrl = document.getElementById('serverUrl').value.replace(/\/+$/, '');
      const apiKey = document.getElementById('apiKey').value.trim();
      const hfToken = document.getElementById('hfToken').value.trim();
      const responseBox = document.getElementById('responseBox');
      const statusBadge = document.getElementById('statusBadge');
      const sendBtn = document.getElementById('sendBtn');

      // Reset
      responseBox.className = 'response-box';
      statusBadge.className = 'status-badge';
      statusBadge.style.display = 'none';
      responseBox.textContent = 'Sending...';
      responseBox.classList.add('loading');
      sendBtn.disabled = true;

      let url = '';
      let options = { headers: {} };

      if (hfToken) {
          options.headers['Authorization'] = `Bearer ${hfToken}`;
      }

      try {
        switch (currentEndpoint) {
          case 'health':
            url = serverUrl + '/health';
            options.method = 'GET';
            break;

          case 'generate':
            const length = document.getElementById('lengthInput').value || 12;
            url = serverUrl + '/generate?length=' + length;
            options.method = 'GET';
            options.headers['x-api-key'] = apiKey;
            break;

          case 'summarize':
            const text = document.getElementById('textInput').value;
            if (!text) {
              throw new Error('Please enter some text to summarize.');
            }
            url = serverUrl + '/api/summarize';
            options.method = 'POST';
            options.headers['Content-Type'] = 'application/json';
            options.headers['x-api-key'] = apiKey;
            options.body = JSON.stringify({ text: text });
            break;
        }

        const res = await fetch(url, options);

        // Read as text first, then try to parse as JSON
        const rawText = await res.text();
        let data;
        let isJson = false;

        try {
          data = JSON.parse(rawText);
          isJson = true;
        } catch {
          data = rawText;
        }

        responseBox.classList.remove('loading');

        if (res.ok) {
          responseBox.className = 'response-box success';
          statusBadge.className = 'status-badge success';
          statusBadge.textContent = res.status + ' OK';
        } else {
          responseBox.className = 'response-box error';
          statusBadge.className = 'status-badge error';
          statusBadge.textContent = res.status + ' ERROR';
        }

        statusBadge.style.display = 'inline-block';
        responseBox.textContent = isJson ? JSON.stringify(data, null, 2) : data;

      } catch (err) {
        responseBox.classList.remove('loading');
        responseBox.className = 'response-box error';
        statusBadge.className = 'status-badge error';
        statusBadge.textContent = 'FAILED';
        statusBadge.style.display = 'inline-block';

        if (err.message === 'Failed to fetch') {
          responseBox.textContent = 'Could not reach the server.\n\nPossible causes:\n• Server is down\n• CORS is blocking the request\n• Wrong server URL';
        } else {
          responseBox.textContent = err.message;
        }
      }

      sendBtn.disabled = false;
    }
  </script>

</body>
</html>

"""
  HTML = HTML.replace("%%HF_TOKEN%%",hf_token)
  return HTMLResponse(HTML)