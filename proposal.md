# Proposal

## What will (likely) be the title of your project?

Basic Strategy Blackjack

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

A fully functional blackjack game that compares player moves to basic strategy.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

The game is going to be a fully functional blackjack game. It will include splits, doubles, etc. I plan on starting the user with some amount of money, and sticking with a standard bet every turn which could then be doubled. The game will end when the player either chooses to end the game or runs out of money. Every turn, the program will run a monte carlo to get the win-loss ratio of the player's turn compared to the win-loss ratio of basic strategy in the same situation. This should also take into account expected value so that bets that could be doubled would be worth more. At the end of the game, the player will get a score related to how well they scored compared to basic strategy. 

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

N/A

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

N/A

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

A good outcome will be if I get a playable blackjack game that calculates win-loss ratio. I will be able to accomplish this no matter what. 

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

A better outcome would include programming in basic strategy and comparing the player's moves to that using a monte carlo with a win-loss ratio. I believe I will be able to accompish this by the project deadline.

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

The best outcome would be if I could do all of the above and then also take into account betting, blackjack playing 3:2, and comparing to basic strategy based on expected value rather than just win-loss ratio. I hope to be able to accomplish that but it'll involve some trial and error for sure. 

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

My first step will be to outline what functions will do what in the program. The first thing I am going to try to do is program in each of the cards and their values, as well as how they would be dealt out randomly or shuffled. I'm going to have to read more about the random library to do that. Then I am going to have to program in a set of acceptable moves for each situation and prompt the user for those moves. I'll probably make it so that it starts at $300 and bets $10 every time just to keep track of the moves. After I have a functional blackjack game, I will program in basic strategy and try to keep track of the win-loss ratio of the player's moves with basic strategy. The last thing I'll do is try to make this win-loss ratio into expected value and make blackjack play 3:2. Overall, I think I'll need to look at code of similar games to see how it is laid out and I'll have to research more about what the random library can do in terms of a card game. I'll need to get better at using functions because I think this code will have to use a bunch of functions that call eachother so that I can test each part individually rather than big blcoks of code. 
