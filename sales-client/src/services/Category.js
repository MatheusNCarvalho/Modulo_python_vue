import {URL} from '../config.js'
import Vue from 'vue'

export default class CategoryService{

    static getAll(){
        return Vue.http.get(`${URL}cargos/`);
    }

    static  post(data){
        return Vue.http.post(`${URL}cargos/`,data);
    }
    static delete(data){
        return Vue.http.delete(`${URL}cargos/`+data+"/");
    }

}