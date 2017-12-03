import {URL} from '../config.js'
import Vue from 'vue'

export default class DataService{

    static getAll(url){
        return Vue.http.get(`${URL}${url}/`);
    }

    static getById(url, id){
        return Vue.http.get(`${URL}${url}/${id}/`)
    }

    static  post(url, data){
        return Vue.http.post(`${URL}${url}/`,data);
    }
    static delete(url, data){
        return Vue.http.delete(`${URL}${url}/`+data+"/");
    }
    static put(url,data,id){
        return Vue.http.put(`${URL}${url}/${id}/`,data);
    }

}