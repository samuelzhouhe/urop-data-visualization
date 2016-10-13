/**
 * Created by Samuel on 13Oct2016.
 * Contains helper functions which are coded per Google Javascript Style Guide
 */


var getDistanceTraveled = function(locationsArray){
    var distanceTraveled = 0;
    var prevCoordinate =  L.latLng(locationsArray[0][0], locationsArray[0][1]);
    for (var i=1; i<locationsArray.length;i++){
        var currentCoordinate = L.latLng(locationsArray[i][0],locationsArray[i][1]);
        distanceTraveled += currentCoordinate.distanceTo(prevCoordinate);
        prevCoordinate = currentCoordinate;
    }
    return distanceTraveled;
};