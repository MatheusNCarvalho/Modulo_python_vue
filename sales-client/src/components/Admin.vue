<template>

    <nav class="navbar  navbar-inverse">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"
                    aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
                <a class="navbar-brand" href="#">Sistema com Django e Vue</a>
            </div>
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav navbar-right">
                    <li v-link-active><a v-link="{ path: '/users' }">Usuários</a></li>
                    <li v-link-active><a v-link="{ path: '/suppliers' }">Funcionarios</a></li>
                    <li v-link-active><a v-link="{ path: '/categories' }">Cargos</a></li>
                    <li v-link-active><a v-link="{ path: '/marcas' }">Marcas</a></li>
                    <li v-link-active><a v-link="{ path: '/produtos' }">Produtos</a></li>

                </ul>
            </div>
        </div>
    </nav>
    <div class="container">
        <router-view></router-view>
    </div>

</template>
<script>
import Vue from 'vue'
import {getLogin} from '../vuex/getters'
export default{
      vuex:{
      getters:  {
          getLogin
      }
  },
   ready(){
      Vue.http.headers.common['x-access-token'] = this.getLogin.token;
  }
}
</script>
<style></style>
