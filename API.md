# Direct Booking API

## Commit
### URL
`/commit`
### Method
`POST`
### Data Params
* user_id: ID of User
* book_date: Date of booking
* amount: Amount of booking (in ref. currency)
* flight_date: Date of booked flight
* flight_origin: Origin of booked flight
* flight_dest: Origin of booked flight
* flight_nr: Number of booked flight
### Success Response
* **Code:** `201 CREATED`
* **Content:** `{"info": "Commited booking!"}`
### Error Response
* **Code:** `400 BAD REQUEST`
* **Content:** `{"error": "Missing one or more mandatory parameters for commit service"}`
### Sample Call
```
curl -X POST \
    http://localhost:5000/commit \
    -H 'Content-Type: application/json' \
    -d '{
            "user_id": "1",
            "book_date": "201801011700",
            "amount": "400.00",
            "merchant_id": "22222",
            "flight_date": "201809011300",
            "flight_origin": "Amsterdam",
            "flight_dest": "Paris",
            "flight_nr": "123456789"
        }'
```
## Bookings
### URL
`/bookings`
### Method
`GET`
### Success Response
* **Code:** `200 OK`
* **Content:**
```
{
    "Bookings": [
        {
            "amount": 200,
            "book_date": "Mon, 01 Jan 2018 16:30:00 GMT",
            "flight_date": "Mon, 01 Jan 2018 15:40:00 GMT",
            "flight_dest": "Amsterdam",
            "flight_nr": 987654321,
            "flight_origin": "Paris",
            "id": 2,
            "merchant_id": 22222
        },
        {
            "amount": 400,
            "book_date": "Mon, 01 Jan 2018 17:00:00 GMT",
            "flight_date": "Sat, 01 Sep 2018 13:00:00 GMT",
            "flight_dest": "Paris",
            "flight_nr": 123456789,
            "flight_origin": "Amsterdam",
            "id": 3,
            "merchant_id": 22222
        }
    ]
}
```
### Sample Call
```
curl -X GET \
  http://localhost:5000/bookings \
  -H 'Content-Type: application/json' \
  -d '{
	"user_id": "1",
	"book_date": "201801011700",
	"amount": "400.00",
	"merchant_id": "22222",
	"flight_date": "201809011300",
	"flight_origin": "Amsterdam",
	"flight_dest": "Paris",
	"flight_nr": "123456789"
}'
```