---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/container-repository-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Container repository management
<a name="container-repository-management"></a>

## Image Hierarchy Management
<a name="image-heirarchy-management"></a>

Most regulated customers have strict requirements around container patching, scanning, and hardening. Management of all container images in a consistent fashion may be challenging. If this is your situation, you will benefit from the following container image hierarchy:
+ Public images are images for OS and/or a specific version of runtime environments such as [Ubuntu](https://ubuntu.com/) or [TensorFlow](https://www.tensorflow.org/) Docker images. These images are stored in public repositories such as [ECR Public Gallery](https://gallery.ecr.aws/), [Github](https://github.com/), and [Docker Hub](https://hub.docker.com/).
+ Base images are foundational images stored in the customer ECR instance. These images are typically built from public images with additional custom patches and OS-level hardening procedures. Base images are owned by the central team and used across an organization.
+ Framework images are built on top of base images and should provide a stable version of the environment with a specific version of frameworks. For instance, platform container with the latest stable TensorFlow Serving framework configured. Framework images are typically also owned by the central team and available across the organization. Framework can also support dynamic loading of sources for flexibility.
+ Application images are used by teams to create a specific environment such as copy sources or compiled binaries or model artifacts for distribution. These images are owned by application teams and should be based on vetted framework images where possible.

  **Organizing repositories** — Amazon ECR provides a number of features to help organize images in the repository.
+ **Namespaces** — Amazon ECR supports namespaces, which allows the grouping of similar repositories into a common name. For example, each team or department can have its own namespace. This avoids potential conflicts with image naming, even if two departments use the exact same image names. In such a case, `department1/tensorflow-serving:latest` and `department2/tensorflow-serving:latest` are different images, as they are prefixed by a unique namespace.
+ **Image tagging** — Container registries provide the functionality to mark any image with a particular tag. There are several tagging schemes applicable for different use cases:
  + **Stable tags** — These tags typically have a specific version of OS or environment. For example, a “`tf-serving:v2.3`” image where “`v2.3`” is a stable tag to designate a specific version of pre-installed TensorFlow framework. A stable version doesn’t mean that image will be frozen, as TensorFlow framework can have minor releases and patches going on. For that reason, it’s recommended to use stable tags for the base and/or platform images.
  + **Unique tags** — This type of tag is typically used when tagging application images, and it includes a reference to the GitHub repository branch and commit hash. This allows easily tracing images to the source code if needed.
+ **Container security** — It is important to scan images for vulnerabilities and establish a continuous patching mechanism for all images. Consider incorporating these steps into the automated Docker image-build pipelines.

  Vulnerabilities in container software can be found on all levels: OS, packages, frameworks, or application code. It’s important to have an automatic way to consistently scan all container images on a recurrent basis.

  Amazon ECR image scanning helps in identifying software vulnerabilities in your container images. Amazon ECR uses the Common Vulnerabilities and Exposures (CVEs) database from the open-source Clair project and provides you with a list of scan findings. You can review the scan findings for information about the security of the container images being deployed. For more information about Clair, see [Clair](https://github.com/quay/clair) on GitHub.

  A customer may choose to use other 3rd party solutions, such as [Aqua Container Security Platform](https://info.aquasec.com/), to scan for vulnerabilities before pushing containers to ECR.

  With the proposed hierarchical approach for container images, it’s easy to ensure that all images are patched regularly. It’s recommended to rebuild base images with the latest OS-level patches at least every 30 days (or as soon as known vulnerabilities are fixed). All dependent platform images should also be rebuilt automatically after the patch is applied to base images. Application containers will be rebuilt on the next commit and will include patches from the upstream platform and base images.
+ **Access Control** — Amazon ECR is fully integrated with the Identity and Access Management service to provide you with granular authorization controls. It supports two types of policies:
  + **Resource-based policies** grant usage permission to other accounts on a per-resource basis. You can also use a resource-based policy to allow an AWS service to access your Amazon ECR repositories.
  + **Identity-based policies** specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. These policies are applied to IAM roles.
+ **Cross-account access** — The ECR repository, hosted in the Shared Services account, needs to provide access to users or services from other AWS accounts. Amazon ECR supports granting such permissions via IAM policies.

  For example, the following policy establishes access to ECR repository by a principal in another account.
