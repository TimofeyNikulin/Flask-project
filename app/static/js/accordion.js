let acc = document.getElementsByClassName("accordion_item");

for (let i = 0; i < acc.length; i++) {
    acc[i].onclick = function() {
        this.classList.toggle("active")
    }
}