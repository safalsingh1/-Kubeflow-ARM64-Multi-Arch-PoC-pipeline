# Kubeflow ARM64 CI/CD Proof of Concept

This repository supports the **"End-to-End ARM64 Support and Validation in Kubeflow"** GSoC 2026 proposal.

## Overview
It demonstrates cross-compiling a glibc-based Ubuntu image using Docker Buildx and QEMU, and successfully executing `numpy` C-bindings on both `amd64` and `arm64` architectures. This workflow directly addresses the `libc` ABI mismatches commonly encountered when deploying ML workloads on ARM64 nodes.

## Verification

**1. Inspect the Manifest**
To verify the multi-architecture image was built and pushed successfully, check the OCI index:
```bash
docker buildx imagetools inspect ghcr.io/safalsingh1/-kubeflow-arm64-multi-arch-poc-pipeline:latest
