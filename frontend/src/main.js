import Vue from 'vue'
import App from './App.vue'

import vuetify from './plugins/vuetify';
import Vuetify from 'vuetify/lib/framework'


import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import BoostrapVue from "bootstrap-vue"
import router from "./router"


Vue.use(Vuetify);
Vue.use(BoostrapVue);

Vue.config.productionTip = false

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
