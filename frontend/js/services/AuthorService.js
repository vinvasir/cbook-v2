function AuthorService($http){
	this.getAuthor = function(id){
		return $http.get('http://127.0.0.1:8000/authors/' + id + '/json/');
	};
}

angular
	.module('app')
	.service('AuthorService', AuthorService);