let blastBox = document.getElementById("is_blasted")
let affordBox = document.getElementById("is_affordable")
let checkField1 = document.getElementById("check_field1")
let checkField2 = document.getElementById("check_field2")

console.log(blastBox)

blastBox.addEventListener("change", function() {
    if (this.checked == true) {
        checkField1.id = "checked_field"
    } else {
        checkField1.id = "check_field1"
    }
})

affordBox.addEventListener("change", function() {
    if (this.checked == true) {
        checkField2.id = "checked_field"
    } else {
        checkField2.id = "check_field2"
    }
})