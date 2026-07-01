const searchForm=document.querySelectorAll(".search-form");

//buttons
const searchBtn=document.querySelector("#search-btn");

searchBtn.addEventListener("click",function(){
    searchForm.ClassList.toggle("active");
    document.addEventListener("click",function(){
        if(!e.composedPath().includes(searchBtn)){
            searchForm.ClassList.remove("active");
        }
    })
})

