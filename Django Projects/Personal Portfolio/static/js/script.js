console.log("nothing to see here")

async function demo(elt, range) {
    for (let i = 0; i <= range; i++) {
        await sleep()
        document.getElementById(elt).style.width = `${i}%`
        document.getElementById(`${elt}-span`).innerHTML = `${i}%`
    }
}

function sleep() {
    return new Promise(resolve => setTimeout(resolve, 5));
}

function skills() {
    if (document.getElementById('Bar1').style.width != '85%') {
        demo("Bar1", 85) //Python programming
        demo("Bar2", 73) //Tensorflow 2.0
        demo("Bar3", 68) //Django/Flask
        demo("Bar4", 78) //Javascript
        demo("Bar5", 90) //HTML5/CSS3
    }
}