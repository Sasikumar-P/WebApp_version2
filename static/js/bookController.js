angular.module('myApp').controller('bookController',['$scope','$http',function($scope,$http) {
  var url="http://127.0.0.1:8000/book/";
    $http.get(url).success( function(response){
      $scope.hard = response;

    });

}]);
