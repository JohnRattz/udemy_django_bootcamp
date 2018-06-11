// Method called when cell is clicked.
function changeMarker(){
	if(this.textContent==''){
		this.textContent = 'X';
	} else if (this.textContent=='X'){
		this.textContent = 'O';
	} else {
		this.textContent = '';
	}
}

// Set click listeners on table cells.
var squares = document.querySelectorAll('td');
for (square of squares){
	square.addEventListener('click', changeMarker);
}

// Metho called when restart button is clicked.
function restart(){
	for (square of squares){
		square.textContent = '';
	}
}
// Set click listener on restart button.
var restart_btn = document.querySelector('#b');
restart_btn.addEventListener('click', restart);