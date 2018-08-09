(function () {
    let pageBaseUrl = 'views/',
        error = `<div class="card">
                    <h1>Sorry</h1>
                    <p>could not get content</p><br> 
                    <a class="button" href="javascript:location.reload(true)">retry</a>
                </div>`

    async function getContent(view, get) {
        let pageUrl = pageBaseUrl + view + '.html' + get
        return fetch(pageUrl).then(
            async Response => {
                return await Response.text()
            }).catch()
    }

    function setActiveLink(view) {
        document.querySelectorAll('#nav a').forEach(
            (linkElement) => {
                let pageName = linkElement.attributes.href.nodeValue.substr(1)
                if (pageName === view) {
                    linkElement.className = 'active'
                } else {
                    linkElement.className = ''
                }
            }
        )
    }

    function render(view, get) {
        getContent(view, get).then(
            async content => {
                if (content) {
                    return await content
                } else {
                    return error
                }
            }
        ).then(
            async content => {
                document.querySelector('#body').innerHTML = await content
                setActiveLink(view)
            }
        )
    }

    function navigate() {
        let hash = location.hash.substr(1),
            fields = hash.split('!'),
            view = fields[0],
            get = fields[1] ? '?' + fields[1] : ''

        render(view, get)
    }

    onload = () => {
        if (!location.hash) {
            location.hash = '#home'
        }
        onhashchange = navigate
        navigate()
    }
}())