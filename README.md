# Election_Analysis

## Overview of Election Audit
### Since we helped Seth and Tom figure out who the winner was from the election and gathered the information requested from them. The election commission requested we figure out which county had the highest turnout. However, since they only requested the highest turnout, more details were added to that request. These details follow the same requests Seth and Tom had originally requested. Essentially, making the commissions request slightly more detailed. 

## Election-Audit Results:

   * How many votes were cast in this congressional election? 
   * * **369,711**
   * Precinct total votes and relative percentages
   * * Jefferson: (38,855) - **10.509560 % or 10.51 %**
   * * Denver: (306,055) - **82.782227 % or 82.78 %**
   * * Arapahoe: (24,801) - **6.708213 % or 6.71 %**
   * Which county had the largest number of votes?
   * * **Denver with 306,055**
   * Candidate total votes and relative percentages
   * * Charles Casper Stockham: **(85,213) - 23.0%**  
   * * Diana DeGette: **(272,892) - 73.8%** 
   * * Raymon Anthony Doane: **(11,606) - 3.1%** 
   * Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
   * * **Diana DeGette won the election with 272,892 and 73.8% of the total votes**

![Election Results](https://github.com/Greekman12490/Election_Analysis/blob/main/Resources/Election%20Results.png?raw=true)
   
## Election-Audit Summary: 
### The code written can be used for other elections if the commission would like to use it. However, certain lines of the code should cater to future elections. For example, if the results were written in a different file than file used in the code, than this should mirror that. The code used was: ```"file_to_load = os.path.join("Resources", "election_results.csv")"```. The "election_results.csv" was the file used to load relative data to establish our results. If the commission used the same file, the results would not be what they expect if they use the code for future elections. Since we saved the results to the file named  "election_analysis.txt" using the code ```"file_to_save = os.path.join("analysis", "election_analysis.txt")"```. We can change the last part of the code to whatever text file the commission would like to name it to store the results. As a precaution though, the file MUST be created prior to writing the code. Otherwise, an error will occur. These would be two examples of what could be changed. Overall, it will sort through the data and provide the necessary information like the results shown above.
