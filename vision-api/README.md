# Logo Creation FastAPI
FastAPI for creation of the logo in the backend


## Features:

- FastAPI project structure tree
- user module
  - id, first name, last name, **email** as username, **password**, role, is_active created_at, updated_at
- admin dashboard => sqladmin
- authentication => JWT
- db migration => alembic
- CORS middleware

## Structured Tree (current)

```sh
├── alembic     # Manages database migrations
├── alembic.ini
├── app
│   ├── api
│   │   ├── endpoints   # Contains modules for each feature (user, product, payments).
│   │   │   ├── __init__.py
│   │   │   └── user
│   │   │       ├── auth.py
│   │   │       ├── functions.py
│   │   │       ├── __init__.py
│   │   │       └── user.py
│   │   ├── __init__.py
│   │   └── routers     # Contains FastAPI routers, where each router corresponds to a feature.
│   │       ├── main_router.py
│   │       ├── __init__.py
│   │       └── user.py
│   ├── core    # Contains core functionality like database management, dependencies, etc.
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── __init__.py
│   ├── main.py     # Initializes the FastAPI app and brings together various components.
│   ├── models      # Contains modules defining database models for users, products, payments, etc.
│   │   ├── admin.py
│   │   ├── common.py
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas   # Pydantic model for data validation
│   │   ├── __init__.py
│   │   └── user.py
│   └── utils       # Can include utility functions that are used across different features.
├── requirements.txt # Lists project dependencies.
```

**app/api/endpoints/**: Contains modules for each feature (user, product, payments).

**app/api/routers/**: Contains FastAPI routers, where each router corresponds to a feature.

**app/models/**: Contains modules defining database models for users, products, payments, etc.

**app/core/**: Contains core functionality like database management, dependencies, etc.

**app/utils/**: Can include utility functions that are used across different features.

**app/main.py**: Initializes the FastAPI app and brings together various components.

**tests/**: Houses your test cases.

**alembic/**: Manages database migrations.

**docs/**: Holds documentation files.

**scripts/**: Contains utility scripts.

**requirements.txt**: Lists project dependencies.

# Setup

The first thing to do is to clone the repository:

```sh
$ https://github.com/mohith2017/logo-extraction
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ cd fastapi-starter-boilerplate
$ python -m venv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
# for fixed version
(venv)$ pip install -r requirements.txt

# or for updated version
(venv)$ pip install -r dev.txt
```

Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:

```sh
# db migrations
(venv)$ alembic upgrade head

# start the server
(venv)$ fastapi dev app/main.py # using fastapi CLI ==> after version 0.100.0
or
(venv)$ uvicorn app.main:app --reload # using directly uvicorn ==> old one => before version 0.100.0
```

# API Schema

1. Fetch Logo Links
### Fetch Logo Links Endpoint

**Endpoint:** `/logo/fetch`
**Method:** `POST`
**Description:** This endpoint accepts a list of URLs and returns the corresponding logo links for each URL.

**Request Body:**

* **Content-Type:** `application/json`
* **Body:**
```json
{
  "urls": ["url1", "url2", ...]
}
```
**Response:**

* **Status Code:** `200 OK`
* **Content-Type:** `application/json`
* **Body:**
```json
{
  "logos": [
    {
      "url": "url1",
      "logo_link": "logo_link1"
    },
    {
      "url": "url2",
      "logo_link": "logo_link2"
    },
    ...
  ]
}
```

2. OpenAI Vision
### OpenAI Vision Endpoint

**Endpoint:** `/openai/vision`
**Method:** `POST`
**Description:** This endpoint accepts an image URL and returns the extracted text from the image using OpenAI's vision capabilities.

**Request Body:**

* **Content-Type:** `application/json`
* **Body:**
```json
{
  "image_url": "image_url_here"
}
```
**Response:**

* **Status Code:** `200 OK`
* **Content-Type:** `application/json`
* **Body:**
```json
{
  "extracted_text": "extracted_text_here"
}
```

3. Claude Vision
### Claude Vision Endpoint

**Endpoint:** `/claude/vision`
**Method:** `POST`
**Description:** This endpoint accepts an image URL and returns the extracted text from the image using Claude's vision capabilities.

**Request Body:**

* **Content-Type:** `application/json`
* **Body:**
```json
{
  "image": "image uploaded here"
}
```
**Response:**

* **Status Code:** `200 OK`
* **Content-Type:** `application/json`
* **Body:**
```json
{
  "extracted_text": "extracted_text_here"
}
```
### Additional Endpoints

(Add descriptions for any other endpoints you may have in your application, following the same format.)

### Example Usage

To use the `/fetch` endpoint, send a `POST` request with the appropriate JSON body as described above. The server will respond with the logo links for the provided URLs.


# Tools

### Back-end

#### Language:

    Python

#### Frameworks:

    FastAPI
    pydantic

#### Other libraries / tools:

    SQLAlchemy
    starlette
    uvicorn
    python-jose
    alembic
