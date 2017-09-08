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

<br>

### Role of the Player
There will be only one role which is the leader of humanity in our game.

<br>

### Objective
Players should choose operators sustainably to build houses, build power plants, mine coals. All operators affect living quality of the residents. The player should think carefully to keep all the variables in check. Player should strive to go through each of the hypothesized stages listed below.

* __Stage1__: Player starts with blank panel(appears to be green but without any man-build constructions), all the variables are initialized

* __Stage2__: Player starts to burn/cut down forest to gain lands that’s suitable for building supplies and also earn fundamental material(woods)

* __Stage3__: While LQ increases and the society grows larger, the society endures explicit temperature Increase, player should start considering making balance between environment protection and growth of population.

* __Stage4__: As the population grows larger, massive industrialization and deforestation is inevitable, which produce considerable amount of greenhouse gases and sharp decrease of human living quality. Meanwhile water level of the ocean starts to increase rapidly and random wildfire might cause permanent loss of forest in large areas.

* __Stage5__: Temperature of the virtual world and the CO2 level will exceed its maximum level, the world is flooded by the melted water from the glacier. The living quality of human race will reach the bottom which leads to degradation of habitats and eventually the extinction of human race  But you still have chance to win if you survive certain number of rounds.


<br>

### Player Affordance
The players can build villages, power plants, mine coals on empty spaces. Making right decisions is crucial to maintain the growth of civilization while minimizing damage to environment. Construction operators available for the user are building villages, power plants, coal mine and farms. Players should consider the operators as a double-edged sword which can develop civilization but also harm their living environment. Players will be able to see their current situation at the bottom of the game board, including the following variables, their related algorithm is listed below.

  * __Greenhouse Gas Impact on Temp:__ 5 unit raise 0.05C
  * __Temp +0.5C:__ LQ - 10
  * __Random Wildfire Starts when:__ Temp. > 0.35C
  * __3 block of sea created/3 states when:__ Temp. + 1C
  * __LQ decrease by 30/state when:__ Population > 300 and no place to live
  * __Requires 100 Food per 500 Population__
  * __Empty Space besides forest grows back to forest after three turns__

<br>

### Initial state
A virtual world consists of 10 * 10 grid is generated. Initially, the world is rich in natural resources. The game board is represented by a two-dimensional list, and each item in sub-lists represents one block on the grid. For each block, an integer is used to represent the type of the block. Initial layout of these elements in the world is fixed and is always the same in every game session.

The player receives 200 __'Gold'__ as the currency. The player should utilize this resource to develop a civilization and keep the __'LQ'__ of his/her citizens high. These values are stored in a dictionary. Other variables, such as __'GG'__, __'Wood'__, __'Food'__, and __'Δ Temp.'__, are 0 when a new game session starts.

<br>

### Operators
The first operator that a player should apply is “burn forest”. Oceans and glaciers are not places where human beings can live for a long term, so the player should want to get some spaces on lands. However, since all lands are covered by forest and plants, the player needs to burn some forest to get empty spaces.

This operator is organizational and indirect because it helps the player get ready for further development, gain more resources, and improve living quality. It is not an operator which would carry out a direct action to solve the problem.

This operator turns the block where the player chooses and its adjacent blocks into empty spaces. It leads to increase in __'GG'__: the gas is produced during tree combustion; since the amount of trees is reduced, the rate of carbon dioxide absorption of trees slows down. This also causes increase in __'Δ Temp.'__.

<br>

### Goals and Scores
There are two goal states players can achieve. The first one is that players make a perfect balance between nature and nurture. To be specific, after __n__ terns (n >= 30) __'LQ'__ must be greater than 50, and __'Δ Temp.'__ should be less than 2C the __'Population'__ should reach a number of ___P___ (The actual value of P will change according to the value of n) This is extremely hard to achieve, due to frequent deforestation and constantly increasing population. Another possible goal state is that the environment has been depleted to a state that is no longer suitable for living.

<br>

### Specification of First Working Code
Our first working code will have all the operators mentioned above.  `is_applicable()` test does not reflect the actual effect it should have since it returns _True_ in all conditions. Some of the algorithms are implemented to run in the background. Graphics is working right now, all of the operations can be reflected on the game board.

<br>

### Specification of Second Working code
By Tuesday, we will be switched from dictionary to object for the state representation.
