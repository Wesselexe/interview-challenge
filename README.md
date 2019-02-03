# Pleo challenge

We would like you to create a user interface using any framework of your choise that solves the following problem.

## The problem

In this challenge, you are given a vector of heights and these heights form a structure like shown in the following figure.
 
![Figure 1](figure1.png)

Vector : **[2, 5, 1, 3, 1, 2, 1, 7, 7, 6]**
 
It is now raining over the structure and the water starts flowing onto the cells.  The water in a cell always flows to the neighboring cell of least height - if it is not already occupied by water or a block. All the neighboring cells that drains into a sink are said to form a basin. 
 
![Figure 2](figure1.2.png)
 
Observe that the structure is thereby partitioned into basins. You need to determine the number of unit of water contained in all basins. In this example the input for this program is [2, 5, 1, 3, 1, 2, 1, 7, 7, 6] and the output is 17 units of water.

## The objective

The goal is to create an optimal algorithm that given any array will output the correct units of water. Please make a user interface to enter the values and visualize the solution.

## Instructions

Fork this repo with your solution. We want to see your progression through commits (so don’t commit the entire solution in 1 step). You sould also edit the README.md to explain your solution.

Solutions for the algorithmic part are possible to find online. Please be advised though that we do expect you to try and solve this without just googling the solution. In the end the most interesting thing is not whether you have the _absolute most optimal_ algorithm, but rather your thought process and work on how you arrived to your solution.

Happy hacking 😁!

## First attempt:
The function made is very simple and manage to solve the challenge with the given array/list. But as the crafty programmer
I am, I realize we might need to further test the function to make sure the result is not simple luck.
Furthermore, I will need to account for edge cases. fx what if one of the "cells height" that is given is 0?
(Spoiler alert, I cheated a bit and talked to Marc. If 0 is given within a basin, the water will fall through.)

After adding another random test and finding the result by visualizing the grid on a piece of paper, one thing was clear
I made a huge plunder, will go back to the drawing board and make sure basins are calculated correctly!

## Second attempt:
After realizing the function did have unexpected behavior, I decided to go back and make the function more work correctly
with lists that have the highest cells before a basin/well forms. Now the function checks through the list both in the
regular order and in reverse, then lastly the 2 outcomes are compared and where they overlap the result is calculated from.
