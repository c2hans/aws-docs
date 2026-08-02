---
source_url: https://docs.aws.amazon.com/modern-apps-strategy-on-aws-how-to-choose/index.html
---

# Choosing a modern application strategy

Determine which modern application development approach is the best fit for your organization

## Overview of modern application development on AWS

AWS provides you with the flexibility to choose different compute options to build and run modern applications that map to your business needs. We provide you with access to the right operational model for your compute choice. Developers and data engineers prefer a level of autonomy when choosing which compute models match which workloads. When initially developing modern applications, development teams need to manage and operate their applications directly. As more workloads are developed, you might decide to create central platform or operations teams. The function of these central teams varies: some provide standard architectures and templated patterns for development teams to use, and others operate and manage workloads on behalf of multiple development teams. These central teams strive to create standards for controlling costs, achieving the right performance and security, simplifying operations, and providing common architecture patterns. Achieving the right balance between autonomy and standardization is a challenge that enterprises and other large organizations often deal with. It is common to choose one of two operational models to meet this challenge: [serverless compute](https://aws.amazon.com/serverless/), or [Kubernetes](https://aws.amazon.com/kubernetes/).

## Key concepts

For developers and data engineers, we recommend that you evaluate the most appropriate compute option on a workload-by-workload basis within your operational strategy. Here are some of the key concepts to consider when determining your strategy.

- **Organizational structure and how it influences compute choices**: Modern application development at AWS requires careful consideration of organizational structure and team skills when selecting compute platforms. Organizations typically adopt either distributed models where individual teams own their entire development lifecycle, or centralized models where specialized teams maintain standards and facilitate knowledge sharing. Many organizations start distributed, and evolve toward centralization as workloads scale and consistency becomes critical. A third approach involves platform engineering teams that build and maintain common automation and deployment tools, particularly in Kubernetes environments where Amazon EKS becomes the platform of choice. The key is matching compute platform decisions to your team's structure, skills, and operational capabilities, with serverless options offering reduced infrastructure management overhead across all models.

[Choosing an AWS compute service](/decision-guides/latest/compute-on-aws-how-to-choose/choosing-aws-compute-service.html)

- **Operational models and automation strategies**: Operational strategy heavily influences compute service selection through standardized automation technologies and tooling choices. Organizations benefit from infrastructure as code (IaC) tools like Terraform, AWS CDK, and CloudFormation, while Kubernetes-focused teams often leverage GitOps tools like ArgoCD, and API-based provisioning tools such as AWS Controllers for Kubernetes. These automation tools have built-in integrations optimized for specific compute choices. For example, AWS Serverless Application Model accelerates serverless Lambda development while ArgoCD automates Kubernetes deployments. As workloads multiply, supporting numerous tooling choices becomes burdensome, making standardization on a core set of tools that support the most common workload patterns essential for operational efficiency.

[Using AWS services for automation](/prescriptive-guidance/latest/migration-operations-integration/aws-services-for-automation.html)

- **Workload characteristics and flexibility needs**: It is important to evaluate the most appropriate compute option on a workload-by-workload basis within the default strategy. You should always strive to achieve the desired performance, security, and cost benefit for each workload. A good standardization strategy will allow for different use cases such as microservices, modernized monoliths, event-driven architectures, tools built by operation teams, and data processing workloads, such as machine learning, batch processing, and stream processing. These workloads have different architectural characteristics. The strategy adopted should allow flexibility to support all the stages of a developer or data scientist workflow. - **Application developer:** Needs to run multiple environments such as development, prototyping, test, staging, and production. - **Data engineer:** These workflows involve streaming and acting on large data models, cleaning, training, running inference with models, and building applications and data pipelines that experiment with the data, including Jupyter Notebooks - **AI/ML scientist:** Generative Artificial Intelligence (AI) Large Language Models (LLM) might require specialized compute instances such as AWS Trainium or other GPU-based architecture.

[Workload architecture](/wellarchitected/2024-06-27/framework/a-workload-architecture.html)

- **Integration and prototyping considerations**: Integration capabilities and rapid prototyping support are crucial elements of effective modern application development strategies. Applications rarely exist in isolation and require seamless integration with databases, messaging systems, orchestration services, and other components. AWS serverless options like Lambda excel here with integrations to over 250 AWS services, while managed Kubernetes offerings provide rich ecosystem integration through both AWS services and open-source projects. Equally important is enabling rapid prototyping and experimentation - serverless compute options like Lambda and AWS App Runner optimize for quick code deployment and iteration with minimal upfront decisions, while container platforms can provide dedicated clusters or namespaces for experimentation. This prototyping capability is often overlooked but essential for innovation, business opportunity discovery, and faster feedback cycles.

[Testing stages in continuous integration and continuous delivery](/whitepapers/latest/practicing-continuous-integration-continuous-delivery/testing-stages-in-continuous-integration-and-continuous-delivery.html)

## Use cases

Build and deploy applications faster while maintaining control over your development environment and infrastructure costs.

### Operational efficiency

Organizations can reduce infrastructure management overhead by choosing serverless options like Lambda and AWS App Runner, or implement standardized container orchestration with Amazon EKS, allowing teams to focus on building business value rather than managing infrastructure.

[App Runner](/apprunner)
[Amazon ECS](/ecs)
[Amazon EKS](/eks)
[Fargate](/ecs)
[Lambda](/lambda)
[Red Hat OpenShift Service on AWS](/rosa)

### Development team autonomy

Teams can select the most appropriate compute options for their specific workloads while maintaining organizational standards for security, cost control, and performance - whether they're building microservices, processing data, or deploying AI/ML models.

[App Runner](/apprunner)
[Amazon ECS](/ecs)
[Amazon EKS](/eks)
[Fargate](/ecs)
[Lambda](/lambda)
[Red Hat OpenShift Service on AWS](/rosa)

### Scalable platform management

As organizations grow, they can effectively balance developer autonomy with standardization through either serverless automation or centralized platform engineering teams, enabling consistent deployment, monitoring, and security practices across multiple applications.

[App Runner](/apprunner)
[Amazon ECS](/ecs)
[Amazon EKS](/eks)
[Fargate](/ecs)
[Lambda](/lambda)
[Red Hat OpenShift Service on AWS](/rosa)

### Rapid innovation

Both approaches support quick prototyping and experimentation - serverless options enable immediate deployment with minimal configuration, while Kubernetes-based solutions provide flexible, standardized environments for testing new ideas within established platforms.

[App Runner](/apprunner)
[Amazon ECS](/ecs)
[Amazon EKS](/eks)
[Fargate](/ecs)
[Lambda](/lambda)
[Red Hat OpenShift Service on AWS](/rosa)

## Compare options

AWS offers different container options, such as Amazon ECS, serverless containers with AWS Fargate , and AWS App Runner, and different Kubernetes options, such as Amazon EKS, ROSA, and self-managed Kubernetes on Amazon EC2.

| Modern application approach | When would you use it? | What workload is it optimized for? | Serverless services |
| --- | --- | --- | --- |
| Serverless | Use when AWS managed services and tools are your first choice, such as Lambda, AWS App Runner, and Amazon ECS. | Optimized for enabling developers to focus solely on writing code without the need to manage or provision servers, minimizing operational overhead. | [Amazon ECS](/AmazonECS/latest/developerguide/Welcome.html) <br> [AWS App Runner](/apprunner/latest/dg/what-is-apprunner.html) <br> [Fargate](/AmazonECS/latest/developerguide/AWS_Fargate.html) <br> [Lambda](/lambda/latest/dg/welcome.html) |
| Kubernetes | Use when Kubernetes is your primary compute platform interface. | Optimized for teams with central platforms teams that invest in platform engineering skills. Platform engineers are skilled at keeping clusters up to date with the fast-moving CNCF Kubernetes versioning strategy. | [Amazon EKS](/eks/latest/userguide/what-is-eks.html) <br> [ROSA](/rosa/latest/userguide/what-is-rosa.html) |

## Start building

Now that you have determined which approach best fits your workload for your environment, we recommend that you review the following service-specific resources to help you begin implementing your approach. This includes links to in-depth documentation, hands-on tutorials, and other key assets to help get you started.

### Amazon ECS

**Getting started with Amazon ECS**

We provide an introduction to the tools available to access Amazon ECS and introductory step-by-step procedures to run containers.

[Explore the guide](/AmazonECS/latest/developerguide/getting-started.html)

**Tutorials for Amazon ECS**

Explore more than a dozen tutorials on how to perform common tasks, including the creation of clusters and VPCs.

[Get started with the tutorials](/AmazonECS/latest/developerguide/ecs-tutorials.html)

**Containers on AWS**

Learn about containers on AWS through blog posts, code patterns, and visuals.

[Explore the site](https://containersonaws.com/)

**Amazon ECS deployment**

This whitepaper offers an overview of Amazon ECS deployment options on AWS and shows how it can be used to manage a simple containerized application.

[Explore the whitepaper](/whitepapers/latest/overview-deployment-options/amazon-elastic-container-service.html)

**Amazon ECS Immersion Day**

This workshop expands on your foundational understanding of containers and provides practical experience scaling, monitoring, and managing container workflows using Amazon ECS and Fargate.

[Explore the workshop](https://catalog.workshops.aws/ecs-immersion-day)

### AWS App Runner

**Getting started with AWS App Runner**

Learn how to configure the source code and deployment, service build, and service runtime to deploy your application to App Runner.

[Get started with the tutorial](/apprunner/latest/dg/getting-started.html)

**AWS App Runner: From code to a scalable, secure web application in minutes**

Explore how AWS App Runner was designed to make it easier for you to deploy web apps and APIs to the cloud, regardless of the language they are written in, even for teams that lack prior experience deploying and managing containers or infrastructure.

[Read the blog post](https://aws.amazon.com/blogs/aws/app-runner-from-code-to-scalable-secure-web-apps/)

**Deploy a web app using AWS App Runner**

Learn how to deploy a containerized web app using AWS App Runner. Start with your source code or a container image. App Runner automatically builds and deploys the web application and load balances traffic with encryption.

[Get started with the tutorial](https://aws.amazon.com/getting-started/guides/deploy-webapp-apprunner/)

### AWS Fargate

**Getting started with AWS Fargate**

Understand the basics of Fargate, a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of EC2 instances.

[Explore the guide](/AmazonECS/latest/developerguide/AWS_Fargate.html)

**Getting started with the console using Linux containers on Fargate**

Get started with Amazon ECS on Amazon ECS by using the Fargate launch type for your tasks in the Regions where Amazon ECS supports Amazon ECS.

[Get started with the tutorial](/AmazonECS/latest/developerguide/getting-started-fargate.html)

### AWS Lambda

**What is AWS Lambda?**

Learn more about AWS Lambda, a compute service that lets you run code without provisioning or managing servers.

[Explore the guide](/lambda/latest/dg/welcome.html)

**Using AWS Lambda with other services**

Explore common use cases, learn how invocation works and includes a table that covers the services that work with Lambda and how it can be invoked from that service.

[Explore the guide](/lambda/latest/dg/lambda-services.html)

**Serverless Land**

Get the latest information, blogs, videos, code, and resources for AWS serverless.

[Explore the site](https://serverlessland.com/)

**Guide to AWS Lambda Pricing**

Explore and understand AWS Lambda pricing. You are charged based on the number of requests for your functions and the duration it takes for your code to start.

[Explore the guide](https://aws.amazon.com/lambda/pricing/)

### Amazon EKS

**Getting started with Amazon EKS**

Learn more about Amazon EKS, a managed service that you can use to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes.

[Explore the guide](/eks/latest/userguide/getting-started.html)

**Deploy a Kubernetes application**

Learn how to deploy a containerized application onto a Kubernetes cluster managed by Amazon EKS.

[Get started with the tutorial](/eks/latest/userguide/sample-deployment.html)

**Amazon EKS workshop**

Explore practical exercises to learn about Amazon EKS.

[Visit the workshop](https://www.eksworkshop.com/)

**Streamline Kubernetes cluster management with Amazon EKS Auto Mode**

Learn how you can automate cluster management without deep Kubernetes expertise using Amazon EKS Auto Mode.

[Read the blog post](https://aws.amazon.com/blogs/aws/streamline-kubernetes-cluster-management-with-new-amazon-eks-auto-mode/)

**Use your on-premises infrastructure in Amazon EKS clusters with Amazon EKS Hybrid Nodes**

With Amazon EKS Hybrid Nodes, you can unify Kubernetes management across your cloud and on-premises environments, and take advantage of the scale and availability of Amazon EKS in all the places your applications need to run.

[Read the blog post](https://aws.amazon.com/blogs/aws/use-your-on-premises-infrastructure-in-amazon-eks-clusters-with-amazon-eks-hybrid-nodes/)

### ROSA

**Getting started with Red Hat OpenShift Service on AWS**

Learn how to get started using Red Hat OpenShift Service on AWS.

[Explore the guide](/rosa/latest/userguide/getting-started.html)

**Why would you use ROSA?**

Learn when you might use ROSA over standard Kubernetes and explore ROSA in depth.

[Watch the video](https://pages.awscloud.com/apn-tv-596.html)

## Resources

- **Learn**: [Whitepapers](https://aws.amazon.com/whitepapers/)
- **Build**: [Explore solutions](https://aws.amazon.com/solutions/)
- **Discover**: [Explore architecture diagrams](https://aws.amazon.com/architecture/)

---
