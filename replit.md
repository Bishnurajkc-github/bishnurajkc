# Portfolio Website - Bishnu Raj KC

## Overview
A personal portfolio website built with Python Flask, showcasing learning projects including a calculator and blog.

## Project Architecture
- **Framework**: Python Flask
- **Server**: Gunicorn (production), Flask dev server (development)
- **Port**: 5000
- **Structure**:
  - `app.py` - Main Flask application with routes
  - `templates/` - Jinja2 HTML templates (index, calculator, blog, weather, vo2max, note)
  - `static/` - Static assets (CSS, JS, images) organized by feature

## Routes
- `/` - Home/portfolio page
- `/calculator` - Calculator page
- `/blog` - Blog page

## Running
- Development: `python app.py` (runs on 0.0.0.0:5000)
- Production: `gunicorn --bind=0.0.0.0:5000 --reuse-port app:app`
