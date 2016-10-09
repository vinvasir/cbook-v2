function BooksController($http, book){
	var bookCtrl = this;

	bookCtrl.bookData = book.data;
}

angular
	.module('app')
	.controller('BooksController', BooksController)