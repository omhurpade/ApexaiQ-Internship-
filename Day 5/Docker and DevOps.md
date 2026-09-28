# DevOps & Docker 

> A simple, beginner-friendly guide to understanding DevOps, CI/CD, Docker, containers, and important Docker concepts.

---

## 1. What is Development and Operations?

### Development (Dev)

Development is the part of the team that:

- Writes application code
- Builds the application
- Tests the application

### Operations (Ops)

Operations is the part of the team that:

- Deploys the application
- Monitors the application
- Maintains the application after deployment

### The old problem

Traditionally, Development and Operations worked separately.

A developer might say:

> "The code works on my machine."

Then the Operations team had to deploy it and might face different problems.

This separation could cause:

- Delays
- Miscommunication
- Deployment problems
- Blame when something failed

---

## 2. What is DevOps?

**DevOps = Development + Operations**

DevOps is a culture and set of practices that brings Development and Operations together.

The main idea is:

> Build, test, release, deploy, and operate software as a continuous process.

DevOps is **not just a collection of tools**.

It is mainly a mindset and working culture. Tools and automation help implement that culture.

---

## 3. Why Do We Need DevOps?

DevOps helps organizations:

| Benefit | Simple Explanation |
|---|---|
| Faster delivery | Software can reach users more quickly |
| Fewer errors | Automation reduces manual mistakes |
| Better collaboration | Development and Operations work together |
| Faster recovery | Problems can be detected and fixed quickly |
| Continuous improvement | Small and regular improvements can be released |

---

## 4. DevOps Lifecycle

The DevOps process is continuous.

```text
Plan
  ↓
Code
  ↓
Build
  ↓
Test
  ↓
Release
  ↓
Deploy
  ↓
Operate
  ↓
Monitor
  ↓
Feedback
  ↓
Plan again
```

There is no real final step because monitoring and feedback help us plan the next improvement.

### What happens at each stage?

| Stage | What Happens |
|---|---|
| Plan | Decide what needs to be built |
| Code | Developers write the code |
| Build | Code is converted into a runnable/package form |
| Test | Automated tests check for problems |
| Release | The tested build is prepared for deployment |
| Deploy | The application is pushed to the live environment |
| Operate | The application is maintained |
| Monitor | Performance, errors, and usage are observed |

---

# 5. CI/CD

## What is CI?

**CI = Continuous Integration**

Developers frequently merge their code changes into a shared repository.

After a change is added, automated processes can:

1. Build the code
2. Run tests
3. Detect problems early

```text
Developer
    ↓
Push Code
    ↓
Build
    ↓
Automated Tests
```

---

## What is CD?

**CD = Continuous Delivery / Continuous Deployment**

After code passes CI:

- **Continuous Delivery** prepares the software for release.
- **Continuous Deployment** can automatically push the software into the live environment.

### Simple CI/CD flow

```text
Code Push
   ↓
Automatic Build
   ↓
Automatic Testing
   ↓
Release Preparation
   ↓
Deployment
```

The main purpose is to reduce repetitive manual work and catch problems early.

---

# 6. Common DevOps Tools

| Category | Examples |
|---|---|
| Version Control | Git, GitHub, GitLab |
| CI/CD | Jenkins, GitHub Actions, GitLab CI, CircleCI |
| Containerization | Docker |
| Orchestration | Kubernetes |
| Configuration Management | Ansible, Puppet, Chef |
| Monitoring | Prometheus, Grafana, Nagios |
| Cloud | AWS, Azure, Google Cloud |

---

# 7. What is Docker?

Docker is a platform used to package an application together with everything it needs.

This includes:

- Application code
- Libraries
- Dependencies
- Configuration

The packaged application can then run inside a **container**.

### The problem Docker solves

A common problem in software development is:

> "It works on my machine."

The application may work on one computer but fail on another because the environments are different.

Docker helps create a more consistent environment.

---

# 8. What is a Container?

A **container** is a running instance created from a Docker image.

Think of it like this:

```text
Docker Image
     ↓
Container
```

### Easy example

An image is like a **blueprint**.

A container is like the **actual thing created from that blueprint**.

You can create multiple containers from the same image.

```text
          Docker Image
          /    |             /     |        Container Container Container
```

---

# 9. Docker Image vs Container

