# embeddings
Simple API example fo embeddings of sentence or documents

## setup
- build docker image
```
docker build . -t embedding-api:latest
```

- start docker container with port fowarding: 8080
```
docker run --rm -it -p 8080:8080 embedding_api:latest 
```

- kick embed api
```
curl -X POST -H "Content-Type: application/json" http://localhost:8080/embed -d '{"sentence": "ひょっとして隣の客はよく柿食う客なのかも知れません。"}'
```
