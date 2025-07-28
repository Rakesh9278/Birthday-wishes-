# Birthday-wishes-<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🎉 Happy Birthday Rakesh 🎂</title>
  <style>
    body {
      background-color: #fff0f5;
      text-align: center;
      font-family: 'Comic Sans MS', cursive;
      color: #d63384;
      padding-top: 50px;
    }
    h1 {
      font-size: 3em;
      animation: bounce 1.5s infinite;
    }
    @keyframes bounce {
      0% { transform: translateY(0px); }
      50% { transform: translateY(-20px); }
      100% { transform: translateY(0px); }
    }
    .balloons {
      font-size: 2em;
      margin: 20px 0;
    }
    button {
      background-color: #ff69b4;
      color: white;
      padding: 15px 25px;
      font-size: 18px;
      border: none;
      border-radius: 12px;
      cursor: pointer;
      margin-top: 30px;
      box-shadow: 2px 2px 8px #888;
    }
    button:hover {
      background-color: #ff1493;
    }
  </style>
</head>
<body>
  <div class="balloons">🎈🎈🎉🎉🎁🎈</div>
  <h1>🎂 Happy Birthday, Rakesh! 🎂</h1>
  <p>🎊 জন্মদিন: 22 নভেম্বর, 2010 🎊</p>
  <p>Wishing you joy, love, and a life full of happiness! 💖</p>
  <img src="https://i.ibb.co/xj5zF0X/birthday-cake.png" width="200" alt="Birthday Cake">

  <!-- 🎵 Audio -->
  <audio controls autoplay loop>
    <source src="https://www2.cs.uic.edu/~i101/SoundFiles/BirthdaySong.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
  </audio>

  <!-- 🎁 Surprise Button -->
  <br><br>
  <button onclick="showWish()">🎁 Tap Here for a Wish 🎁</button>

  <script>
    function showWish() {
      alert("🎉 শুভ জন্মদিন রাকেশ! \n\nতোমার জীবন হোক আনন্দ, ভালোবাসা, ও সাফল্যে ভরপুর! 🎂💖🎈");
    }
  </script>

  <div class="balloons">🎈🎊🎂🎉🎈</div>
</body>
</html>
