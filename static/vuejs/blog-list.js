Vue.config.delimiters = ["[[","]]"]

var blogList = new Vue({
    el: '#blog_list',
    data: {
        blog_list:[]
    },
    methods: {

    },
    ready: function()
    {
        this.$http.get('/api/blog/').then(function (response) {
            this.blog_list = this.blog_list.concat(response.data);
        });
    }
});

Vue.filter('DDMMYYYY', function(date){
    var dt = new Date(date);

    var mm = dt.getMonth();
    var dd = dt.getDate();

    var monthShortNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

    return [(dd>9 ? '' : '0') + dd, monthShortNames[mm] , dt.getFullYear()].join(' ');

});