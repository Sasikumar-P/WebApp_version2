angular.module('myApp').controller('student5Controller',['$scope','$http',function($scope,$http) {

$scope.pushh = function() {
	
        data= {
	malayalam: $scope.malayalam,
	physics:$scope.physics,
	chemistry:$scope.chemistry,
        maths:$scope.maths
};
   var url="http://127.0.0.1:8000/mark/";
    $http.post(url,data).success( function(response){
      $scope.hello = response;

    });
}
var data = {
	$scope.malayalam : ""
	$scope.physics : ""
	$scope.chemistry : ""
	$scope.maths : ""

}]);
