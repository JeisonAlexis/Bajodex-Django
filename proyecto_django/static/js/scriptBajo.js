document.addEventListener('DOMContentLoaded', function () {
  const regionSpans = document.querySelectorAll('.regionvalue');
  const cards = document.querySelectorAll('.cardContainer');
  const header = document.querySelector('.header');
  const searchInput = document.getElementById('searchbar');
  const tipos = ["Aire", "Tierra", "Fuego", "Energia", "Agua"];

  let selectedRegion = 'Todos';

  const urlParams = new URLSearchParams(window.location.search);
  const elementoFromUrl = urlParams.get('elemento');
  const searchFromUrl = urlParams.get('search');

  if (elementoFromUrl) {
    selectedRegion = elementoFromUrl;
  }

  if (searchFromUrl) {
    searchInput.value = searchFromUrl;
  }


  regionSpans.forEach(span => {
    if (span.dataset.value === selectedRegion) {
      span.classList.add('selected');
    } else {
      span.classList.remove('selected');
    }
  });


  updateHeaderColor();


  regionSpans.forEach(span => {
    span.addEventListener('click', () => {
      regionSpans.forEach(s => s.classList.remove('selected'));
      span.classList.add('selected');

      selectedRegion = span.dataset.value;

      const params = new URLSearchParams(window.location.search);


      if (selectedRegion !== 'Todos') {
        params.set('elemento', selectedRegion);
      } else {
        params.delete('elemento');
      }

      const currentSearch = searchInput.value.trim();
      if (currentSearch) {
        params.set('search', currentSearch);
      } else {
        params.delete('search');
      }

      params.delete('page'); 

      window.location.href = `${window.location.pathname}?${params.toString()}`;
    });
  });


  searchInput.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
      const inputValue = searchInput.value.trim();
      const params = new URLSearchParams(window.location.search);


      if (inputValue !== '') {
        params.set('search', inputValue);
      } else {
        params.delete('search');
      }


      if (selectedRegion !== 'Todos') {
        params.set('elemento', selectedRegion);
      } else {
        params.delete('elemento');
      }

      params.delete('page'); 

      window.location.href = `${window.location.pathname}?${params.toString()}`;
    }
  });


  function updateHeaderColor() {
    tipos.forEach(tipo => header.classList.remove(tipo));
    header.classList.remove('todos-color');

    if (selectedRegion === 'Todos') {
      header.classList.add('todos-color');
    } else if (tipos.includes(selectedRegion)) {
      header.classList.add(selectedRegion);
    }
  }
});
