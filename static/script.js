let DirectoryToIgnoreImages

const format_date = () => {
    let date_txt = new Date();
    months = ["Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    let month = months[date_txt.getMonth()];
    let year = date_txt.getFullYear();
    date_txt = `${month} ${year}`;
    // returns the first element who's ID starts with date
    date = document.querySelectorAll(`[id^="date"]`)[0]
    date.innerHTML = date_txt;
    console.log("Formatted date to " + date_txt)
}

const validate = (object) => {
    let flags = [
        (object.parentNode.localName === "header"), // Checks if object is in the header
        (object.getAttribute("alt") === "omit") // Checks if object alt is "omit"
    ]

    return flags.some(element => element === true)
};

const format_img = () => {
    let images = document.querySelectorAll('img');
    let figure_number = 1;
    for (let image of images) {
        if (validate(image)) continue;
        let alt = image.getAttribute('alt');
        let description = `<p class="alt"> Fig. ${figure_number}. ${alt} </p>`;
        image.insertAdjacentHTML("afterend", description);
        figure_number++;
    }
    console.log("Formatted img description");
}

const format_table = () => {
    let tables = document.querySelectorAll('table');
    let figure_number = 1;
    for (let table of tables) {
        if (validate(table)) continue;
        let description = `<p class="alt"> Tabla ${figure_number}. </p>`;
        table.insertAdjacentHTML("afterend", description);
        figure_number++;
    }
    console.log("Formated table description");
}

const main = () => {
    format_date()
    format_img()
    format_table()
}

document.onload = main()