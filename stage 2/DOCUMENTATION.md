# API Documentation

## Introduction

This document provides an overview of the RESTful API for managing a "person" resource. The API allows for Create, Read, Update, and Delete (CRUD) operations on person records.

## Table of Contents

1. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Running the API](#running-the-api)

2. [Endpoints](#endpoints)
   - [Create a Person](#create-a-person)
   - [Retrieve a Person](#retrieve-a-person)
   - [Update a Person](#update-a-person)
   - [Delete a Person](#delete-a-person)

3. [Request and Response Formats](#request-and-response-formats)

4. [Sample Usage](#sample-usage)
5. [UML Diagram](#uml-diagram)

6. [Testing the API](#testing-the-api)


## Getting Started

### Installation

1. Clone the project repository from GitHub:

   ```bash
   git clone https://github.com/TolulopeJoel/HNG.git
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On macOS and Linux
   myenv\Scripts\activate  # On Windows
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the API

4. Navigate to the project directory:

   ```bash
   cd stage_2
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

The API should now be running locally at `https://person.onrender.com/api/`.

## Endpoints

### Create a Person

- **URL**: `/api/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "John Doe"
  }
  ```
- **Response**:
  - Status Code: `201 Created`
  - Body:
    ```json
    {
      "id": 1,
      "name": "John Doe"
    }
    ```

### Retrieve a Person

- **URL**: `/api/<user_id>/`
- **Method**: `GET`
- **Response**:
  - Status Code: `200 OK`
  - Body:
    ```json
    {
      "id": 1,
      "name": "John Doe"
    }
    ```

### Update a Person

- **URL**: `/api/<user_id>/`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "name": "Updated Name"
  }
  ```
- **Response**:
  - Status Code: `200 OK`
  - Body:
    ```json
    {
      "id": 1,
      "name": "Updated Name"
    }
    ```

### Delete a Person

- **URL**: `/api/<user_id>/`
- **Method**: `DELETE`
- **Response**:
  - Status Code: `204 No Content`

## Request and Response Formats

- All request and response data should be in JSON format.
- For request data, ensure that fields are properly validated (e.g., string fields only).

## Sample Usage

Here are some sample API requests and responses:

### Create a Person

**Request**:

```json
POST /api/
{
  "name": "Alice Johnson",
}
```

**Response**:

```json
201 Created
{
  "id": 2,
  "name": "Alice Johnson",
}
```

### Retrieve a Person

**Request**:

```json
GET /api/2/
```

**Response**:

```json
200 OK
{
  "id": 2,
  "name": "Alice Johnson",
}
```

### Update a Person

**Request**:

```json
PUT /api/2/
{
  "name": "Updated Name",
}
```

**Response**:

```json
200 OK
{
  "id": 2,
  "name": "Updated Name",

}
```

### Delete a Person

**Request**:

```json
DELETE /api/2/
```

**Response**:

```json
204 No Content
```

#### UML Diagram

![Class Diagram](https://drive.google.com/file/d/1h76E0frnNBlmMC54sGkCAA-CeK0MRpDi/view?usp=sharing)

https://drive.google.com/file/d/1h76E0frnNBlmMC54sGkCAA-CeK0MRpDi/view?usp=sharing

This UML class diagram represents the structure and relationships of key classes and models in our API. It illustrates the 'Person' model and its associations with other classes.


## Testing the API

To test the API, you can use the provided test_api.py script located in the py_client folder. Here's how to run the tests:

1. Navigate to the py_client folder:
   ```bash
   cd stage_2
   cd py_client
   ```

2. Run the test script:

   ```bash
   python test_api.py
   ```


