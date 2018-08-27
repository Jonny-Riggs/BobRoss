


console.log("I am here!!")

document.getElementById("js-clicker").addEventListener("click", () => {
    console.log("OOOOH, that tickles")
    fetch('http://127.0.0.1:8000/birthday')
        .then(r => r.json())
        .then(birthday => {
            let list = ""
            birthday.forEach(b => {
                list += `<li>${b.name} ${b.greeting} ${b.date}</li>`
            })
            $("#list").append(list)
        })
})

// TODO: Make an http request to ""

// url: "/birthdays"