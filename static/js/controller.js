async function sendContent(destination, post) {
    return fetch(destination, {
            method: 'POST',
            body: post
        })
        .then(
            async Response => {
                return await Response.json()
            }
        ).catch()
}

async function redirect(destination, landingPage, post) {
    content = await sendContent(destination, post)
    json = await content.json
    verify = (json) ? false : (json => {
        const regex = /(U|u)nable/g;
        let m;

        while ((m = regex.exec(json)) !== null) {
            if (m.index === regex.lastIndex) {
                regex.lastIndex++;
            }

            // The result can be accessed through the `m`-variable.
            m.forEach((match, groupIndex) => {
                console.log(`Found match, group ${groupIndex}: ${match}`);
            });
        }
        return m ? true : false
    })
    console.log('content:' + content + '\n' +
        'response:' + json + '\n' +
        'hash:' + location.hash + '\n' +
        'verify: ' + verify() + '\n' +
        'post:' + post
    )
    location.hash = verify(json) ? landingPage : location.hash
}

async function activity(arg) {
    let el = isInPage(arg.el),
        destination = arg.destination,
        landingPage = arg.landingPage,
        post = arg.formData
    await redirect(destination, landingPage, post)
}

function init(rq) {

    switch (rq) {
        case 'a':
            return document.querySelector('form#a') ? {
                el: document.querySelector('form#a'),
                formData: formDataToObject(document.querySelector('form#a')),
                destination: '',//api link
                landingPage: '#'//page to go if succesfull
            } :false
    
        default:
            return null
    }
}

function isInPage(node) {
    return (node === document.body) ? false : document.body.contains(node);
}

function eventHandler(formObject) {
    let form = init(formObject)
    if (form) {
        activity(form)
    }
}

function formDataToObject(elForm) {
    if (!elForm instanceof Element) return
    let fields = elForm.querySelectorAll('input, select, textarea'),
        o = {}
    for (let i = 0, iMax = fields.length; i < iMax; ++i) {
        let field = fields[i],
            sKey = field.name || field.id
        if (field.type === 'button' || field.type === 'image' || field.type === 'submit' || !sKey) continue
        switch (field.type) {
            case 'checkbox':
                o[sKey] = +field.checked
                break
            case 'radio':
                if (o[sKey] === undefined) o[sKey] = '';
                if (field.checked) o[sKey] = field.value
                break
            case 'select-multiple':
                let a = [];
                for (let j = 0, jMax = field.options.length; j < jMax; ++j) {
                    if (field.options[j].selected) a.push(field.options[j].value)
                }
                o[sKey] = a
                break
            default:
                o[sKey] = field.value
        }
    }
    return JSON.stringify(o)
}