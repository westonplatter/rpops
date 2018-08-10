# RPOPs
Restful panda operations


## development
Run this,
```
FLASK_ENV=development flask run
```


## production
Run this,
```
docker pull westonplatter/rpops:latest
docker run -p 5000:5000 westonplatter/rpops:latest
```


## build
Run this,
```
docker build -t westonplatter/rpops:latest .
```
