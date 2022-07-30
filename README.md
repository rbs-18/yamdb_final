![workflow](https://github.com/rbs-18/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
# yamdb_final

## DESCRIPTION
Project allows to collect reviews on compositions. There is admin panel.
Admin can create compositions (from API or admin panel), genres and categories.
Users can write reviews on compositions and comment them. The project is hosted on the server 51.250.29.192

--------------------------------------------------------------------------------------

### REGISTRATION OF NEW USERS

1) `/api/v1/auth/signup/` `POST`
```json
{
  "username": "string", (required)
  "email": "user@example.com", (required)
}
```
2) YaMDB sending letter with verification code (confirmation_code) to email
3) `/api/v1/auth/token/` `POST`
```json
{
  "username": "string", (required)
  "confirmation_code": "user@example.com", (required)
}
```
4) *NOT NECESSARY*

`/api/v1/users/me/` `PATCH`
```json
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
--------------------------------------------------------------------------------------

### USERS
- #### GETTING LIST OF USERS

 `api/v1/users/` `GET`

-- *Permissions*

Administrator

-- *Parameters*

search - looking for users

-- *Responses*

200, 401

- #### ADD NEW USER

 `api/v1/users/` `POST`

```json
{
  "username": "string", (required)
  "email": "user@example.com", (required)
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"/"moderator"/"admin"
}
```
-- *Permissions*

Administrator

-- *Responses*

201, 400, 401, 403

 #### GET USER

 `api/v1/users/{username}` `GET`

-- *Permissions*

Administrator

-- *Responses*

200, 401, 403, 404

- #### CHANGE CERTAIN USER

 `api/v1/users/{username}/` `PATCH`

```json
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```

-- *Permissions*

Administrator

-- *Responses*

200, 400, 401, 403, 404

- #### DELETE USER

 `api/v1/users/{username}/` `DELETE`

-- *Permissions*

Administrator

-- *Responses*

204, 401, 403, 404

--------------------------------------------------------------------------------------

### CATEGORIES
- #### GETTING LIST OF CATEGORIES

 `api/v1/categories/` `GET`

-- *Permissions*

All

-- *Parameters*

search - looking for category

-- *Responses*

200

- #### ADD NEW CATEGORY

 `api/v1/categories/` `POST`

```json
{
  "name": "string", (required)
  "slug": "string" (required)
}
```
-- *Permissions*

Administrator


-- *Responses*

201, 400, 401, 403

- #### DELETE CATEGORY

 `api/v1/categories/{slug}/` `DELETE`

-- *Permissions*

Administrator

-- *Responses*

204, 401, 403, 404

--------------------------------------------------------------------------------------

### GENRES
- #### GETTING LIST OF GENRES

 `api/v1/genres/` `GET`

-- *Permissions*

All

-- *Parameters*

search - looking for genre

-- *Responses*

200

- #### ADD NEW GENRE

 `api/v1/genres/` `POST`

```json
{
  "name": "string", (required)
  "slug": "string" (required)
}
```
-- *Permissions*

Administrator

-- *Responses*

201, 400, 401, 403

- #### DELETE GENRE

 `api/v1/genres/{slug}/` `DELETE`

-- *Permissions*

Administrator

-- *Responses*

204, 401, 403, 404

--------------------------------------------------------------------------------------

### TITLES
- #### GETTING LIST OF TITLES

 `api/v1/titles/` `GET`

-- *Permissions*

All

-- *Parameters*

filter by category, genre, name, year

-- *Responses*

200

- #### ADD NEW TITLE

 `api/v1/titles/` `POST`

```json
{
  "name": "string", (required)
  "year": 0, (required)
  "description": "string",
  "genre": [
    "string"
  ], (required)
  "category": "string" (required)
}
```

-- *Permissions*

Administrator

-- *Responses*

201, 400, 401, 403

- #### GET INFORMATION ABOUT TITLE

 `api/v1/titles/{titles_id}/` `GET`


-- *Permissions*

All

-- *Responses*

200, 404

- #### CHANGE CERTAIN TITLE

 `api/v1/titles/{titles_id}/` `PATCH`

```json
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

