---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/container-minimal.html
---

# AL2027 minimal container image
<a name="container-minimal"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

The AL2027 minimal container image is a separate container image variant. You can use it as a starting point and install the packages that your application requires.

The minimal container image is available in the [Amazon ECR Public Gallery](https://gallery.ecr.aws/amazonlinux/amazonlinux).

## Minimal container image size
<a name="container-minimal-size"></a>

Because the AL2027 minimal container image contains fewer packages than the AL2027 base container image, it is also smaller. The following table compares the AL2027 container image options with the equivalent AL2023 container images.

**Note**
Image Size is as-shown on [Amazon Linux on Amazon ECR Public Gallery](https://gallery.ecr.aws/amazonlinux/amazonlinux).

| Image | Version | Image Size |
| --- | --- | --- |
| Amazon Linux 2023 base container image | 2023.12.20260831.0 | 54.6MB |
| Amazon Linux 2023 minimal container image | 2023.12.20260831.0-minimal | 37.4MB |
| Amazon Linux 2027 base container image | 2027.0.20260903.0 | 44.8MB |
| Amazon Linux 2027 minimal container image | 2027.0.20260903.0-minimal | 38.9MB |

## Pull the minimal container image
<a name="container-minimal-pull"></a>

Public repositories support unauthenticated pulls. For optional authentication, see [Authenticate to Amazon ECR Public (optional)](container-base.md#container-base-authenticate).

```
$ docker pull public.ecr.aws/amazonlinux/amazonlinux:2027-minimal
```

## Use the minimal image in a Dockerfile
<a name="container-minimal-dockerfile"></a>

The minimal container image uses DNF5. Use the **dnf** command to install packages. The following example installs GCC and removes cached repository data.

```
FROM public.ecr.aws/amazonlinux/amazonlinux:2027-minimal
RUN dnf install -y gcc && dnf clean all
```
