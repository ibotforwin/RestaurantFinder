# RestaurantFinder

The project contains a front-end and a back-end.

The back-end is a RESTful API, while the front-end is a simple representation of some of the data.

## localhost/api/restaurants end point:

Example: This end point contains location data as well as a rating.

[
    {
        "id": 1,
        "name": "TRes",
        "latitude": 11.0,
        "longitude": 52.0,
        "rating": 4.5
    },
    {
        "id": 2,
        "name": "Boolean Pizza",
        "latitude": 65.0,
        "longitude": 49.0,
        "rating": 3.9
    },

]

## localhost/api/userdata end point:

Example: This end point contains users rating as well as blacklist preferences.

[
    {
        "id": 1,
        "user": 1,
        "restaurant": 1,
        "blacklisted": true,
        "favorite": false
    },
    {
        "id": 2,
        "user": 1,
        "restaurant": 2,
        "blacklisted": true,
        "favorite": false
    }
]