| Docker Image | Docker Container |
|---|---|
| Static template | Running/stopped instance |
| Read-only | Can have a writable container layer |
| Used to create containers | Created from an image |
| Acts like a blueprint | Acts like the actual application environment |

### Easy way to remember

```text
Image = Blueprint
Container = Instance
```

---

# 10. Why Docker?

Docker provides several useful advantages.

| Feature | Simple Explanation |
|---|---|
| Consistency | Application can run in a consistent environment |
| Lightweight | Containers share the host OS kernel |
| Isolation | Containers are separated from each other |
| Portability | Containers can be moved between environments |
| Faster setup | Environments can be created quickly |

---

# 11. Docker vs Virtual Machine

Both Docker and Virtual Machines provide isolation, but they work differently.

## Virtual Machine

```text
Physical Hardware
       ↓
   Hypervisor
       ↓
    Guest OS
       ↓
 Application
```

Every VM normally contains its own complete operating system.

## Docker Container

```text
Physical Hardware
       ↓
    Host OS
       ↓
 Docker Engine
       ↓
   Container
       ↓
 Application
```

Containers share the host operating system's kernel.

### Comparison

| Point | Virtual Machine | Docker Container |
|---|---|---|
| Virtualizes | Complete machine/OS environment | Application environment |
| OS | Each VM has its own guest OS | Containers share host kernel |
| Size | Usually larger | Usually smaller |
| Startup | Generally slower | Generally faster |
| Resource usage | Higher | Lower |
| Isolation | Strong OS-level isolation | Process-level isolation |
| Use | Different operating systems or stronger isolation needs | Fast and consistent application packaging |

---

# 12. Docker Architecture

Docker follows a **client-server model**.

The main parts are:

```text
Docker Client
      ↓
Docker Daemon
      ↓
Docker Images
      ↓
Docker Containers
```

### Docker Client

The Docker Client is what we interact with through commands such as:

```bash
docker run
docker build
docker ps
```

The client sends instructions to the Docker daemon.

### Docker Daemon

The Docker daemon is the background service called:

```text
dockerd
```

It does the actual Docker work, such as:

- Building images
- Running containers
- Managing networks
- Managing volumes

### Docker Registry

A registry stores Docker images.

A common public registry is:

```text
Docker Hub
```

### Simple flow

```text
You type command
      ↓
Docker Client
      ↓
Docker Daemon
      ↓
Pull Image if required
      ↓
Create Container
      ↓
Run Application
```

---

# 13. Docker Container Lifecycle

A container can go through different states.

```text
Create
  ↓
Start
  ↓
Running
  ↓
Stop
  ↓
Remove
```

There are also operations such as pause, unpause, kill, and restart.

### Important commands

| Action | Command |
|---|---|
| Create | `docker create image_name` |
| Run | `docker run image_name` |
| Start | `docker start container_name` |
| Pause | `docker pause container_name` |
| Continue | `docker unpause container_name` |
| Stop | `docker stop container_name` |
| Force stop | `docker kill container_name` |
| Restart | `docker restart container_name` |
| Remove | `docker rm container_name` |

---

# 14. Checking Containers

### Show running containers

```bash
docker ps
```

### Show all containers

```bash
docker ps -a
```

### Important point

A container normally needs to be stopped before removing it.

```bash
docker rm container_name
```

For a running container, removal can be forced with:

```bash
docker rm -f container_name
```

---

# 15. Docker Desktop

Docker Desktop is an application that helps run and manage Docker on a local computer.

It provides:

- Docker Engine
- Docker CLI
- Docker Compose
- Visual management tools

It is commonly used on:

- Windows
- macOS
- Linux

---

# 16. Docker Hub

Docker Hub is an online registry where Docker images can be:

- Found
- Stored
- Shared

Examples of commonly available images include:

```text
nginx
python
mysql
```

---

# 17. Docker Scout

Docker Scout is used to scan Docker images for security vulnerabilities.

It can:

- Check image layers
- Identify known vulnerabilities
- Provide recommendations
- Help identify safer or updated packages/base images

---

# 18. Docker Build Cloud

Docker Build Cloud allows Docker image builds to run using cloud infrastructure instead of relying only on the local computer.

This can be useful for:

- Large projects
- Team environments
- Faster builds
- Powerful shared build infrastructure

---

# 19. Docker Debug

