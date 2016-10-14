angular
	.module('app', ['ui.router'])
	.config(function($stateProvider){
		$stateProvider
			.state('home', {
				url: '/',
				templateUrl: 'js/templates/home.html'
			})
			.state('books', {
				url: '/books',
				templateUrl: 'js/templates/books/list.html',
				controller: 'BooksController as bookCtrl',
				resolve: {
					book: function($stateParams, BookService) {
						return BookService.getBooks();
					}
				}
			})
			.state('books.new', {
				url: '/books/new',
				templateUrl: 'js/templates/books/new.html'
			})
	});