

Vue.config.delimiters = ["[[","]]"]

var app = new Vue({
    el: '#app',
    data: {
        'apptitle': 'Django Vue.JS Job Board',
        'jobs': [],
        title: 'blog',
        blog_list:[
            {
                'title': '처음 타보는 퍼스트 클래스, ANA NH211 - 후편',
                'category': 'travel',
                'date': '03 Oct 2016',
                'link': '/blog/detail/'
            }
        ]

    },
    methods: {
        addJob: function () {
            var newJob = {
                jobtitle: this.jobtitle.trim(),
                jobdescription: this.jobdescription.trim()
            };

            this.$http.post('http://127.0.0.1:8000/api/jobs/', newJob);
        },
        removeJob: function (index) {
            this.$http.delete('http://127.0.0.1:8000/api/jobs/'.concat(this.jobs[index].id));
            this.jobs.splice(index, 1);
        }
    },
    ready: function()
        {

        }
});