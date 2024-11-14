# http-parrot

A minimal Flask app useful as a test service in containerized workflows

## Usage

### With Docker CLI

```sh
docker run -e SAY="Polly want a cracker?" -e PORT=8081 -p 8081:8081 -d sahilng/http-parrot
```

```sh
curl localhost:8081
```

### In a Docker Compose File

```yaml
http-parrot:
    image: sahilng/http-parrot:latest
    environment:
      SAY: "Polly want a cracker?"
      PORT: 8081
    ports:
        - "8081:8081"
```

```sh
curl localhost:8081
```
