# ⚙️ Basic Docker Commands

## 🔍 Docker Info

```bash
docker --version
docker info
```

## 🐳 Image Commands

```bash
docker images              # List images
docker pull ubuntu         # Download an image
docker rmi image_id        # Remove image
```

## 🚀 Container Commands

```bash
docker ps -a               # List containers
docker run -it ubuntu      # Run interactively
docker exec -it <id> bash  # Enter running container
docker stop <id>           # Stop container
docker rm <id>             # Remove container
```

## 🧹 Clean-up

```bash
docker system prune
docker volume prune
```

These are the most essential commands to navigate Docker as a data engineer.
