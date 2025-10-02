Title: Saxon Games

This site pulls together various resources for the quasi-historical Anglo-Saxon
board games I've made.

### Overview

I've made up my own games since I was a child. Most of them were simply a way to
pass time and have long since been forgotten; some, like **Claim the Crown**,
had limited physical availability. Along the way, I began to delve into making
abstract strategy games. As a fan of Hnefatafl, I wanted to name my games using
Anglo-Saxon words as an alternative to Old Norse and to lend a quasi-historical
feel to them. All the games falling under this umbrella utilize the same 7x7
grid because, if they were historical, it might make sense for people to reuse
an existing board, much like chess and checkers. As a supporter of free culture,
my games are available
under [Creative Commons Attribution-Share Alike license](https://creativecommons.org/licenses/by-sa/4.0/)
with the software-based versions also
being [copyleft](https://en.wikipedia.org/wiki/Copyleft).

---

### Mǽrstánas

> The word *mǽrstánas* is the plural form of *mǽrstán*, an Anglo-Saxon (Old
> English) word that means "a
> boundary-stone". ([Source](https://bosworthtoller.com/22190))

#### Game Rules

- ["Living rules"](https://jaerrib.codeberg.page/maerstanas/)
- [Print-and-Play game](https://johnbeers.xyz/saxon-games/codeberg.org/jaerrib/maerstanas)

#### Play Online

- Multiplayer game platform (Python/Django
  based) - [Live Site](https://maerstanas.fly.dev/) | [Source Code](https://codeberg.org/jaerrib/maerstanas-webapp)
- 1-player or 2-player (local) (Python/Flask
  based) - [Live Site](http://maerstanas-python.fly.dev/) | [Source Code](https://codeberg.org/jaerrib/maerstanas_python)
- 1-player game (
  JavaScript-based) - [Live Site](https://jaerrib.codeberg.page/maerstanas_js/) | [Source Code](https://codeberg.org/jaerrib/maerstanas_js)

---

### Oferhlýp

> The word *oferhlýp* is an Anglo-Saxon (Old English) word meaning "A leap
> across or over, a bound". ([Source](https://bosworthtoller.com/24132))

Oferhlýp is an abstract strategy game played between two players on a 7x7 grid
where the objective is to try to eliminate the opponent's king via jumping
attacks while protecting one's own king. On the surface, gameplay is similar to
checkers (draughts). However, there are several differences:

- Tokens may move in any direction rather than just forwards diagonally
- A player's own pieces may be jumped to create a more dynamic game
- Tokens must be jumped twice before they are removed from the board
- Each player has a king token that must be captured to end the game

Oferhlýp is my oldest "Anglo-Saxon game" and was created in 2013 while working
on another game, Claim the Crown, which incorporated the concept of tokens with
two hit points, but featured various types of Middle Ages themed units, like
spearmen and archers, and replaced jump attacks with dice rolling combat.
Oferhlýp is a purer abstract interpretation of that game with a focus on
strategy over luck.

#### Game Rules

- ["Living rules"](https://jaerrib.codeberg.page/oferhlyp/)
- [Print-and-Play game](https://codeberg.org/jaerrib/oferhlyp)

#### Play Online

- 1-player or 2-player (local) (Python/Flask
  based) - [Live Site](http://oferhlyp.fly.dev/) | [Source Code](https://codeberg.org/jaerrib/oferhlyp_python)

---

### Cyngesheall

> The word cyngesheall is an Anglo-Saxon (Old English) word meaning "king's
> corner".

Cyngesheall is my newest game, being conceived in late 2024. It, too, uses a 7x7
grid. However, instead of "checkers with hit points" or making connections with
stones, Cyngesheall take more direct inspiration from Hnefatafl. Aside from the
setup, the primary differentiation is that the number of player pieces is even
instead of asymmetrical, and each player has a king, which must reach the
opposite corner rather than an edge. It currently features the same stones as
Mǽrstánas but uses them in a completely different manner.

#### Game Rules

- ["Living rules"](https://codeberg.org/jaerrib/cyngesheall)
- Print-and-play game *Coming soon!*
