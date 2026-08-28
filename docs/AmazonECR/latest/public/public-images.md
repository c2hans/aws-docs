---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/public/public-images.html
---

# Amazon ECR Public images
<a name="public-images"></a>

Amazon ECR Public is a fully-managed service provided by AWS that allows you to store, manage, and deploy Docker images, Open Container Initiative (OCI) images, and OCI compatible artifacts in public repositories. You can use the Docker CLI and other compatible clients to push and pull images to and from your Amazon ECR public repositories. Once stored, you can easily deploy these container images to various environments like Amazon ECS, Amazon EKS, or on-premises infrastructure.

Amazon ECR public provides features for managing the lifecycle of your container images, including tracking versions, applying tags, and controlling access to your public repositories. Amazon ECR public repositories are globally available, allowing you to distribute and consume container images from anywhere in the world.

**Important**
Amazon ECR requires that users have permission to make calls to the `ecr-public:GetAuthorizationToken` and `sts:GetServiceBearerToken` API through an IAM policy before they can authenticate to a registry and push any images to an Amazon ECR repository.

**Topics**
+ [Pushing an image to a public repository in Amazon ECR public](docker-push-ecr-image.md)
+ [Pushing a multi-architecture image to a public repository in Amazon ECR public](docker-push-multi-architecture-image.md)
+ [Pushing a Helm chart to a public repository in Amazon ECR public](push-oci-artifact.md)
+ [Pulling an image from the Amazon ECR Public Gallery](docker-pull-ecr-image.md)
+ [Deleting an image in a public repository in Amazon ECR public](public-image-delete.md)
+ [Container image manifest formats in Amazon ECR public](image-manifest-formats.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
