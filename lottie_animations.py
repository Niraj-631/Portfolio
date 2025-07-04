
# --- Load Lottie Animations ---

import requests
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animations = {
"ai" : load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_ydo1amjm.json"),
"dev" : load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_t24tpvcu.json"),
"about" : load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_jtbfg2nb.json"),
"hero" : load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_zrqthn6o.json"),
"network" : load_lottie_url("https://assets6.lottiefiles.com/packages/lf20_3vbOcw.json"), 
"education" : load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_qp1q7mct.json"), 
"certification": load_lottie_url("https://assets6.lottiefiles.com/private_files/lf30_m6j5igxb.json"),
"skills":load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_tno6cg2w.json"), 
"contact" : load_lottie_url("https://lottie.host/6d2e9a88-4e76-435f-ae48-9e32d26091c7/fkF6UKKPl7.json"),
}