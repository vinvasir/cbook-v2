function BooksController(book, $http){
	var bookCtrl = this;

	this.bookData = book.data;
}

angular
	.module('app')
	.controller('BooksController', BooksController);