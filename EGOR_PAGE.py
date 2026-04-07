from fastapi.responses import HTMLResponse

# THE MAINE HTML CONVERTED TO VIA PYTHON

HTML_PAGE = HTMLResponse("""
<html>
    <head>
    <style>

     body{
      margin:0;
      height:100vh;
      display:flex;
      justify-content: center;
      align-items:center;
      background:black;
      color:rgb(243, 240, 80);
      font-family:monospace;
      }

      pre{
       font-size:18px;
       text-align:center;
       animation: glow 2s ease-in-out infinite alternate;
       }

       @keyframes glow{
        from{
            text-shadow: 0 0 5px #fff;
        }
        to{
            text-shadow: 0 0 20px #ffd700, 0 0 30px #ffd700;
        }
       }

    </style>
    </head>
    <body>
    <pre>
     ███████╗░██████╗░░█████╗░██████╗░
    ██╔════╝██╔════╝░██╔══██╗██╔══██╗
    █████╗░░██║░░██╗░██║░░██║██████╔╝
    ██╔══╝░░██║░░╚██╗██║░░██║██╔══██╗
    ███████╗╚██████╔╝╚█████╔╝██║░░██║
    ╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝
    </pre>
    </html>
""")


# V2  STORME AND LIGHTENING EFFECTS BUILDED BY CLOUDE

# HTML_PAGE_V2 = HTMLResponse("""
# <html>
#     <head>
#     <style>

#      *{ margin:0; padding:0; box-sizing:border-box; }

#      body{
#       margin:0;
#       height:100vh;
#       display:flex;
#       justify-content: center;
#       align-items:center;
#       background:#050510;
#       color:rgb(243, 240, 80);
#       font-family:monospace;
#       overflow:hidden;
#       position:relative;
#       }

#       /* Lightning canvas fills the entire screen behind everything */
#       #lightning-canvas{
#         position:fixed;
#         top:0; left:0;
#         width:100%; height:100%;
#         z-index:0;
#         pointer-events:none;
#       }

#       /* Screen flash overlay for when lightning strikes */
#       #flash-overlay{
#         position:fixed;
#         top:0; left:0;
#         width:100%; height:100%;
#         background:rgba(180,180,255,0);
#         z-index:1;
#         pointer-events:none;
#         transition: background 0.05s ease-out;
#       }

#       /* The banner sits on top of everything */
#       pre{
#        position:relative;
#        z-index:2;
#        font-size:18px;
#        text-align:center;
#        animation: glow 2s ease-in-out infinite alternate;
#        }

#        @keyframes glow{
#         from{
#             text-shadow: 0 0 5px #fff, 0 0 10px rgba(255,215,0,0.3);
#         }
#         to{
#             text-shadow: 0 0 20px #ffd700, 0 0 30px #ffd700, 0 0 50px rgba(255,215,0,0.2);
#         }
#        }

#        /* Ambient storm clouds effect */
#        body::before{
#         content:'';
#         position:fixed;
#         top:-50%; left:-50%;
#         width:200%; height:200%;
#         background:
#           radial-gradient(ellipse at 20% 20%, rgba(40,40,80,0.4) 0%, transparent 50%),
#           radial-gradient(ellipse at 80% 30%, rgba(30,30,70,0.3) 0%, transparent 50%),
#           radial-gradient(ellipse at 50% 10%, rgba(50,50,90,0.5) 0%, transparent 40%);
#         animation: clouds 15s ease-in-out infinite alternate;
#         z-index:0;
#         pointer-events:none;
#        }

#        @keyframes clouds{
#         from{ transform: translate(0,0) scale(1); opacity:0.6; }
#         to{ transform: translate(-2%,1%) scale(1.05); opacity:0.9; }
#        }

#     </style>
#     </head>
#     <body>
#     <canvas id="lightning-canvas"></canvas>
#     <div id="flash-overlay"></div>
#     <pre>
#      ███████╗░██████╗░░█████╗░██████╗░
#     ██╔════╝██╔════╝░██╔══██╗██╔══██╗
#     █████╗░░██║░░██╗░██║░░██║██████╔╝
#     ██╔══╝░░██║░░╚██╗██║░░██║██╔══██╗
#     ███████╗╚██████╔╝╚█████╔╝██║░░██║
#     ╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝
#     </pre>

#     <script>
#     // === LIGHTNING EFFECT ENGINE ===
#     const canvas = document.getElementById('lightning-canvas');
#     const ctx = canvas.getContext('2d');
#     const flash = document.getElementById('flash-overlay');

#     function resize(){
#       canvas.width = window.innerWidth;
#       canvas.height = window.innerHeight;
#     }
#     resize();
#     window.addEventListener('resize', resize);

#     // Generate a single lightning bolt segment with branches
#     function createBolt(startX, startY, endX, endY, maxBranches){
#       const segments = [];
#       const points = [{x: startX, y: startY}];
#       const steps = 12 + Math.floor(Math.random()*10);
#       let cx = startX, cy = startY;

#       for(let i=1; i<=steps; i++){
#         const t = i / steps;
#         cx = startX + (endX - startX) * t + (Math.random()-0.5) * 120;
#         cy = startY + (endY - startY) * t;
#         points.push({x: cx, y: cy});
#       }
#       points.push({x: endX, y: endY});
#       segments.push(points);

