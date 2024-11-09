from ninja import Schema

from datetime import date, datetime

from pydantic import EmailStr 

class BookingCreateSchema(Schema):
    # POST
    email: EmailStr
    date: date
    timeslot: int

class BookingListSchema(Schema):
    # GET
    id: int
    email: EmailStr
    date: date

class BookingDetailSchema(Schema):
    # GET
    id: int
    email: EmailStr
    date: date
    timeslot: int
    timestamp: datetime
