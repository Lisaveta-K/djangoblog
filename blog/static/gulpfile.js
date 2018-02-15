// Include gulp
var gulp = require('gulp');

// Include Our Plugins
var less = require('gulp-less');

var postcss = require('gulp-postcss'),
    autoprefixer = require('autoprefixer'),
    lost = require('lost');

gulp.task('css', function () {
  gulp
      .src('./less/blog.less')
      .pipe(less({
        strictMath: true
      }))
      .pipe(postcss([
        lost(),
        autoprefixer({
          browsers: [
            '> 1%',
            'last 3 versions',
            'iOS >= 7',
            'IE >= 9',
            'Firefox >= 18',
            'Opera >= 14',
            'Safari >= 8',
            'Android >= 2.1',
            'ExplorerMobile >= 10'
          ]
        })
      ]))
      .pipe(gulp.dest('./css'));
});

gulp.task('watch', function () {
  gulp.watch('./less/**/*.less', ['css']);
});