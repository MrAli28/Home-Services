from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Service, Provider, Booking, Review, ServiceArea

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'base_price')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'rating', 'total_jobs')
    list_filter = ('service_types',)
    search_fields = ('user__username', 'user__email', 'bio')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'customer', 'provider', 'date', 'time', 'status_display', 'created_at')
    list_filter = ('status', 'date', 'created_at')
    search_fields = ('customer__username', 'provider__user__username', 'service__name', 'email', 'phone_number', 'address')
    date_hierarchy = 'date'
    list_per_page = 20
    actions = ['mark_as_confirmed', 'mark_as_completed', 'mark_as_cancelled']
    
    def status_display(self, obj):
        status_classes = {
            'pending': 'status-pending',
            'confirmed': 'status-confirmed',
            'completed': 'status-completed',
            'cancelled': 'status-cancelled',
        }
        status_display = obj.get_status_display()
        status_key = obj.status.lower()
        status_class = status_classes.get(status_key, '')
        return mark_safe(f'<span class="{status_class}">{status_display}</span>')
    
    status_display.short_description = 'Status'
    
    def mark_as_confirmed(self, request, queryset):
        updated = queryset.update(status='confirmed')
        self.message_user(request, f'{updated} bookings marked as confirmed.')
    mark_as_confirmed.short_description = 'Mark selected bookings as confirmed'
    
    def mark_as_completed(self, request, queryset):
        updated = queryset.update(status='completed')
        self.message_user(request, f'{updated} bookings marked as completed.')
    mark_as_completed.short_description = 'Mark selected bookings as completed'
    
    def mark_as_cancelled(self, request, queryset):
        updated = queryset.update(status='cancelled')
        self.message_user(request, f'{updated} bookings marked as cancelled.')
    mark_as_cancelled.short_description = 'Mark selected bookings as cancelled'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('booking', 'rating', 'date')
    list_filter = ('rating', 'date')
    search_fields = ('comment', 'booking__customer__username')

@admin.register(ServiceArea)
class ServiceAreaAdmin(admin.ModelAdmin):
    list_display = ('city', 'postcodes')
    search_fields = ('city', 'postcodes')
