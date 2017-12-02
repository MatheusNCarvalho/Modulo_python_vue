<template>
    <div class="panel panel-default">
        <div class="panel-heading">
            <div class="row">
                <div class="col-xs-6">
                    <h4>Cargos</h4>
                </div>
                <!--<div class="col-xs-6">-->
                <!--<button @click.prevent="novoCargo()" class="btn btn-default pull-right">Novo</button>-->
                <!--</div>-->
            </div>
        </div>
        <div class="panel-body">
            <div class="row">
                <div class="col-md-6">


                    <!--<div class="form-group form-inline">-->
                    <!--<input type="input"  class="form-control" id="keyword" name="keyword" placeholder="Buscar por nome" v-model="keyword">-->
                    <!--<button @click.prevent="trySearch" class="btn btn-default">Buscar</button>-->
                    <!--</div>-->


                    <table class="table table-bordered table-hover">
                        <thead>
                        <tr>
                            <th>Id</th>
                            <th width="50%">Nome</th>
                            <th width="100%">Descrição</th>
                            <th width="20%">Ação</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="category in listaCategorias">
                            <td>{{category.id}}</td>
                            <td>{{category.nome}}</td>
                            <td>{{category.descricao}}</td>

                            <td role="button" @click.prevent="tryEdit(category)"><span
                                    class="glyphicon glyphicon-pencil" aria-hidden="true"></span></td>
                        </tr>
                        </tbody>
                    </table>

                    <!--<div class="text-center">-->
                    <!--<Pagination :total="getTotalCategories" :itens-per-page="getItensPerPage" :page="getCategoryPage" @change-page="onChangePage"></Pagination>-->
                    <!--</div>-->

                </div>
                <div class="col-md-6">
                    <!--<Error></Error>-->
                    <validator name="validateForm">
                        <form>
                            <div class="form-group">
                                <label for="name">Id</label>
                                <input type="input" class="form-control" id="id" placeholder="id"
                                       v-model="form.id" readonly>
                            </div>

                            <div class="form-group">
                                <label for="name">Nome</label>
                                <input type="input" class="form-control" id="name" placeholder="Nome"
                                       v-model="form.nome">

                            </div>

                            <div class="form-group">
                                <label for="descricao">Descrição</label>
                                <input type="input" class="form-control" id="descricao" placeholder="Descricao"
                                       v-model="form.descricao">

                            </div>
                            <button @click.prevent="Salvar" class="btn btn-default" :disabled="condicao">Salvar
                            </button>
                            <Loading></Loading>
                            <button @click.prevent="tryDeleteCategory" class="btn btn-default pull-right"
                                    :disabled="form.id==null">Apagar
                            </button>
                            <button @click.prevent="Limpar" class="btn btn-default">Limpar </button>

                        </form>
                    </validator>
                </div>
            </div>
        </div>
    </div>
    </div>
</template>
<script>

    import Loading from '../controls/Loading.vue'
    import Error from '../controls/Error.vue'
    import Pagination from '../controls/Pagination.vue'
    import DadaService from '../services/Category'

    export default {

        components: {
            Loading, Error, Pagination
        },

        created() {
            this.carregarCargos();

        },
        data() {
            return {
                listaCategorias: {},
                keyword: "",
                form: {
                    id: null,
                    nome: '',
                    descricao: ''
                },
                condicao: false

            }
        },
        methods: {
            novoCargo() {

            },
            newCategory() {
                this.setCategory({})
            },
            Limpar() {

                this.form = {}
            },
            Salvar() {
                const onFinally = () => {
                    this.Limpar()
                }

                this.condicao = true

                if (this.form.id == null) {
                    DadaService.post(this.form)
                        .then(response => {
                                this.condicao = false
                                this.carregarCargos()


                            },
                            error => {
                                console.log("Error: ", error)
                            }).finally(onFinally())
                } else {

                }

            },
            carregarCargos() {
                DadaService.getAll()
                    .then(response => {
                            this.listaCategorias = JSON.parse(response.data)
                            /// console.log(JSON.parse( response.data))
                            this.carregarCargos()
                        },
                        error => {

                        }).finally(function () {

                })


            },
            tryEdit(category) {
                console.log("Editar", category);
                this.form = category;
            },
            tryDeleteCategory() {
                const onFinally = () => {
                    this.Limpar()
                }
                if (confirm(`Deseja apagar " ${this.form.nome} " ?`)) {
                    DadaService.delete(this.form.id)
                        .then(response => {
                                this.carregarCargos()
                            },
                            error => {

                            }).finally(onFinally)
                }
            }
        }


    }</script>
