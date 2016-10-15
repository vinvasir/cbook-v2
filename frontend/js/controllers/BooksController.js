function BooksController(book, $http, AuthorService){
	var bookCtrl = this;

	this.bookData = book.data;

	this.newBook = {};

	this.addBook = function(){
		console.log(bookCtrl.newBook);
		$http
			.post('http://127.0.0.1:8000/books/json/', bookCtrl.newBook)
			.then(function(res){
				console.log(res.data);
				bookCtrl.data.push(res.data);
			});
		
		bookCtrl.newTask = {};			
	};
}

angular
	.module('app')
	.controller('BooksController', BooksController);