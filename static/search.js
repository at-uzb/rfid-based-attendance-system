const socket = new WebSocket('ws://localhost:8000/ws/student_search/');

socket.onopen = function () {
  console.log('WebSocket connection established.');
};

socket.onmessage = function (event) {
  const searchResults = JSON.parse(event.data);
  // Update the frontend with the search results
  // e.g., populate a table or list with the search results
};

function performSearch() {
  const query = document.getElementById('search-input').value;
  socket.send(query);
}
