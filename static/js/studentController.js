angular.module('myApp').controller('studentController',['$scope','$http',function($scope,$http) {
var url="http://127.0.0.1:8000/snippets/1";
   $http.get(url).success( function(response) {
                           $scope.students = response;
                        });
 
}]);
