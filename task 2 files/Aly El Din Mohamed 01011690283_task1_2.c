/*
 * File: Aly El Din Mohamed El Sayed 01011690283_task1_2
 * Author: Aly El Din Mohamed El Sayed
 * Description: counting down starting from a positive number until we reach zero, with delaying one second
 * Date: 13/8/2023
 */



 /*Header files*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//function takes number of seconds as an argument and do a while loop for this number of seconds until the loop breaks
void delay(int numberOfSeconds){
    int milliSeconds=1000*numberOfSeconds;
    clock_t start=clock();
    while(clock()<start+milliSeconds);
}
int main()
{
    //Counting Down with bonus
    int countDown=0;
    do{
        scanf("%d",&countDown);
        if(countDown<0){
            printf("There is no time with negative value!!\ntry again\n");
        }
    }while(countDown<0);

    while(countDown!=0){
        printf("%d\n",countDown);
        delay(1);
        countDown--;
    }
    printf("Blast off to the moon!");
}
