function BookDetailController(book){
	var bookCtrl = this;

	this.bookData = book.data;
}

angular
	.module('app')
	.controller('BookDetailController', BookDetailController);