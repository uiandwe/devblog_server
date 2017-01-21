Vue.config.delimiters = ["[[","]]"]

var blogDetail = new Vue({
    el: '#blog_detail',
    data: {
        post_data: {}
    },
    methods: {
        get_domain_name(url){
            var matches = url.match(/:\/\/(?:www\.)?(.[^/]+)(.*)/);
            return matches
        }
    },
    ready: function()
    {
        this.$http.get('/api'+this.get_domain_name(window.location.href)[2]).then(function (response) {
            this.post_data = response.data;
        },
        function (response) {
            console.log(response);
        });
    }
});