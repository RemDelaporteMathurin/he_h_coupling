# he_h_coupling

1. Run a FEniCS docker container

```
docker run -ti -v $(pwd):/home/fenics/shared quay.io/fenicsproject/stable:latest
```

2. Install FESTIM dev at commit 5d9aed7ff3d9a0e6a83402ad586a179e28680b06

```
pip install git+https://github.com/RemDelaporteMathurin/FESTIM@5d9aed7ff3d9a0e6a83402ad586a179e28680b06
```