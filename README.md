# Kubeflow ARM64 CI/CD Proof of Concept

This repository supports the "End-to-End ARM64 Support and Validation in Kubeflow" GSoC proposal.

It demonstrates cross-compiling a glibc-based Ubuntu image using Docker Buildx and QEMU, and successfully executing `numpy` C-bindings on both `amd64` and `arm64` architectures.

To verify the manifest and ensure the multi-architecture image was pushed successfully, run the following command:

```bash
docker buildx imagetools inspect ghcr.io/<YOUR_USERNAME>/<YOUR_REPO>:latest
```
*(Make sure to replace `<YOUR_USERNAME>` and `<YOUR_REPO>` with your actual GitHub username and repository name.)*