-- *Permissions*

Administrator

-- *Responses*

200, 401, 403, 404

- #### DELETE TITLE

 `api/v1/titles/{titles_id}/` `DELETE`

-- *Permissions*

Administrator

-- *Responses*

204, 401, 403, 404

--------------------------------------------------------------------------------------

### REVIEWS
- #### GETTING LIST OF REVIEWS

 `api/v1/titles/{title_id}/reviews/` `GET`

-- *Permissions*

All

-- *Responses*

200, 404

- #### ADD NEW REVIEW

 `api/v1/titles/{title_id}/reviews/` `POST`

```json
{
  "text": "string", (required)
  "score": 1 (required)
}
```
-- *Permissions*

Authenticated Users

-- *Responses*

201, 400, 401, 404

- #### GET REVIEW BY ID

 `api/v1/titles/{title_id}/reviews/{review_id}/` `GET`

-- *Permissions*

All

-- *Responses*

200, 404

- #### CHANGE CERTAIN REVIEW

 `api/v1/titles/{title_id}/reviews/{review_id}/` `PATCH`

```json
{
  "text": "string",
  "score": 1
}
```

-- *Permissions*

Administrator, Moderator, Owner

-- *Responses*

200, 400, 401, 403, 404

- #### DELETE REVIEW

 `api/v1/titles/{title_id}/reviews/{review_id}/` `DELETE`

-- *Permissions*

Administrator, Moderator, Owner

-- *Responses*

204, 401, 403, 404

--------------------------------------------------------------------------------------

### COMMENTS
- #### GETTING LIST OF COMMENTS

 `api/v1/titles/{title_id}/reviews/{review_id}/comments/` `GET`

-- *Permissions*

All

-- *Responses*

200, 404

- #### ADD NEW COMMENT

 `http://localhost/api/v1/titles/{title_id}/reviews/{review_id}/comments/` `POST`

```json
{
  "text": "string" (required)
}
```
-- *Permissions*

Authenticated Users

-- *Responses*

201, 400, 401, 404

- #### GET COMMENT BY ID

 `api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/` `GET`

-- *Permissions*

All

-- *Responses*

200, 404

- #### CHANGE CERTAIN COMMENT

 `api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/` `PATCH`

```json
{
  "text": "string"
}
```

-- *Permissions*

Administrator, Moderator, Owner

-- *Responses*

200, 400, 401, 403, 404

- #### DELETE COMMENT

 `api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/` `DELETE`

-- *Permissions*

Administrator, Moderator, Owner

-- *Responses*

204, 401, 403, 404


## DOCUMENTATION AVAILIBLE AFTER LAUNCH:
- http://localhost/redoc/


## TECHNOLOGY

- Python 3.8
- Django 2.2
- Django Rest Framework 3.12
- Docker


## DATABASE

- PostgreSQL


## HOW TO START PROJECT
### IN INTERNET
Go to 51.250.29.192. It's all!

### LOCALLY (IF SERVER DOESN'T WORK)
- Clone repository and going:
```
git clone ...
cd /infra
```
- Change nginx settings (servername)
- Create .env file (like template)

SECRET_KEY=...
DEBUG=...
ALLOWED_HOSTS=...
DB_ENGINE=...
DB_NAME=...
POSTGRES_USER=...
POSTGRES_PASSWORD=...
DB_HOST=...
DB_PORT=...

- Deploy and launch app:
```bash
docker-compose up -d --build
```

- Make migrations:
```bash
docker-compose exec web python manage.py migrate
```

- Fill database by data (optionally)
```bash
docker-compose exec web python manage.py loaddata fixtures.json
```

- Create superuser
```bash
docker-compose exec web python manage.py createsuperuser
```

- Collect static
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

# AUTHORS
*_Kozhevnikov Aleksei_*
