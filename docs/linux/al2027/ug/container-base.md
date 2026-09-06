---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/container-base.html
---

# Using the AL2027 base container image
<a name="container-base"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

The AL2027 base container image provides an AL2027 environment for local development and containerized workloads. You can use the image directly or as the base for your own container images.

The base container image is available in the [Amazon ECR Public Gallery](https://gallery.ecr.aws/amazonlinux/amazonlinux). Public repositories support unauthenticated pulls. You can optionally authenticate your Docker client before pulling the image.

## Authenticate to Amazon ECR Public (optional)
<a name="container-base-authenticate"></a>

Run the following command to authenticate Docker to Amazon ECR Public. Always use the `us-east-1` Region when you retrieve an Amazon ECR Public authentication token. The token is valid for 12 hours.

```
$ aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
```

For more information, see [Registry authentication in Amazon ECR Public](https://docs.aws.amazon.com/AmazonECR/latest/public/public-registry-auth.html) in the *Amazon ECR Public User Guide*.

## Pull and run the base container image
<a name="container-base-pull"></a>

**To pull and run the AL2027 base container image**

1. Pull the image from Amazon ECR Public.

   ```
   $ docker pull public.ecr.aws/amazonlinux/amazonlinux:2027
   ```

1. Run an interactive shell in the container.

   ```
   $ docker run --rm -it public.ecr.aws/amazonlinux/amazonlinux:2027 /bin/bash
   ```

## Manage software packages
<a name="container-base-package-management"></a>

The AL2027 base container image uses DNF5. Use the **dnf** command to manage software packages in the container. The **dnf** command invokes DNF5.
