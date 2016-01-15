angular.module('myApp').controller('student4Controller',['$scope','$http',function($scope,$http) {
  var url="http://127.0.0.1:8000/mark/";
    $http.get(url).success( function(response){
      $scope.st = response;

    });

}]);
