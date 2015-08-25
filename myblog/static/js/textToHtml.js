$(document).ready(function(){
	var $article_content = $(".article_content"),
		i
		;
	console.log("len: " + $article_content.length);
	for (i = $article_content.length - 1; i >= 0; i--) {
		console.log("for");
		$article_content.eq(i).html($article_content.eq(i).text());
		$article_content.eq(i).removeClass("hide");
	}

})