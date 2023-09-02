/*
 * File: Aly El Din Mohamed El Sayed 01011690283_task1_4
 * Author: Aly El Din Mohamed El Sayed
 * Description:implementing kalman filter to reduce noise of the readings of the sensors to output the optimal measurments
 * Date: 13/8/2023
 */

/*approach
since the second sensor's accuracy is more trusted than the first sensor's accuracy
therefore the expected measurement should be close to the maximum of the second array
so that I decided that the
*/


/*Header Files*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*Hardcoding sensors readings*/
static float mpu6050[10] = {0.0, 11.68, 18.95, 23.56, 25.72, 25.38, 22.65, 18.01, 10.14, -0.26};
static float bno55[10] =   {0.0,9.49, 16.36, 21.2, 23.16, 22.8, 19.5, 14.85, 6.79, -2.69};
static float optimalMissilePosition[10];


/*functions prototype*/
float newErrorInEstimate(float prev_kalman_gain,float prev_error_in_estimate);
void currentEstimate(int index,float kalman_gain);
float kalmanGain(float estimateError,float measureError);


/*
Laws used in computing:
kalman gain=error in estimate/(error in estimate+error in measurement)

current estimate=prev. estimate+Kalman gain * (measure-prev.estimate)

new estimate state error=(1-kalman gain)*prev.estimate


*/


float newErrorInEstimate(float prev_kalman_gain,float prev_error_in_estimate){
    return (1-prev_kalman_gain)*prev_error_in_estimate;
}

void currentEstimate(int index,float kalman_gain){
    float previousEstimate=bno55[index];
    optimalMissilePosition[index]=previousEstimate+kalman_gain*(mpu6050[index]-previousEstimate);
}

float kalmanGain(float estimateError,float measureError){
    return (float)estimateError/(estimateError+measureError);
}
int main(){
    //Declaration of array having the actual measurements using equation of motion of projectile

    float actual_measurements[10];

    //equation of motion of projectile-->   Y(t)=Y(0)+V(0)*t*sin(theta)-1/2*g*t^2
    actual_measurements[0]=0.0;
    for(int i=1;i<10;i++){
        actual_measurements[i]=30*(0.5*i)*sin(46)-0.5*9.8*(0.5*i)*(0.5*i);
    }


    int initialAngle=46,initialVelocity=30;
    float measuredPosition[10],initalErrorInEstimate=0.79,errorInMeasure=0.92;
    float initialKalmanGain=kalmanGain(initalErrorInEstimate,errorInMeasure);
    float Kg=initialKalmanGain,est=initalErrorInEstimate;
    for(int i=0;i<10;i++){
        currentEstimate(i,Kg);
        est=newErrorInEstimate(Kg,est);
        Kg=kalmanGain(est,errorInMeasure);
        printf("%f ",optimalMissilePosition[i]);
    }
}

