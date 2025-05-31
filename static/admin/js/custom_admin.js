// Home-Fix Admin Dashboard Custom JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Add loading animations
    const content = document.getElementById('content');
    if (content) {
        content.classList.add('animate__animated', 'animate__fadeIn');
    }

    // Enhance dashboard modules with entrance animations
    const modules = document.querySelectorAll('.dashboard .module');
    modules.forEach((module, index) => {
        module.style.opacity = '0';
        setTimeout(() => {
            module.style.opacity = '1';
            module.classList.add('animate__animated', 'animate__fadeInUp');
        }, 100 * index);
    });

    // Add notification counter for bookings
    addNotificationCounters();

    // Add status badges to booking status
    styleBookingStatuses();

    // Add pulse animation to recent actions
    stylizeRecentActions();

    // Add hover animations to list rows
    enhanceListRows();
});

// Add notification counters to the app list
function addNotificationCounters() {
    // This would typically fetch from an API, but we'll simulate for now
    const appList = document.querySelector('.app-services.module');
    if (appList) {
        const bookingLink = appList.querySelector('a[href*="/booking/"]');
        if (bookingLink) {
            const badge = document.createElement('span');
            badge.className = 'notification-badge';
            badge.textContent = 'New';
            badge.style.backgroundColor = '#e74c3c';
            badge.style.color = 'white';
            badge.style.padding = '2px 6px';
            badge.style.borderRadius = '10px';
            badge.style.fontSize = '10px';
            badge.style.marginLeft = '5px';
            badge.style.animation = 'pulse 2s infinite';
            bookingLink.appendChild(badge);
        }
    }
}

// Style booking statuses with color-coded badges
function styleBookingStatuses() {
    const statusCells = document.querySelectorAll('.field-status');
    statusCells.forEach(cell => {
        const statusText = cell.textContent.trim().toLowerCase();
        let className = '';
        
        if (statusText.includes('pending')) {
            className = 'status-pending';
        } else if (statusText.includes('confirmed')) {
            className = 'status-confirmed';
        } else if (statusText.includes('completed')) {
            className = 'status-completed';
        } else if (statusText.includes('cancelled')) {
            className = 'status-cancelled';
        }
        
        if (className) {
            const span = document.createElement('span');
            span.className = className;
            span.textContent = cell.textContent;
            cell.textContent = '';
            cell.appendChild(span);
        }
    });
}

// Add animations to recent actions
function stylizeRecentActions() {
    const recentActions = document.querySelector('.module.actions');
    if (recentActions) {
        const listItems = recentActions.querySelectorAll('li');
        listItems.forEach((item, index) => {
            item.style.transition = 'all 0.3s ease';
            item.style.borderLeft = '3px solid transparent';
            item.style.paddingLeft = '10px';
            item.style.animation = `fadeIn 0.5s ${index * 0.1}s both`;
            
            item.addEventListener('mouseenter', function() {
                this.style.borderLeft = '3px solid #3498db';
                this.style.backgroundColor = 'rgba(52, 152, 219, 0.05)';
            });
            
            item.addEventListener('mouseleave', function() {
                this.style.borderLeft = '3px solid transparent';
                this.style.backgroundColor = 'transparent';
            });
        });
    }
}

// Add hover effects to list rows
function enhanceListRows() {
    const listRows = document.querySelectorAll('#changelist table tbody tr');
    listRows.forEach(row => {
        row.style.transition = 'all 0.2s ease';
        
        row.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.01)';
            this.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        });
        
        row.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
            this.style.boxShadow = 'none';
        });
    });
}

// Add pulse animation style
document.head.insertAdjacentHTML('beforeend', `
<style>
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}
</style>
`);
