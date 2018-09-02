# Gecko

## Branches

### master


Setting up development Environment on Linux
----------------------------------

### Install Project (edit mode)

#### Working copy
    
    $ cd /path/to/workspace
    $ git clone git@github.com:Carrene/gecko.git
    $ cd gecko
    $ pip install -e .
 
### Setup Database

#### Configuration

```yaml

db:
  url: postgresql://postgres:postgres@localhost/gecko_dev
  test_url: postgresql://postgres:postgres@localhost/gecko_test
  administrative_url: postgresql://postgres:postgres@localhost/postgres

messaging:
  default_messenger: restfulpy.messaging.SmtpProvider

smtp:
  host: <example.com>
  port: 587
  username: <smtp-user>
  password: <smtp-password>
  local_hostname: carrene.com
   
```

#### Remove old abd create a new database **TAKE CARE ABOUT USING THAT**

    $ gecko db create --drop --mockup

And or

    $ gecko db create --drop --basedata 

#### Drop old database: **TAKE CARE ABOUT USING THAT**

    $ gecko [-c path/to/config.yml] db --drop

#### Create database

    $ gecko [-c path/to/config.yml] db --create

Or, you can add `--drop` to drop the previously created database: **TAKE CARE ABOUT USING THAT**

    $ gecko [-c path/to/config.yml] db create --drop


### Running tests

```bash
pip install -r requirements-dev.txt
pytests
```

### Running server

#### Single threaded 

```bash
gecko [-c path/to/config.yml] serve
```

#### WSGI

wsgi.py

```python
from gecko import gecko
gecko.configure(files=...)
app = gecko
```

```bash
gunicorn wsgi:app
```

### How to start

Checkout `gecko/controllers/foo.py`, 
`gecko/models/foo.py` and `gecko/tests/test_foo.py` to
learn how to create an entity.

