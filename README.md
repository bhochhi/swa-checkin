Southwest Airline Check-in
---



Local setup
---
1. run mongo
```docker run -p 27017:27017 -v /Users/bhochhi/mongoData:/data/db mongo```
2. run mongo-express
```npm install -g mongo-express```
```mongo-express -u user -p password  -d swacheckins```
3. run swa-checkin app
```gunicorn app:app``` or 
```python app.py```
