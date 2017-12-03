<template>
    <div class="panel panel-default">
        <div class="panel-heading">
            <div class="row">
                <div class="col-xs-6">
                    <h4>Produtos </h4>
                </div>
                <div class="col-xs-6">
                    <!--<button @click.prevent="newSupplier" class="btn btn-default pull-right">Novo</button>-->
                </div>
            </div>
        </div>
        <div class="panel-body">
            <div class="row">
                <div class="col-md-6">


                    <!--<div class="form-group form-inline">-->
                    <!--<input type="input"  class="form-control" id="keyword" name="keyword" placeholder="Buscar por nome" v-model="keyword">-->
                    <!--<button @click.prevent="search" class="btn btn-default">Buscar</button>-->
                    <!--</div>-->


                    <table class="table table-bordered table-hover">
                        <thead>
                        <tr>
                            <th>Id</th>
                            <th width="50%">Descrição</th>
                            <th width="20%">Ações</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="supplier in produtos">
                            <td>{{supplier.id}}</td>
                            <td>{{supplier.descricao}}</td>
                            <td role="button" @click.prevent="editar(supplier)"><span
                                    class="glyphicon glyphicon-pencil" aria-hidden="true"></span></td>

                        </tr>
                        </tbody>
                    </table>

                    <!--<div class="text-center">-->
                    <!--<Pagination :total="total" :itens-per-page="itensPerPage" :page="page"-->
                    <!--@change-page="onChangePage"></Pagination>-->
                    <!--</div>-->

                </div>
                <div class="col-md-6">
                    <!--<Error></Error>-->
                    <validator name="validateForm">
                        <form>
                            <div class="form-group">
                                <label for="name">Id</label>
                                <input type="input" class="form-control" id="id" placeholder="id" v-model="form.id"
                                       readonly>
                            </div>
                            <div class="form-group">
                                <label for="descricao">Descrição</label>
                                <input type="input" class="form-control" id="descricao" placeholder="Descricao"
                                       v-model="form.descricao">

                                <label for="preco">Preço</label>
                                <input type="input" class="form-control" id="preco" placeholder="Preco"
                                       v-model="form.preco">

                                <!--<label for="name">Endereço</label>-->
                                <!--<textarea class="form-control" rows="5" id="address" v-model="form.address"></textarea>-->

                            </div>


                            <div class="row">
                                <div class="form-group col-xs-12 col-sm-6">
                                    <label for="idCargo">Marca</label>
                                    <select id="idCategory" class="form-control" v-model="marca">
                                        <option v-for="category in categories" value="{{category.id}}">
                                            {{category.nome}}
                                        </option>
                                    </select>

                                </div>

                            </div>

                            <button @click.prevent="saveSupplier" class="btn btn-default"
                                    :disabled="condicao">Salvar
                            </button>
                            <button @click.prevent="Limpar" class="btn btn-default" >Limpar
                            </button>
                            <Loading></Loading>
                            <button @click.prevent="deleteSupplier" class="btn btn-default pull-right"
                                    :disabled="form.id==null">Apagar
                            </button>
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
    import DataService from '../services/DataService'
    import {URL} from '../config.js'

    export default {
        components: {
            Loading, Error, Pagination
        },
        created() {
            this.loadProdutos();
            this.carregarMarcas();
        },
        data() {
            return {
                condicao: false,
                categories: [],
                keyword: "",
                produtos: [],
                form: {},
                marca: null

            }
        },
        methods: {
            newSupplier() {
                this.form = {}
            },
            saveSupplier() {
                let self = this;
                self.condicao = true

                self.form['fkMarca'] = self.marca

                if (self.form.id == null) {
                    DataService.post("produtos", self.form)
                        .then(response => {
                                self.condicao = false
                                self.loadProdutos()
                            },
                            error => {

                            }).finally(function () {
                        self.Limpar()
                    })
                } else {
                    DataService.put("produtos", self.form, self.form.id)
                        .then(response => {
                                self.condicao = false
                                self.loadProdutos()
                            },
                            error => {

                            }).finally(function () {
                        self.Limpar()
                    })

                }

            },
            editar(supplier) {

                for (var i = 0; i < this.categories.length; i++) {
                    if (this.categories[i].id === supplier.fkMarca) {
                        this.marca = this.categories[i].id
                        this.form = supplier
                    }
                }
            },
            deleteSupplier() {
                if (confirm(`Deseja apagar " ${this.form.descrcao} " ?`)) {

                    let t = this;
                    DataService.delete("produtos", this.form.id)
                        .then(response => {
                                t.loadProdutos()
                            },
                            error => {

                            }).finally(function () {
                        t.Limpar()

                    })

                }
            },
            loadProdutos() {
                let t = this;
                DataService.getAll("produtos")
                    .then(response => {
                            t.produtos = JSON.parse(response.data)
                        },
                        error => {
                            console.log("Error: ", error)
                        }).finally(function () {

                })
            },
            carregarMarcas() {
                DataService.getAll("marcas")
                    .then(response => {
                            this.categories = JSON.parse(response.data)
                            /// console.log(JSON.parse( response.data))

                        },
                        error => {

                        }).finally(function () {

                })
            },
            Limpar() {

                this.form = {}
            },
        }


    }
</script>
