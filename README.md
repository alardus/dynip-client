# dynip-client

In `client.py` change content of two strings:
- `client_token = ''` - paste token from `Settings` section
- `subdomain = ''` - enter `hostname` that you want to update

Run `client.py` itself or use `Dockerfile` to build a docker container:

```
docker build -t dynip .
```
```
docker run -d --name dynip-client dynip
```
