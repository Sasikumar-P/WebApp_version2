angular.module('myApp').controller('student8Controller',['$scope','$http',function($scope,$http) {
  var url="http://127.0.0.1:8000/hard/";
    $http.get(url).success( function(response){
      $scope.hard = response;

    });

}]);
