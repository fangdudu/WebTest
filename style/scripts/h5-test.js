var x = document.getElementById("loc");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "该游览器不支持获取地理位置";
    }
}

function showPosition(position) {
    x.innerHTML = "纬度：" + position.coords.latitude + "<br> 经度：" + position.coords.longitude;
}