let timer;
function mouseFollower(a,b) {
    let cursor = document.querySelector(".circle")


    document.addEventListener("mousemove", function (e) {

        x = e.clientX 
        y = e.clientY

        cursor.style.transform = `translate(${x}px,${y}px) scale(${a},${b})`
        setTimeout(function(){
            document.querySelector(".circle").style.opacity=1;
        },400)



    })
}
xprev = 0;
yprev = 0;
function circleflatten() {
    window.addEventListener("mousemove", function (manoj) {
        clearTimeout(timer)
        x = manoj.clientX-12;
        y = manoj.clientY-12;
        xdiff = -(xprev - x);
        ydiff = -(yprev - y);
        xprev = x;
        yprev = y;
        xclamp = gsap.utils.clamp(.8,1.2,xdiff)
        yclamp = gsap.utils.clamp(.8,1.2,ydiff)
        mouseFollower(xclamp,yclamp)
        timer = setTimeout(function(){
            document.querySelector(".circle").style.transform = `translate(${x}px,${y}px) scale(1,1)`
        },100)

    })
}
circleflatten()




function updateTime() {
  const now = new Date();
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');
  const timeString = `${hours}:${minutes}:${seconds}`;
  document.getElementById('live-time').innerText = timeString;
}

// Update time every second
setInterval(updateTime, 1000);

// Initial call to display time immediately
updateTime();