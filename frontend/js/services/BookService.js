function BookService($http){
	this.getBooks = function(){
		return $http.get('http://127.0.0.1:8000/books/json');
	}

	this.getBook = function(id){
		return $http.get('http://127.0.0.1:8000/books/json/' + id);
	}
}


angular
	.module('app')
	.service('BookService', BookService)