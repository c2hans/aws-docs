---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/docker-basics.html
---

# Docker container basics
<a name="docker-basics"></a>

The following page outlines the most significant aspects of using Docker containers with Amazon SageMaker AI.

Docker is a program that performs operating system-level virtualization for installing, distributing, and managing software. It packages applications and their dependencies into virtual containers that provide isolation, portability, and security. With Docker, you can ship code faster, standardize application operations, seamlessly move code, and economize by improving resource utilization. For more general information about Docker, see [Docker overview](https://docs.docker.com/engine/docker-overview/).

**SageMaker AI Functions**

SageMaker AI uses Docker containers in the backend to manage training and inference processes. SageMaker AI abstracts away from this process, so it happens automatically when a ModelTrainer is used. While you don't need to use Docker containers explicitly with SageMaker AI for most use cases, you can use Docker containers to extend and customize SageMaker AI functionality.

**Containers with Amazon SageMaker Studio Classic**

Studio Classic runs from a Docker container and uses it to manage functionality. As a result, you must create your Docker container following the steps in [Custom Images in Amazon SageMaker Studio Classic](studio-byoi.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