Docker Debug can help debug running containers, including minimal containers that do not contain a normal shell or debugging tools.

It can provide temporary debugging utilities without modifying the original image.

---

# 20. Dockerfile

A **Dockerfile** contains instructions used to build a Docker image.

Example:

```dockerfile
FROM ubuntu:22.04

COPY app.py /app/app.py

RUN pip install flask
```

### Common Dockerfile instructions

| Instruction | Purpose |
|---|---|
| `FROM` | Selects the base image |
| `COPY` | Copies files into the image |
| `RUN` | Executes commands while building the image |

### `FROM`

Example:

```dockerfile
FROM ubuntu:22.04
```

It defines the base image.

### `COPY`

Example:

```dockerfile
COPY app.py /app/app.py
```

It copies a file from the local build context into the image.

### `RUN`

Example:

```dockerfile
RUN pip install flask
```

It executes a command during image building.

---

# 21. Removing Docker Objects

### Remove a container

```bash
docker rm my_container
```

### Remove an image

```bash
docker rmi my_image
```

Remember:

```text
rm   → container
rmi  → image
```

---

# 22. Docker Volumes

Containers have their own filesystem, but data stored only inside a container may not survive after the container is removed.

A **Docker volume** provides persistent storage outside the container's own filesystem.

### Why use volumes?

Suppose we run a database inside a container.

If the container is deleted, we don't want the database data to disappear.

A volume can keep that data.

```text
Container
    ↓
Volume
    ↓
Persistent Data
```

---

# 23. Types of Docker Mounts

### Named Volume

Created and managed by Docker.

Example:

```bash
docker volume create mydata
```

### Bind Mount

Maps a specific folder from the host machine into the container.

This is useful during development.

### tmpfs Mount

Stores data in the host's memory rather than on disk.

It can be useful for temporary data.

---

# 24. Volume Example

For a MySQL container:

```bash
docker run -v mydata:/var/lib/mysql mysql
```

Here:

```text
mydata
   ↓
Docker volume

/var/lib/mysql
   ↓
Location inside the container
```

The database data can survive even if the container is removed and recreated.

---

# 25. Detached Mode

Normally, when a container runs in the foreground, its output is connected to your terminal.

To run it in the background, use:

```bash
docker run -d nginx
```

The `-d` option means:

```text
Detached Mode
```

### Why use detached mode?

It allows the container to continue running while you use the same terminal for other commands.

This is useful for long-running applications such as web servers.

---

# 26. Working with Detached Containers

### Check running containers

```bash
docker ps
```

### View logs

```bash
docker logs container_name
```

### Attach to a running container

```bash
docker attach container_name
```

---

# 27. Hyper-V and Docker on Windows

Hyper-V is a Windows virtualization technology.

Docker Desktop on Windows can use a lightweight Linux environment underneath because Docker containers are fundamentally based on Linux kernel features.

### Common backends

```text
Hyper-V
WSL2
```

WSL2 is a newer and generally lighter option and is commonly used by modern Docker Desktop installations.

### On native Linux

Docker can run directly using the Linux kernel, so a separate Windows-style virtualization layer is not required.

---

# 28. Docker Compose

Docker Compose is used when an application needs **multiple containers**.

For example, a web application might contain:

```text
Web Application
      +
Database
      +
Redis Cache
```

Instead of running many separate commands, we can define the services in one configuration file.

The common file is:

```text
docker-compose.yml
```

It is written in YAML.

---

# 29. Basic Docker Compose Commands

### Start services

```bash
docker compose up
```

### Stop and remove services

```bash
docker compose down
```

### Check services

```bash
docker compose ps
```

### View logs

```bash
docker compose logs
```

---

# 30. DevSecOps

**DevSecOps = Development + Security + Operations**

DevSecOps extends DevOps by including security throughout the development and deployment process.

The main idea is:

> Shift security left.

This means finding security problems early instead of waiting until the application is already deployed.

### Security at different stages

| Stage | Security Focus |
|---|---|
| Development | Secure coding, dependency scanning, static analysis |
| Build/Test | Container and dependency vulnerability scanning |
| Deployment/Production | Runtime monitoring, access control, patching |

---

# 31. Complete DevOps Process

A typical DevOps process can be understood like this:

```text
Plan
 ↓
Develop
 ↓
Build
 ↓
Test
 ↓
Release
 ↓
Deploy
 ↓
Monitor
 ↓
Feedback
 ↓
Plan Again
```

