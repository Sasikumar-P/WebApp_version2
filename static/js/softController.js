angular.module('myApp').controller('softController',['$scope','$http',function($scope,$http) {
  var url="http://127.0.0.1:8000/soft/";
    $http.get(url).success( function(response){
      $scope.hard = response;

    });

}]);
