// ---- un-authenticated users drawer alert ---- //
function handleMenuClick(element, isDisabled) {
    if (isDisabled === 'true') {
        var loginModal = new bootstrap.Modal(document.getElementById('loginRequiredModal'));
        loginModal.show();
        return false; 
    }
    return true; 
}

// --- project deletetion modal --- //
document.addEventListener('DOMContentLoaded', function() {
    const deleteModal = document.getElementById('deleteModal');
    
    deleteModal.addEventListener('show.bs.modal', function(event) {
        const button = event.relatedTarget;
        const projectId = button.getAttribute('data-project-id');
        const projectName = button.getAttribute('data-project-name');
        
        document.getElementById('projectName').textContent = projectName;
        
        document.getElementById('deleteForm').action = `/projek/${projectId}/delete/`;
    });
});

// --- Charts --- //
function createBarChart(elementId, {labels, data, label, bgColors, borderColors}) {
    const element = document.getElementById(elementId);
    if (!element) return null;

    return new Chart(element.getContext('2d'), {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: label,
                data: data,
                backgroundColor: bgColors,
                borderColor: borderColors,
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}