#       // Create branches
#       const branchCount = Math.floor(Math.random() * maxBranches);
#       for(let b = 0; b < branchCount; b++){
#         const branchIdx = Math.floor(Math.random() * (points.length - 2)) + 1;
#         const bp = points[branchIdx];
#         const branchLen = 40 + Math.random() * 120;
#         const angle = (Math.random() - 0.5) * Math.PI * 0.8;
#         const branchPoints = [{x: bp.x, y: bp.y}];
#         let bx = bp.x, by = bp.y;
#         const bSteps = 4 + Math.floor(Math.random()*4);
#         for(let s=1; s<=bSteps; s++){
#           bx += Math.sin(angle) * (branchLen/bSteps) + (Math.random()-0.5)*30;
#           by += Math.cos(angle) * (branchLen/bSteps) * 0.5 + branchLen/bSteps;
#           branchPoints.push({x: bx, y: by});
#         }
#         segments.push(branchPoints);
#       }

#       return segments;
#     }

#     // Draw a bolt with glow
#     function drawBolt(segments, alpha, color){
#       segments.forEach((points, idx) => {
#         const isMain = idx === 0;
#         const width = isMain ? 2.5 : 1.2;

#         // Outer glow
#         ctx.beginPath();
#         ctx.moveTo(points[0].x, points[0].y);
#         for(let i=1; i<points.length; i++){
#           ctx.lineTo(points[i].x, points[i].y);
#         }
#         ctx.strokeStyle = `rgba(${color},${alpha * 0.3})`;
#         ctx.lineWidth = width * 8;
#         ctx.shadowColor = `rgba(${color},${alpha * 0.5})`;
#         ctx.shadowBlur = 40;
#         ctx.stroke();

#         // Inner glow
#         ctx.beginPath();
#         ctx.moveTo(points[0].x, points[0].y);
#         for(let i=1; i<points.length; i++){
#           ctx.lineTo(points[i].x, points[i].y);
#         }
#         ctx.strokeStyle = `rgba(${color},${alpha * 0.6})`;
#         ctx.lineWidth = width * 3;
#         ctx.shadowBlur = 20;
#         ctx.stroke();

#         // Core bolt
#         ctx.beginPath();
#         ctx.moveTo(points[0].x, points[0].y);
#         for(let i=1; i<points.length; i++){
#           ctx.lineTo(points[i].x, points[i].y);
#         }
#         ctx.strokeStyle = `rgba(255,255,255,${alpha})`;
#         ctx.lineWidth = width;
#         ctx.shadowColor = `rgba(${color},${alpha})`;
#         ctx.shadowBlur = 10;
#         ctx.stroke();
#       });
#     }

#     // Active lightning bolts
#     let bolts = [];

#     function spawnBolt(){
#       const startX = Math.random() * canvas.width;
#       const endX = startX + (Math.random()-0.5) * 300;
#       const segments = createBolt(startX, 0, endX, canvas.height * (0.5 + Math.random()*0.5), 4);
#       // Randomly pick blue-ish or purple-ish tint
#       const colors = ['150,150,255','180,160,255','120,180,255','200,180,255'];
#       const color = colors[Math.floor(Math.random()*colors.length)];
#       bolts.push({
#         segments,
#         color,
#         life: 1.0,          // starts fully visible
#         decay: 0.02 + Math.random()*0.03,
#         flickerCount: 2 + Math.floor(Math.random()*3),
#         flickerTimer: 0,
#         visible: true
#       });

#       // Screen flash
#       flash.style.background = 'rgba(180,180,255,0.12)';
#       setTimeout(()=>{ flash.style.background = 'rgba(180,180,255,0)'; }, 80);
#     }

#     // Main animation loop
#     function animate(){
#       ctx.clearRect(0, 0, canvas.width, canvas.height);
#       ctx.shadowBlur = 0;

#       bolts.forEach(bolt => {
#         // Flicker effect
#         bolt.flickerTimer++;
#         if(bolt.flickerTimer > 3){
#           bolt.flickerTimer = 0;
#           if(bolt.flickerCount > 0){
#             bolt.visible = !bolt.visible;
#             if(!bolt.visible) bolt.flickerCount--;
#           } else {
#             bolt.visible = true;
#           }
#         }

#         if(bolt.visible){
#           drawBolt(bolt.segments, bolt.life, bolt.color);
#         }
#         bolt.life -= bolt.decay;
#       });

#       // Remove dead bolts
#       bolts = bolts.filter(b => b.life > 0);

#       requestAnimationFrame(animate);
#     }
#     animate();

#     // Spawn lightning at random intervals (1-4 seconds)
#     function scheduleNext(){
#       const delay = 800 + Math.random() * 3000;
#       setTimeout(()=>{
#         spawnBolt();
#         // Sometimes double-strike
#         if(Math.random() < 0.3){
#           setTimeout(spawnBolt, 100 + Math.random()*200);
#         }
#         scheduleNext();
#       }, delay);
#     }
#     scheduleNext();
#     // First bolt fires quickly so user sees it right away
#     setTimeout(spawnBolt, 500);

#     </script>
#     </body>
#     </html>
# """)

