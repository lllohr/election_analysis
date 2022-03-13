# Election Analysis

## Overview of Project

The specifics of this project were to conduct an election audit for the Colorado Board of the Elections. The Elections Commission is looking for specific data analysis on a congressional race in a Colorado precinct. Initially, the specifications were to audit the winner of the election and the final project required a tabulation of the votes in each of the Colorado counties. 

### Purpose
The project required using the data to calculate the total number of votes cast in the election, a complete list of all candidates, how many votes each candidate received, calculation of the percentage of the votes for each candidate received and determining the winner based on popular vote. Our job is to send a report with election results for the congressional precinct. 

## Analysis and Challenges
Here are the election results:

![Election_Results](https://github.com/lllohr/election_analysis/blob/main/Resources/Election_Results.png)

<b>•	How many votes were cast in this congressional election?</b>

The total number of votes cast in this congressional election was 369,711.

<b>•	Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.</b>

County Votes:
Jefferson: 10.5% (38,855);
Denver: 82.8% (306,055);
Arapahoe: 6.7% (24,801).

<b>•	Which county had the largest number of votes?</b>

Denver had the largest turnout and therefore, the largest number of votes.

<b>•	Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.</b>

Charles Casper Stockham received 23.0% of the vote, with 85,213 votes.
Diana DeGette received 73.8% of the vote, with 272,892 votes.
Raymon Anthony Doane received 3.1% of the vote, with 11,606 votes.

<b>•	Which candidate won the election, what was their vote count, and what was their percentage of the total votes?</b>

Diana DeGette won the election with 82.8% of the popular vote and 272,892 votes. 

### Challenges and Difficulties Encountered
My biggest challenge completing this task was combining the initial data analysis for the candidates with the county analysis. I reused the code from the initial data analysis of the candidate results by recopying it into the new analysis and changing the variables. I was able to use the starter code very efficiently. It didn't take too long to begin printing and writing the country data to the terminal and the file. Where I ran into the biggest challenges was combining the code. I didn't realize it at the time, but I had broke my code with repetition of lines of code I'd already introduced into the file. I was able to use the debugging tool in Visual Studio to comb through my code line-by-line until I identified where it was broken. I had to walk away from the project to regain some objectivity and composure. 

The last challenge that really stumped me was the spacing on the print to terminal and writing to the file. I attempted to emulate the exact spacing of the image in the project specs. I experimented with the \N operator in Python until it looked like the image. Alas! I was able to achieve success!

## Election-Audit Summary:
This election audit was a robust analysis of a single congressional precinct election. Can you imagine what this code could do on a larger scale? Will some modifications, this code could audit the presidential election results for each county is the state. For local elections, with just a code of modifications, the winner of the local elections could be verified. 

For example, the election results for the city of Denver for the local elections (judges, mayorial, city council, school board, etc) could be tabulated from a simple .csv file contatining the votes. The code could read and tabulate the votes and then automatically reveal the winner. The total votes of each election and each race could be tabulated and written to a file for the election board to view. This code is flexible enough, it could be modified to include numerous candidates and the winners of multiple races or than the congressional races. Just as I was able to drill down into the county data, I could look at cities and towns within the counties and analyze the election data. 

