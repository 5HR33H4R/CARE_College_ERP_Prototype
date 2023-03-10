$(function() {

	$('select[multiple].active.3col').multiselect({
	  columns: 3,
	  placeholder: 'Select By',
	  search: false,
	  searchOptions: {
	      'default': 'Search Options'
	  },
	  selectAll: false
	});

});