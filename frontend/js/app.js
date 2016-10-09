angular
	.module('app', ['ui.router'])
	.config(function($stateProvider){
		$stateProvider
			.state('home', {
				url: '/home',
				templateUrl: 'js/templates/home.html'
			})
			.state('books', {
				url: '/books',
				templateUrl: 'js/templates/books.html'
			})
	});