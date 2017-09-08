# Project 3 Milestone B Report
## **FATE** - Formulating Historical Society Growth for a Better World
<div style="text-align: right">
Colson Xu, Leo Liao, Yujia Lin, Yuxuan Lu
</div>

---

### Tentative Name
Our decision on the name of this game is **"FATE"**, as we want to give our target audience a message that the outcome of the game will be the ___fate___ of out world if we build our society the way the player did in the game.

<br>

### The Setting
Our game timeline starts at ancient time, before any civilization has formed. The earth's condition is optimized. The player will be shown a `10 * 10` green panel which also includes 9 blue squares represent ocean and 1 square represents glacier. Player will be able to take a series of operations including burn down trees, build house, mine coal, etc. To develop a civilization, player need to gain population, improve technology stratum, and build seamless interconnections between each operators. All operations in the game are things we participate in real life. The game board is a representation of some elements of our earth. i.e. grass, forest, glacier, and ocean.
The following aspect of our wicked problem will be implemented to the game:

  * __Deforestation__
  * __Glacial Melting__
  * __Industrialization__
  * __CO<sub>2</sub>__
  * __CH<sub>4</sub>__
  * __Forest Fire__
  * __Farming__
  * __Population__

Although it might seems like there are a lot of aspects in our game, one of the biggest aspect is actually left out on purpose. That is, the political factor. This is not in the game design because it is so complex and it is not something that happens in the natural world, thus, won’t make much sense to be in a natural simulation game.

<br>

### Initial Situation
The initial state of this game will be represented by a 10*10 panel with 9 blue squares representing the ocean and 1 square representing the glacier. Initially, there will be variables including __'Gold'__ (amount of money), __'Change in Temperature'__, __'LQ'__ (Living Quality Level) with a maximum value of 100 (player need to try their best maintaining LQ as high as possible). Initial __'Population'__ in the game will be 100 (players need to build more and more facilities to maintain a high LQ as it will decrease as the world becomes more and more crowded). Meanwhile, players must create empty spaces and collect materials to build a house within the first three turns of the game, or the population will drop rapidly, which leads to human extinction. Statistics will be provided at the bottom of the window showing values of each variable. Players should stay focused on these numbers as they are extremely valuable for making sustainable decisions.

Some of the operators will cost the player some __'Resources'__ as it will be unrealistic to do them for free. For example, building a __'Power Plant'__ will cost the player 5 __'Wood'__ and 15 __'Gold'__. A list of essential variables and their initial or maximum value is shown below.

  * __Initial Gold: 200__
  * __Initial Wood: 0__
  * __Initial Δ Temp.: 0__
  * __Initial Population: 100__
  * __LQ MAX: 100__
