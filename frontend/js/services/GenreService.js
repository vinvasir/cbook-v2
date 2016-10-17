function GenreService($http){
	this.getGenres = function(){
		return $http.get('http://127.0.0.1:8000/genres/json');
	}
}

angular
	.module('app')
	.service('GenreService', GenreService);