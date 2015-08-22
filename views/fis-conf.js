/*辅助开发、文件监听、自动编译、自动刷新
 *添加 --lint 或 -l 参数，支持在编译的时候根据项目配置自动代码检查
 *添加 --test 或 -t 参数，支持在编译的时候对代码进行自动化测试
 */
fis.config.merge({
	modules : {
		// parser.less表示设置后缀名为less的文件的parser，第二个less表示使用fis-parser-less进行编译
		parser : {
			less : 'less',
			coffee : 'coffee-script',
			jade : 'jade'
		},
		// preprocessor : {
	 //    	//css后缀文件会经过fis-preprocessor-image-set插件的预处理
	 //    	css : 'image-set'
		// },
		// 解释：在fis对js、css和类html文件进行语言能力扩展之后调用的插件配置，可以根据 文件后缀 对文件进行后处理。该阶段的插件可以获取文件对象的完整requires信息。
		postprocessor : {
			js : 'jswrapper'
		},
		// 单文件编译过程中的代码检查插件。
		lint : {
			js : 'jslint'
		},

		// 解释：单文件编译过程中的自动测试插件。
        //js后缀文件会经过fis-test-phantomjs插件的测试
        test : {
	        js : 'phantomjs'
        },
        // 单文件编译过程中的最后阶段，对文件进行优化。
        optimizer : {
        	js : 'uglify-js',
        	css : 'clean-css',
        	png : 'png-compressor'
        },
        // 在fis打包操作前调用的插件， 不管调用fis release命令时是否使用 --pack 参数，该插件均会被调用。
        // prepackager : 'oo,xx'
        //打包调用fis-packager-your_packager插件进行处理
        // packager : 'your_packager'
        // 解释：打包后处理csssprite的插件。
        // spriter : 'your_spriter'
		// 解释：打包后处理插件。
        // 在fis打包操作后调用的插件， 不管调用fis release命令时是否使用 --pack 参数，该插件均会被调用。
        // postpackager : 'your_postpackager'

	}
})

fis.config.merge({
	roadmap : {
		//将less文件编译为css
		ext : {
			less :'css',
			coffee : 'js',
			jade : 'html'
		},
		// all css and js file add domain like http://localhost:8080
		// html 所有引用的资源都会加上domain
		// 貌似没有什么用处
		domain : {
			'**.css' : 'http://localhost:8080',
			'**.js' : 'http://localhost:8080'
		},
		path : [
			{
				//  all js files
				reg : /^\/static\/js\/(.*\.(?:js|coffee))/i,
				// release at path like '/static/js'
				release : 'static/js/$1'
			},
			{
				reg : /^\/static\/css\/(.*\.(?:css|less))/i,
				release : 'static/css/$1'
			},
			{
				reg : /^\/static\/images\/(.*\.(?:png|gif|jpg|json|mp3|jpeg|bmp))/i,
				release : '/assets/$1'
			},
			{
				reg : /^\/static\/fonts\/(.*\.(?:eot|svg|ttf|woff))/i,
				release : '/fonts/$1'
			}
			// {
			// 	reg : /^\/resource\/assets\/640\/number.fnt/i,
			// 	release : '/assets/number.fnt'
			// },
			// {
			// 	reg : /^\/resource\/assets\/640\/buttons.json/i,
			// 	release : '/assets/buttons.json'
			// },
			// {
			// 	reg : /^\/resource\/assets\/640\/levels.json/i,
			// 	release : '/assets/levels.json'
			// }
		]
	},
	// 项目配置
	project : {
		charset : 'utf-8',
		md5Length : 7,
		md5Connector : '_',
		include : '**'			
	},
	pack : {
        //打包所有的demo.js, script.js文件
        //将内容输出为static/pkg/aio.js文件
        'game.js' : ["static/js/homepage.js", "static/js/config.js", "static/js/egret_require.js", "static/js/egret_loader.js", "static/js/game-min.js"],
        //打包所有的css文件
        //将内容输出为static/pkg/aio.css文件
        'game.css' : '**.css'
    },
    deploy: {
		dist: {
			to: "./dist"
		}
	}
});
