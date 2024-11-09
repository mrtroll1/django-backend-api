from typing import List

from ninja import Router

from django.shortcuts import get_object_or_404

from .models import Booking
from .schemas import BookingListSchema, BookingDetailSchema

router = Router()

@router.get('', response=List[BookingListSchema])
def bookings_list(request):
    return Booking.objects.all()

@router.get('{entry_id}/', response=List[BookingDetailSchema])
def booking_detail(request, entry_id:int):
    qs = [get_object_or_404(Booking, id=entry_id)]
    return qs