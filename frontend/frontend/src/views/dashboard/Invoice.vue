<template>
    <div class="page-invoice">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Invoice - {{ invoice.invoice_number }}</h1>
            </div>

            <div class="column is-12 mb-4">
                <h3 class="is-size-4 mb-5">Client</h3>

                <p><strong>{{ invoice.client_name }}</strong></p>
                    
                <p v-if="invoice.client_address1">{{ invoice.client_address1 }}</p>
                <p v-if="invoice.client_address2">{{ invoice.client_address2 }}</p>
                <p v-if="invoice.client_zipcode || invoice.client_place">{{ invoice.client_zipcode }} {{ invoice.client_place }}</p>
                <p v-if="invoice.client_country">{{ invoice.client_country }}</p>
            </div>

            <div class="column is-12 mb-4">
                <h3 class="is-size-4 mb-5">Items</h3>

                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Title</th>
                            <th>Quantity</th>
                            <th>Amount</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr 
                            v-for="item in invoice.items"
                            v-bind:key="item.id"
                        >
                            <td>{{ item.title }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>{{ item.net_amount }}%</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'Invoice',
        data() {
            return {
                invoice: {},
                items: []
            }
        },
        mounted() {
            this.getInvoice()
        },
        methods: {
            getInvoice() {
                const invoiceID = this.$route.params.id

                axios
                    .get(`/api/v1/invoices/${invoiceID}`)
                    .then(response => {
                        this.invoice = response.data
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
            }
        }
    }
</script>