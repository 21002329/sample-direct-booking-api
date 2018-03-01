# Direct Booking API
----
* ##URL
    /commit
    **Method:**
    `POST`
    **Data Params**
    user_id: ID of User
    book_date: Date of booking
    amount: Amount of booking (in ref. currency)
    flight_date: Date of booked flight
    flight_origin: Origin of booked flight
    flight_dest: Origin of booked flight
    flight_nr: Number of booked flight
    **Success Response**
    * **Code:** `201 CREATED`
    * **Content:** `{"info": "Commited booking!"}`
    **Error Response**
    * **Code:** `400 BAD REQUEST`
    * **Content:** `{"error": "Missing one or more mandatory parameters for commit service"}`
    **Sample Call**
    ```
    curl -X POST \
        http://localhost:5000/commit \
        -H 'Cache-Control: no-cache' \
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