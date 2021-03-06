function BooksController(book, genre, $http){
	var bookCtrl = this;

	this.bookData = book.data;

	if(genre.data) {
		this.genreData = genre.data;
	}
	
	this.newBook = {genres: []};

	this.addBook = function(){
		bookCtrl.newBook.genres.push(bookCtrl.newBook.newGenre);
		console.log(bookCtrl.newBook);
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