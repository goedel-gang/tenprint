# tenprint
"10 print" in Python-processing. Inspired by [Daniel Shiffman's video](https://youtu.be/bEyTZ5ZZxZs). Rather than statically generating random positions and leaving it, each slash has a chance of mutating each frame. The starting state is an aligned grid:

![screenshot](https://github.com/elterminad0r/tenprint/blob/master/screenshots/start.png)

And as the program runs, it deforms into something more like this:

![screenshot](https://github.com/elterminad0r/tenprint/blob/master/screenshots/inprogress.png)

You can see that they don't just snap, but interpolate themselves to where they need to be. The slashes aren't often precisely aligned - this is a natural side effect of allowing them to turn in a continuum rather than flipping between binary states.

This also illustrates the mildly interesting property that this does actually approach a half/half distribution.

Lastly, [here](https://youtu.be/eZNffI1R3xM) is a video of it in action.
