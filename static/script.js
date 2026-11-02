const pasteBtn=document.getElementById("pasteBtn");
const urlInput=document.getElementById("url");
pasteBtn.addEventListener("click",async()=>{
  try{
    const text=await navigator.clipboard.readText();
    if(!text){pasteBtn.textContent="Clipboard empty";return;}
    urlInput.value=text.trim();pasteBtn.textContent="Pasted ✓";
    setTimeout(()=>pasteBtn.textContent="Paste",1600);
  }catch{
    urlInput.focus();pasteBtn.textContent="Use Ctrl+V";
    setTimeout(()=>pasteBtn.textContent="Paste",1800);
  }
});
