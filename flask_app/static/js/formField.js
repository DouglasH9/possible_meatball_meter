let blastBox = document.getElementById("is_blasted")
let affordBox = document.getElementById("is_affordable")
let checkField1 = document.getElementById("check_field1")
let checkField2 = document.getElementById("check_field2")
let thumbSlide = document.getElementById("rating")

console.log(blastBox)

blastBox.addEventListener("change", function() {
    if (this.checked == true) {
        checkField1.id = "checked_field"
        checkField1.classList.add("checked")
    } else {
        checkField1.id = "check_field1"
        checkField1.classList.remove("checked")
    }
})

affordBox.addEventListener("change", function() {
    if (this.checked == true) {
        checkField2.id = "checked_field"
        checkField2.classList.add("checked")
    } else {
        checkField2.id = "check_field2"
        checkField2.classList.remove("checked")
    }
})

thumbSlide.addEventListener("input", () => {
    const value = Number(thumbSlide.value)/10
    thumbSlide.style.setProperty("--thumb-rotate", `${value * 720}deg`);
})