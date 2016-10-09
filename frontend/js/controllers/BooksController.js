function BooksController(book, $http){
	var bookCtrl = this;

	this.bookData = book.data;

	this.newBook = {};

	this.addBook = function(){

	};
}

angular
	.module('app')
	.controller('BooksController', BooksController);