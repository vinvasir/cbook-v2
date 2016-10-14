function BookService($http){
	this.getBooks = function(){
		return $http.get('http://127.0.0.1:8000/books/json');
	}
}


angular
	.module('app')
	.service('BookService', BookService)