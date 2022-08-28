
# Summary

The goal of this project/internship is to understand the role that floating point numbers play in the world of computer science (mathematical operations). Specifically, we focued on research that addressed the well known problem of lack of accuracy of floating point within computer science mathematics. Our task was to continue an ongoing paper (to be published) that has the end question of finding the probability of associativity within 3 floating point numbers through various combinations. Further we were tasked with creating a logic statement that encapsulates the associativity of each specific case.

During 2022 Avi Darbari as well as I (Rohan Udupa) worked on the case that included A,B <0 and C> 0.

## Previous Work
This has been an onging project that only last year was an addition to the Summer Preceptorship Program. Unlike many usual internships we were tasked with a mathematical challenge in order to be selected for this unique research oppurtunity. So far, through the work of past interns such as Mindy Kim, the project was in a conclusion state in which only the most difficult cases remained. This is where Avi and I picked up the project and were tasked with the A,B< 0 and C> 0 case. The complexity laid in the fact that when these numbers are commbined in different ways a borrow or a carry is sure to occur (something never addressed in the research before). With this in mind we were given control of defining these terms within the research in such a way that allowed for its longevity through the work.

From there we split the case into several branches and worked on takling the outputs and creating logic statements for every branch. Within our work we used the assistence of these python scripts we developed and refined for future interns. 

## The Code

### Intial Code
---
So what is the point of this code exactly? Well, through the internship we were tasked with verifying our logic statements. To do this we had to make truth tables and often times these would become huge and immpossible to do by hand without human mistakes. Thats when we used the code to develop all the possibile rows of a truth table depending on how many varibales it had. From there we were able to test the logic statements we derived by running it through the table to see if we got the expected results.  

### Logic Statements
---
We eventually got to a point where the logic statements were just getting more and more complicated as the number of variables were increasing. This lead to the use of a logic statement developer [website](http://www.32x8.com/var6.html). As you can see if you visit the site you are required to input the output for eacch and every line when trying to get a logic statement. For this reason, we had our python code create the table similiar to before and keep track of all the outputs. From there this allowed us to use the outputs to create a Webscraper.

### Webscraper
---
This was developed soley to allow for no human error when inputing data into the [website](http://www.32x8.com/var6.html). By using a selenium webdriver this allowed us to input all the values and effciently get a logic statement. As you may notrice in the code their are different webscrappers as the website is different depending on the number of variables.

## Dependencies
  -Selenium - This is the webdriver that we used to automate chrome.
      - In order to add this to your python script:
       
       1) Type "pip install selenium" into your terminal
  
  -Webdriver - A webdriver is also required this is the file known as *webdriver.exe*
      - In order to add this to your python script you will need to: 
      
       1) Install the webdriver from this [website](https://chromedriver.chromium.org/downloads)
       2) Point to where it is installed in your python script - replace this line- "path=Service("C:\chromedriver_win32 (1)\chromedriver.exe")"
  
  -Chrome Beta - The latest version of chrome is required - Chrome Beta
    - In order to implement this you will need to:
    
    1) Install the latest version of chrome from this [website](https://www.google.com/chrome/beta/)
    2) Point to where it is installed on your computer - replace this line with the correct path- "chrome_options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'"