Security can be included throughout the complete process.

```text
        SECURITY
           ↓
Plan → Code → Build → Test → Release → Deploy → Monitor
           ↑
        Feedback
```

---

# 32. Important Docker Commands

| Command | Purpose |
|---|---|
| `docker run` | Create and run a container |
| `docker create` | Create a container without starting it |
| `docker start` | Start a stopped container |
| `docker stop` | Stop a running container |
| `docker restart` | Restart a container |
| `docker pause` | Pause a container |
| `docker unpause` | Resume a paused container |
| `docker kill` | Forcefully stop a container |
| `docker rm` | Remove a container |
| `docker ps` | Show running containers |
| `docker ps -a` | Show all containers |
| `docker images` | Show local images |
| `docker rmi` | Remove an image |
| `docker logs` | View container logs |
| `docker attach` | Attach to a running container |
| `docker volume create` | Create a volume |
| `docker compose up` | Start Compose services |
| `docker compose down` | Stop and remove Compose services |

---

# 33. Easy Docker Mental Model

Remember Docker using this simple model:

```text
Dockerfile
    ↓
Build
    ↓
Docker Image
    ↓
Run
    ↓
Docker Container
    ↓
Application
```

For persistent data:

```text
Container
    ↓
Volume
    ↓
Persistent Data
```

For multiple containers:

```text
Docker Compose
      ↓
 ┌────┼────┐
 ↓    ↓    ↓
App  DB   Redis
```

---

# 34. DevOps vs Docker

Do not confuse DevOps and Docker.

| DevOps | Docker |
|---|---|
| Culture and practices | Container platform |
| Combines Development and Operations | Packages and runs applications |
| Covers the complete software lifecycle | Focuses mainly on containerization |
| Includes CI/CD, monitoring, collaboration, etc. | Provides images, containers, volumes, Compose, etc. |

### Easy example

```text
DevOps = Way of working

Docker = Tool/platform used in that workflow
```

---

# 35. Final Revision

### DevOps

```text
Development + Operations
```

### CI

```text
Frequently integrate code
        ↓
Build
        ↓
Test
```

### CD

```text
Tested code
     ↓
Release
     ↓
Deployment
```

### Docker

```text
Application + Dependencies
          ↓
       Image
          ↓
      Container
```

### Dockerfile

```text
Instructions
     ↓
Build
     ↓
Image
```

### Volume

```text
Container
    ↓
Persistent Storage
```

### Compose

```text
One configuration
      ↓
Multiple containers
```

### DevSecOps

```text
DevOps + Security
```

---

# 36. Day 3 Practice

Try to explain these questions in your own words:

1. What is DevOps?
2. Why is DevOps needed?
3. What is the DevOps lifecycle?
4. What is CI?
5. What is CD?
6. What is Docker?
7. What is a Docker image?
8. What is a Docker container?
9. What is the difference between an image and a container?
10. Docker vs Virtual Machine — what is the difference?
11. What is a Dockerfile?
12. What is a Docker volume?
13. What is detached mode?
14. What is Docker Compose?
15. What is DevSecOps?

---

# 37. Final Takeaway

The easiest way to understand the complete topic is:

```text
DEVOPS
  ↓
Plan → Code → Build → Test → Release → Deploy → Monitor
  ↓
Continuous Feedback

DOCKER
  ↓
Dockerfile
  ↓
Image
  ↓
Container
  ↓
Application

PERSISTENT DATA
  ↓
Volume

MULTIPLE CONTAINERS
  ↓
Docker Compose

SECURITY
  ↓
DevSecOps
```

> **DevOps is a way of working, while Docker is a technology used to package and run applications consistently.**

## 🎯 Day 3 Goal

By the end of this lesson, you should be able to:

- Explain DevOps in simple words
- Explain the DevOps lifecycle
- Understand CI/CD
- Identify common DevOps tools
- Explain Docker
- Explain images and containers
- Understand Docker architecture
- Understand the container lifecycle
- Write basic Docker commands
- Understand Dockerfiles
- Understand volumes
- Understand detached mode
- Understand Docker Compose
- Understand Hyper-V/WSL2 in the Docker context
- Explain DevSecOps

> **Don't just memorize Docker commands. Understand what is happening behind each command.**

