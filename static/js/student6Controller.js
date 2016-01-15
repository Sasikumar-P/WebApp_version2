angular.module('myApp').controller('student6Controller',['$scope','$http',function($scope,$http) {

  $scope.page = {};

  $scope.pages = [];

 $http.get('http://127.0.0.1:8000/note/').success(function(pages){
        $scope.pages = pages;
    });
$scope.pushhh = function(page) {
	
       
   var url="http://127.0.0.1:8000/note/";
    $http.post(url,page).success( function(){
      $scope.pages.push(page);
      $scope.page = {};
    });
}

}]);
