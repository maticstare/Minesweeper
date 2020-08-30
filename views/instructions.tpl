<html>

<h1><center>INSTRUCTIONS</center></h1>

<p>
<ul>
    <li>The aim of MineSweeper is to determine the locations of 10 bombs, randomly placed in a 9x9 grid</li>
    <li>On each go, you type in the coordinates of a square, e.g. E4.</li>
    <li>If there is a bomb in that square, you lose.</li>
    <li>Otherwise, the number of bombs directly surrounding that square, including diagonally, will appear in that square.</li>
    <li>If that number is a 0, the squares around it will be 'opened' automatically, as there cannot be any bombs there, to save you time.</li>
    <li>If you think you know the position of a bomb, type 'M' followed by the coordinates of that square, e.g. ME4.</li>
    <li>You win by 'opening' all of the squares except those with bombs in.</li>
</ul>
NB: It is luck on the first move, and you may get to a stage where it is luck later in the game too.
Good luck!
</p>

<form action="/game/" method="post">
    <button type="submit">Play</button>
</form>

</html>