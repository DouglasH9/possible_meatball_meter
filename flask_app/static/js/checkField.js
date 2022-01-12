let blastBox = document.getElementById("is_blasted")
let affordBox = document.getElementById("is_affordable")
let checkField1 = document.getElementById("check_field1")
let checkField2 = document.getElementById("check_field2")

blastBox.addEventListener("change", function() {
    if (this.checked) {
        checkField1.id = "checked_field"
    }
})

affordBox.addEventListener("change", function() {
    if (this.checked) {
        checkField2.id = "checked_field"
    }
})