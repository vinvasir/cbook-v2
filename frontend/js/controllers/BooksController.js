function BooksController(book, $http, AuthorService, genres){
	var bookCtrl = this;

	this.bookData = book.data;

	if(genres){
		this.genres = genres.data;
	}

	this.newBook = {genres: []};

	this.addBook = function(){
		console.log(bookCtrl.newBook);
		debugger;
		$http
			.post('http://127.0.0.1:8000/books/json/', bookCtrl.newBook)
			.then(function(res){
				console.log(res.data);
				bookCtrl.bookData.push(res.data);
			});
		
		bookCtrl.newBook = {genres: []};			
	};
}

angular
	.module('app')
	.controller('BooksController', BooksController);