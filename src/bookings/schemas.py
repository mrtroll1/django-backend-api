from ninja import Schema

from datetime import date, datetime

class BookingCreateSchema(Schema):
    # POST
    email: str
    date: date
    timeslot: int

class BookingDetailSchema(Schema):
    # GET
    email: str
    date: date
    timeslot: int
    timestamp: datetime
