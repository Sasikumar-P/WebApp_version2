angular.module('myApp').controller('student7Controller',['$scope','$http',function($scope,$http) {
  var url="http://127.0.0.1:8000/note/";
    $http.get(url).success( function(response){
      $scope.page = response;

    });

}]);
