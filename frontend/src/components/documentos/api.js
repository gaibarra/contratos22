const SERVER_URL = 'http://127.0.0.1:8000/v1/'
const DOCS_URL = SERVER_URL + "contratos/"
const TOKEN_URL = SERVER_URL + "token/"
const USUARIO = "gaibarra"
const PASSWORD = "6Vlgpcr/zaira"
const credenciales = {"username":USUARIO,"password":PASSWORD}

const getToken = async () => {
    const r = await fetch(
        TOKEN_URL, {
            method="POST",
            body=JSON.stringify(credenciales),
            mode:"cors",
            headers:{
                'Content-Type':'application/json'
            }        
        }
    )
    const token = await r.json();
    return token;
}

export default {
    getall: async () => {
        const token = await getToken();
        const res = await fetch(DOCS_URL,{
            method = "GET",
            headers: {
                'Content-Type':'application/json',
                'Autorization':"Bearer "+token.access
            }
        }   
        );
        const items = await res.json();
        console.log(items);
        return items.results;
    }
}
