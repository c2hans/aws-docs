---
source_url: https://docs.aws.amazon.com/whitepapers/latest/containers-on-aws/container-repositories.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Container repositories
<a name="container-repositories"></a>

Containers are distributed using container images. Images are a compile time construct, defined by the Dockerfile manifest. It is made up of a set of instructions to create the containers. Images are stored in container registries. Within a registry, a collection of related images is grouped together as repositories. When an image is run as a container, it is pulled from the container registry and stored locally in the compute.

 Amazon Elastic Container Registry (Amazon ECR) is the AWS native managed container registry for Open Container Initiative (OCI) artifacts. It not only allows you to store container images, but also OCI artifacts such as Helm charts (a collection of files that describe a related set of Kubernetes resources) and open policy agent (OPA) bundles (tarballs that contain policies and data). With Amazon ECR, you can share container images privately within your organization using a private repository. By default, it is only accessible within your AWS account by IAM users with the necessary permissions. Amazon ECR also offers a public registry called Amazon ECR Public Gallery. Public repositories are available worldwide for anyone to discover and download. Amazon ECR comes with features like encryption at rest using [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) and in-transit using Transport Layer Security (TLS) endpoints. Using image lifecycle policies, you can automatically preserve the most recent images and archives the ones you don’t need. You can use rules and tagging to access container images faster.

 Amazon ECR image scanning helps in identifying software vulnerabilities in your container images by using CVEs database from the Clair project and provides a list of scan findings. Additionally, you can use VPC interface endpoints for Amazon ECR to restrict the network traffic between your VPC and Amazon ECR to Amazon network, without a need for an internet gateway, NAT gateway, or a VPN or Direct Connect. You can also use a registry of your choice such as DockerHub or any other cloud of self-hosted container registry and integrate seamlessly with AWS container services.

 Other notable features of Amazon ECR include support for pull through cache, image replication and support for multi-architecture container images. With Amazon ECR’s pull-through cache repositories, you can retrieve, store, and sync container artifacts stored in publicly accessible container registries. With frequent registry syncs and no additional tools to manage, pull-through cache repositories help you keep container images sourced from public registries up to date. You can configure your Amazon ECR private registry to support the replication of your Amazon ECR repositories. Amazon ECR supports both cross-Region and cross-account replication. Amazon ECR also supports creating and pushing Docker manifest lists, which are used for multi-architecture images. A manifest list is a list of images that is created by specifying one or more image names. In most cases, the manifest list is created from images that serve the same function, but for different operating systems or architectures.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
