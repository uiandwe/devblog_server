Vue.config.delimiters = ["[[","]]"]

var blogCreate = new Vue({
    el: '#blog_create',
    data: {
        userId: 0,
        csrfmiddlewaretoken: ''
    },
    methods: {
        createPostSend: function () {
            var body = {
                content : CKEDITOR.instances.editor1.getData(),
                title : document.getElementsByName('title')[0].value,
                category : document.getElementsByName('category')[0].value,
                userId: this.userId,
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value

            };

            console.log(body)

             $.ajax({
                 url : '/api/blog/create/',
                 type: "POST",
                 data : body,
                 dataType : "json",
                 success: function( data ){
                     alert("생성하였습니다 ");
                     window.location.href = '/';
                 }
             });

        },

    },
    ready: function()
    {

    }
});
