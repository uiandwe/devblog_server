var gulp = require('gulp');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var minifyCss = require('gulp-minify-css');
var browserSync = require('browser-sync').create();
var browserify = require('browserify');
var source = require('vinyl-source-stream');
var buffer = require('vinyl-buffer');
var babel = require('gulp-babel');
var sass = require('gulp-sass');




gulp.task('minifycss', function() {
    return gulp.src('static/src/css/*.css')
        .pipe(concat('index.css'))
        .pipe(minifyCss({compatibility: 'ie8'}))
        .pipe(gulp.dest('static/css/'))
        .pipe(browserSync.reload({stream:true}));
});

gulp.task('compile-sass', function () {
    return gulp.src('static/src/scss/main.scss')
        .pipe(sass())
        .pipe(minifyCss({compatibility: 'ie8'}))
        .pipe(gulp.dest('static/css/'))
        .pipe(browserSync.reload({stream:true}));
});


gulp.task('babel', function() {
    return gulp.src('static/src/js/*.js')
        .pipe(babel())
        .pipe(gulp.dest('static/js/'))
        .pipe(browserSync.reload({stream:true}));
});


gulp.task('watch', function(){
    gulp.watch('static/src/js/*.js', ['babel']) ;
    gulp.watch('static/src/css/*.css',['minifycss']);
    gulp.watch('static/src/scss/*.scss',['compile-sass']);

});


gulp.task('default', ['watch']);