---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/containers.html
---

# Containers for computing
<a name="containers"></a>

Containers are a popular choice for a modern MES that comprises microservices. Containers are a powerful way for MES developers to package and deploy their applications—they are lightweight and provide consistent, portable software for MES applications to run and scale anywhere. Containers are also preferred for running batch jobs such as interface processing, running machine learning applications for use cases such as automated quality inspection, and moving legacy MES modules to the cloud. Almost all MES modules can use containers for computing.

## Architecture
<a name="containers-architecture"></a>

The architecture in the following diagram combines DNS and load balancing for a consistent user experience with backend containerized computing. It also includes a continuous integration and continuous deployment (CI/CD) pipeline for continuous updates.

![MES container-based architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/images/guide-img/093538ca-c7c9-4311-a0e9-8a876ae66d65/images/3d4dced7-8ccd-4f5c-8d21-ee6b7c4a970b.png)

1. The MES development team uses AWS CodePipeline to build, commit, and deploy the code.

1. The new container image is pushed to Amazon Elastic Container Registry (Amazon ECR).

1. Fully managed Amazon Elastic Kubernetes Service (Amazon EKS) clusters support computing functions for MES microservices such as production management and inventory management.

1. AWS database and cloud storage services are used to support the unique needs of the microservices.

1. Elastic Load Balancing (ELB) automatically distributes incoming traffic for MES modules across multiple targets in one or more Availability Zones. For more information, see [Workloads](https://docs.aws.amazon.com/eks/latest/userguide/eks-workloads.html) in the Amazon EKS documentation.

1. Amazon Route 53 serves as a DNS service to resolve incoming requests to the load balancer in the primary AWS Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
