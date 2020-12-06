const change_colour = async () => {
    let light = document.getElementById('light');
    let hue = document.getElementById('hue');

    let response = await fetch('/api/hue/${light.value}/${hue.value}/', {
        method: "POST"
    }).then(res => res.json()).then(res => {
        if (!res.error) return alert('Done!');
        else {
            console.log(res.output);
            return alert("Error - Please check console");
        }
    }).catch((err) => {
        if (err) {
            console.log(err)
            return alert("Error - Please check console")
        }
    })

}