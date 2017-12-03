<template>
    <div class="panel panel-default">
        <div class="panel-heading">
            <div class="row">
                <div class="col-xs-6">
                    <h4>Funcionarios </h4>
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
                            <th width="50%">Nome</th>
                            <th width="50%">CPF</th>
                            <th width="30%">Ações</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="supplier in funcionarios">
                            <td>{{supplier.id}}</td>
                            <td>{{supplier.nome}}</td>
                            <td>{{supplier.cpf}}</td>
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
                                <label for="name">Nome</label>
                                <input type="input" class="form-control" id="name" placeholder="Nome"
                                       v-model="form.nome">

                                <label for="email">Email</label>
                                <input type="input" class="form-control" id="email" placeholder="Email"
                                       v-model="form.email">

                                <!--<label for="name">Endereço</label>-->
                                <!--<textarea class="form-control" rows="5" id="address" v-model="form.address"></textarea>-->

                            </div>
                            <div class="row">
                                <div class="form-group">
                                    <div class="col-sm-6">
                                        <label for="cpf">CPF</label>
                                        <input type="input" class="form-control" id="cpf" placeholder="CPF"
                                               v-model="form.cpf">
                                    </div>

                                    <div class="col-sm-6">
                                        <label for="cpf">Telefone</label>
                                        <input type="input" class="form-control" id="telefone" placeholder="Telefone"
                                               v-model="form.telefone">
                                    </div>

                                </div>
                            </div>

                            <div class="row">
                                <div class="col-sm-6">
                                    <label for="celular">Celular</label>
                                    <input type="input" class="form-control" id="celular" placeholder="Celular"
                                           v-model="form.celular">
                                </div>

                                <div class="form-group col-xs-12 col-sm-6">
                                    <label for="idCargo">Cargo</label>
                                    <select id="idCategory" class="form-control" v-model="cargo">
                                        <option v-for="category in categories" value="{{category.id}}">
                                            {{category.nome}}
                                        </option>
                                    </select>

                                </div>

                            </div>

                            <button @click.prevent="saveSupplier" class="btn btn-default"
                                    :disabled="condicao">Salvar
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
            this.loadFuncionarios();
            this.carregarCargos();
        },
        data() {
            return {
                condicao: false,
                categories: [],
                keyword: "",
                funcionarios: [],
                form: {},
                cargo: null

            }
        },
        methods: {
            newSupplier() {
                this.form = {}
            },
            saveSupplier() {
                let self = this;
                self.condicao = true

                self.form['fkCargo'] = self.cargo

                if (self.form.id == null) {
                    DataService.post("funcionarios", self.form)
                        .then(response => {
                                self.condicao = false
                                self.loadFuncionarios()
                            },
                            error => {

                            }).finally(function () {
                        self.Limpar()
                    })
                } else {
                    DataService.put("funcionarios", self.form, self.form.id)
                        .then(response => {
                                self.condicao = false
                                self.loadFuncionarios()
                            },
                            error => {

                            }).finally(function () {
                        self.Limpar()
                    })

                }

            },
            editar(supplier) {

                for (var i = 0; i < this.categories.length; i++) {
                    if (this.categories[i].id === supplier.fkCargo) {
                        this.cargo = this.categories[i].id
                        this.form = supplier
                    }
                }
            },
            deleteSupplier() {
                if (confirm(`Deseja apagar "${this.form.name}"s ?`)) {
                    this.showLoading()
                    let t = this;
                    this.$http.delete(`${URL}/supplier/${this.form.id}`).then(response => {
                            t.form = {}
                        },
                        error => {
                            t.setError(error.body)
                        }
                    ).finally(function () {
                        t.hideLoading()
                        this.loadSuppliers();
                    })
                }
            },
            loadFuncionarios() {
                let t = this;
                DataService.getAll("funcionarios")
                    .then(response => {
                            t.funcionarios = JSON.parse(response.data)

                        },
                        error => {
                            console.log("Error: ", error)
                        }).finally(function () {

                })
            },
            carregarCargos() {
                DataService.getAll("cargos")
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
