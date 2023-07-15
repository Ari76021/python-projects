import qrcode

myqr=qrcode.make("https://www.linkedin.com/in/arindam-das-71a382243/")
myqr1=qrcode.make("https://www.youtube.com/")
myqr1.save("myqr1.png",scale=7)
myqr.save("myqr.png",scale=8)