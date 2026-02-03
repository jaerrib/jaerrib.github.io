Title: Making an App
Category: Blog
Tags: coding,  
Date: 2026-02-02
Modified: 2026-02-03
Author: John Beers
Summary: What I built between projects

In the last year, I've made a variety of games with Godot. They've ranged from things I built by following a tutorial to full-fledged inventions of my own. My ambition, however, is still greater. I have grand ideas for things that I'm not even sure I can build (yet), and to be honest, sometimes it impacts my motivation. So, I got the idea to build something else. Something different, smaller in scope, and most importantly, fun.

While Godot is a game engine, there are multiple examples of building apps with it, such as Pixelorama. I like the idea that I can build something once and be able to export it for multiple platforms, including HTML5 for web embeds.

Many people who play solo TTRPGs (tabletop role playing games) have books, paper, and dice: basically everything as non-electronic as possible. Others use PDF sourcebooks and keep notes using some sort of app. I got the idea to make a dice-rolling application for that latter group.

But wait! Some people might use an old repurposed laptop as a dedicated machine for such a thing, and games/apps made with Godot 4.x don't always run on those older devices. So, despite learning Godot staring with version 4.3, I decided to step backwards and build something with Godot 3.6.2! Not only was this a good learning exercise, it was also a lesson in appreciating all the improvements that have been made in recent releases. 

Enter RNGremlin!

![A screenshot of the RNGremlin UI with the Rust Gold theme]({static}/images/screenshot01.png)

RNGremlin has the following features:

- Generates up to five results simultaneously
- Select various die types (d4, d6, d8, d10, d12, d20 or d100) or leave a particular position off
- Select from various light and dark themes in a pixel art style because why not
- Auto save/load so that you can resume your session exactly as you left off
- UI sound effects, which can be toggled on/off
- Visual roll history, which can be cleared at any point
- Keyboard shortcuts if you don't / can't use a mouse

So what did I accomplish by doing this? I learned how Godot has evolved between the two versions, including signal handling and node types. I reinforced the idea of outlining a project, keeping the scope small, and building to the requirements. (Although, admittedly, I expanded on the original plan by adding auto saving and loading the workspace with some inspiration from native elementary OS apps.) In the end, I made a cool thing that I can run on the Thinkpad T510 I acquired from my dad, and am able to share it with other people who may find value in it as well.

The project file is available on [Codeberg](https://codeberg.org/jaerrib/RNGremlin). Binaries are available for Linux and Windows (64-bit only), and I plan on putting it up on itch.io very soon.

<iframe frameborder="0" src="https://itch.io/embed/4255184?bg_color=202020&amp;fg_color=f6cd26&amp;link_color=ac6b26&amp;border_color=5f4843" width="552" height="167"><a href="https://jaerrib.itch.io/rngremlin">RNGremlin by jaerrib</a></iframe>