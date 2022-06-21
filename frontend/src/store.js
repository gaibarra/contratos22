import Vuex from 'vuex';
import Vue from 'vue';

Vue.use(Vuex)

import api from  "./componentes/documentos/api"

export default new Vuex.Store({
    state:{
        items: []
    },

    getters:{
        getAllIems: state => {
            return state.items;
        }    
    },
          
    mutations:
})