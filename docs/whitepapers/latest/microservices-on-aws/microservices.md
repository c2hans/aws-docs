---
source_url: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices.html
---

# Microservices
<a name="microservices"></a>

 APIs are considered the *front door* of microservices, as they are the entry point for application logic. Typically, RESTful web services API or GraphQL APIs are used. These APIs manage and process client calls, handling functions such as traffic management, request filtering, routing, caching, authentication, and authorization.

## Microservices implementations
<a name="microservices-implementations"></a>

 AWS offers building blocks to develop microservices, including Amazon ECS and Amazon EKS as the choices for container orchestration engines and AWS Fargate and EC2 as hosting options. AWS Lambda is another serverless way to build microservices on AWS. Choice between these hosting options depends on the customer’s requirements to manage the underlying infrastructure.

 AWS Lambda allows you to upload your code, automatically scaling and managing its execution with high availability. This eliminates the need for infrastructure management, so you can move quickly and focus on your business logic. Lambda supports [multiple programming languages](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) and can be triggered by other AWS services or called directly from web or mobile applications.

 Container-based applications have gained popularity due to portability, productivity, and efficiency. AWS offers several services to build, deploy and manage containers.
+  [App2Container](https://aws.amazon.com/app2container/), a command line tool for migrating and modernizing Java and .NET web applications into container format. AWS A2C analyzes and builds an inventory of applications running in bare metal, virtual machines, Amazon Elastic Compute Cloud (EC2) instances, or in the cloud.
+  Amazon Elastic Container Service ([Amazon ECS](https://aws.amazon.com/ecs/)) and Amazon Elastic Kubernetes Service ([Amazon EKS](https://aws.amazon.com/eks/)) manage your container infrastructure, making it easier to launch and maintain containerized applications.
  +  Amazon EKS is a managed Kubernetes service to run Kubernetes in the AWS cloud and on-premises data centers ([Amazon EKS Anywhere](https://aws.amazon.com/eks/eks-anywhere/)). This extends cloud services into on-premises environments for low-latency, local data processing, high data transfer costs, or data residency requirements (see the whitepaper on "[Running Hybrid Container Workloads With Amazon EKS Anywhere](https://d1.awsstatic.com/kubernetes-pmm/eks-a/getting-started/AWS_Whitepaper_Running_Hybrid_Container_Workloads_with_Amazon_EKS_Anywhere.pdf)"). You can use all the existing plug-ins and tooling from the Kubernetes community with EKS.
  +  Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service that simplifies your deployment, management, and scaling of containerized applications. Customers choose ECS for simplicity and deep integration with AWS services.

 For further reading, see the blog [Amazon ECS vs Amazon EKS: making sense of AWS container services](https://aws.amazon.com/blogs/containers/amazon-ecs-vs-amazon-eks-making-sense-of-aws-container-services/).
+  [AWS App Runner](https://aws.amazon.com/apprunner/) is a fully managed container application service that lets you build, deploy, and run containerized web applications and API services without prior infrastructure or container experience.
+  [AWS Fargate](https://aws.amazon.com/fargate/), a serverless compute engine, works with both Amazon ECS and Amazon EKS to automatically manage compute resources for container applications.
+  [Amazon ECR](https://aws.amazon.com/ecr/) is a fully managed container registry offering high-performance hosting, so you can reliably deploy application images and artifacts anywhere.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
