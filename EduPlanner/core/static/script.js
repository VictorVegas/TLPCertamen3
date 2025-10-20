document.addEventListener('DOMContentLoaded', function () {
    let calendarEl = document.getElementById('calendar'); // Div donde se renderiza el calendario

    let calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth', // Vista inicial (mes)
        headerToolbar: {
            left: 'prev,next today', // Controles para cambiar entre meses
            center: 'title',        // Título del calendario
            right: 'dayGridMonth,timeGridWeek,timeGridDay' // Vistas disponibles
        },
        events: '/eventos/', // URL para obtener los eventos desde Django
        eventClick: function(info) {
            // Muestra un alerta con la descripción al hacer clic en un evento
            alert('Evento: ' + info.event.title + '\nDescripción: ' + info.event.extendedProps.description);
        }
    });

    calendar.render(); // Renderiza el calendario
});

