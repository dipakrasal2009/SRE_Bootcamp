# Student REST API

Simple REST API for managing students.

## Endpoints

- `GET /api/v1/student`
- `POST /api/v1/student`
- `GET /api/v1/student/<id>`
- `PUT /api/v1/student/<id>`
- `DELETE /api/v1/student/<id>`
- `GET /healthcheck`

## How to Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py



---

### ✅ 11. Add Logging (optional but recommended)

In `routes.py`, you can add logs like:

```python
import logging
logging.basicConfig(level=logging.INFO)

# inside route
logging.info("Student created: %s", new_student.name)

# SRE_Bootcamp
