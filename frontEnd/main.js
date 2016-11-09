var shenzhenMap = L.map('mapid').setView([22.544399, 114.039803], 11);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1Ijoic2FtdWVsaGUiLCJhIjoiY2lzeXR3N256MGV3MzJvcGd3Z3NnZXJheSJ9.tP7vfvSMJXdSmZbweB6IOw', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'samuelhe.1c6hdkgb'
    //accessToken: 'pk.eyJ1Ijoic2FtdWVsaGUiLCJhIjoiY2lzeXR3N256MGV3MzJvcGd3Z3NnZXJheSJ9.tP7vfvSMJXdSmZbweB6IOw'
}).addTo(shenzhenMap);

//var trajectory1 = L.polyline(locationsArray, {color: 'red'}).addTo(shenzhenMap);

var sztaxiApp = angular.module('shenzhenTaxis', []);
sztaxiApp.controller('sztaxiController', function ($scope, $http) {
    $scope.welcomeMsg = 'Welcome to Shenzhen Taxi Trajectory Visualization toolkit.';

    //Configuring start time
    $scope.startTime = new Date(1451664000000);
    $scope.startTimeOffset = 720;
    $scope.startTimeDisplay = moment($scope.startTime);
    $scope.$watch("startTimeOffset", function (newValue, oldValue) {
        $scope.startTime.setHours(0, $scope.startTimeOffset);
        $scope.startTimeDisplay = moment($scope.startTime).format("MMMM Do YYYY, h:mm:ss a");
    });

    //Configuring end time
    $scope.endTime = new Date(1451664000000);
    $scope.endTimeOffset = 720;
    $scope.endTimeDisplay = moment($scope.endTime);
    $scope.$watch("endTimeOffset", function (newValue, oldValue) {
        $scope.endTime.setHours(0, $scope.endTimeOffset);
        $scope.endTimeDisplay = moment($scope.endTime).format("MMMM Do YYYY, h:mm:ss a");
    });
    $scope.licensePlate = "";


    $scope.receiveTimestamps = function () {
        if ($scope.startTimeOffset > $scope.endTimeOffset || $scope.licensePlate === "") {
            alert("Not a valid time range");
        }
        else {
            $scope.partialLocations = [];
            console.log($scope.startTime.getTime());

            //Send http request
            var queryCriteria = {
                "timeRecorded": {
                    "$lt": $scope.endTime.getTime() / 1000,
                    "$gt": $scope.startTime.getTime() / 1000
                }, "licensePlate": $scope.licensePlate
            };
            $http.post('http://127.0.0.1:4000/queryFromDB', queryCriteria).then(function (res) {
                console.log(res);
                console.log(res.data);
                for (var i = 0; i < res.data.length; i++) {
                    console.log(res.data[i]);
                    $scope.partialLocations[i] = [res.data[i].latitude, res.data[i].longitude];
                    var trajectory1 = L.polyline($scope.partialLocations, {color: 'red'}).addTo(shenzhenMap);
                }
            }, function (res) {
                console.log(res);
            });
            $scope.licensePlate = "";
            $scope.startTimeOffset = 720;
            $scope.endTimeOffset = 720;
        }
    };
});
