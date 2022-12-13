let dateEl = document.getElementById('id_date')
  M.Datepicker.init(dateEl, {
    format: 'yyyy-mm-dd',
    defaultDate: new Date(),
    setDefaultDate: true,
    autoClose: true
  })

let selectEl = document.getElementById('id_genre')
M.FormSelect.init(selectEl)