# Ride_Share
The Ride Sharing API is a Django Rest Framework-based backend for a ride-sharing platform. It offers user registration, ride requests, status updates, and real-time tracking. Features include ride matching, driver acceptance, and robust testing for models and endpoints, ensuring scalability and efficiency


Overview of the Task

This is an application development task, with specific requirements broken down into several components. Here's a detailed breakdown:
1. User API

Purpose:
To allow users to register and log in.

Requirements:

    Implement endpoints for:
        User Registration: Users can sign up by providing required details (e.g., name, email, password).
        User Login: Users can log in using their credentials and receive an authentication token (e.g., JWT or DRF Token).

Key Points to Implement:

    Use DRF's built-in authentication system or libraries like djangorestframework-simplejwt for token-based authentication.
    Serialize the user model and handle registration and login functionality using class-based views (CBVs) or viewsets.

2. Ride API

Purpose:
To manage ride requests and ride details.

Requirements:

    Django Model for Rides:
    Define a Ride model with fields:
        rider: A foreign key to the User model (who requested the ride).
        driver: A foreign key to the User model (who accepted the ride).
        pickup_location: A string or a geographical point for where the ride starts.
        dropoff_location: A string or geographical point for where the ride ends.
        status: A choice field (e.g., Pending, In Progress, Completed, Cancelled).
        created_at, updated_at: Timestamps for when the ride was created or modified.

    Endpoints:
        Create a Ride Request: Allow users to request a ride.
        View Ride Details: View details of a specific ride (e.g., rider, driver, locations, status).
        List All Rides: Retrieve a list of all rides.

Key Points to Implement:

    Use viewsets for CRUD operations.
    Implement permissions (e.g., riders can only view rides they requested, and drivers can view rides they’ve accepted).

3. Ride Status Updates

Purpose:
Allow status transitions (e.g., ride started, completed, cancelled).

Requirements:

    Create an endpoint to update the status of a ride.
    Define allowed status transitions, for example:
        Pending → In Progress
        In Progress → Completed or Cancelled.

Key Points to Implement:

    Use a PATCH method in the API.
    Validate the state transition logic.

4. Real-time Ride Tracking (Bonus for Juniors)

Purpose:
To simulate real-time tracking of a ride's current location.

Requirements:

    Add a field in the Ride model for current location (e.g., current_location).
    Periodically update the current location using a background task or dummy simulation logic.

Key Points to Implement:

    Use a library like Celery for periodic location updates.
    Expose an API endpoint to fetch the current location.

5. Ride Matching (Bonus for Juniors)

Purpose:
Match ride requests with available drivers based on certain criteria.

Requirements:

    Implement a simple algorithm (e.g., proximity-based) to assign drivers to rides.
    Create an endpoint for drivers to:
        View available ride requests.
        Accept a ride request.

Key Points to Implement:

    Use a custom logic to match riders and drivers.
    Use Django signals or notifications to inform the rider when a driver accepts the ride.

6. Tests

Purpose:
Ensure the application is robust and reliable.
Basic Tests:

    Write tests for:
        Models (e.g., checking field validations).
        API endpoints (e.g., registration, login, ride creation, status updates).

Advanced Tests (Bonus for Seniors):

    Write tests for:
        Ride matching algorithm.
        Status updates and validation logic.
        Driver API endpoints.
        Real-time ride tracking simulation.

Tools and Technologies

    Framework: Django and Django Rest Framework.
    Authentication: JWT or DRF's token authentication.
    Database: SQLite (for simplicity) or Postgres/MySQL (for production readiness).
    Testing: Django's built-in test framework.
    Task Scheduling (for real-time tracking): Celery with Redis as the message broker.

Expected Deliverables

    A Django project with:
        User API endpoints for registration and login.
        Ride API endpoints for ride requests, viewing details, listing rides, and updating ride statuses.
        Simulation of real-time ride tracking (bonus).
        Ride-matching logic and driver endpoints (bonus).
    A test suite covering models and API endpoints.