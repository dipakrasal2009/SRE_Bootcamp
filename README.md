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

# Student API (Flask)

## 🐳 Docker

Build Docker Image:

```bash
make build

Run the container with environment variables:
```
make run
```
Tag and push:
```
make tag-latest
make push
```
🧪 Healthcheck
```
curl http://localhost:5000/healthcheck
```

🧬 Image Info
Multi-stage build

Small image size (~40MB)

Tags: student-api:v1.0.0 (no latest tag)


—

✅ Summary

You now have:

- ✅ Multi-stage Dockerfile
- ✅ Minimal image size
- ✅ Environment variable support
- ✅ SemVer tagging
- ✅ Automated Makefile
- ✅ Clean README instructions

Let me know if you want to Docker Compose this or deploy to AWS/GCP next.

