function toggleOtherField() {
  const select = document.getElementById("category_select");
  const otherDiv = document.getElementById("other_category");
  const otherInput = document.getElementById("other_input");

  if (select.value === "Others") {
    otherDiv.style.display = "block";
    otherInput.required = true;
  } else {
    otherDiv.style.display = "none";
    otherInput.required = false;
  }
}
