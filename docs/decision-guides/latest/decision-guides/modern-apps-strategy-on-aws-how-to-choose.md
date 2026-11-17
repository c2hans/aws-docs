---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/modern-apps-strategy-on-aws-how-to-choose.html
---

# Choosing a modern application strategy
<a name="modern-apps-strategy-on-aws-how-to-choose"></a>

**Taking the first step**

|  |  |
| --- |--- |
| **Purpose** | Help determine which modern application development approach is the best fit for your organization. |
| **Last updated** | November 13, 2026 |
| **Covered services** |  +  [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started.html) <br />+  [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) <br />+  [Amazon ECS Express Mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-overview.html) <br />+  [AWS App Runner](https://docs.aws.amazon.com/apprunner/) <br />+  [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) <br />+  [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html) <br />+  [Red Hat OpenShift Service on AWS](https://docs.aws.amazon.com/ROSA/latest/userguide/getting-started.html) <br />+  [AWS Transform](https://aws.amazon.com/transform/)   |

**AWS App Runner availability**
AWS App Runner closed to new customers on April 30, 2026. Existing customers can continue to use the service, including creating new resources. If you are a new customer and want a similar experience that runs containers without managing infrastructure, use Amazon ECS Express Mode. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html) and [Amazon ECS Express Mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-overview.html).

## Introduction
<a name="intro"></a>

Amazon Web Services (AWS) gives you the flexibility to choose different compute options to build and run modern applications that map to your business needs. It provides access to the right operational model for your compute choice.

Developers and data engineers prefer a level of autonomy when choosing which compute models match which workloads. When initially developing modern applications, development teams need to manage and operate their applications directly.

As more workloads are developed, you might decide to create central platform or operations teams. The function of these central teams varies. Some provide standard architectures and templated patterns for development teams to use. Others operate and manage workloads on behalf of multiple development teams.

These central teams strive to create standards for controlling costs, achieving the right performance and security, simplifying operations, and providing common architecture patterns. Achieving the right balance between autonomy and standardization is a challenge that enterprises and other large organizations often face.

It is common to choose one of two operational models to meet this challenge: [serverless compute](https://aws.amazon.com/serverless/) or [Kubernetes](https://aws.amazon.com/kubernetes/).

When you modernize existing applications, you can also use AI-assisted services to accelerate the work. AWS Transform uses agentic AI to migrate and modernize .NET, VMware, and mainframe workloads at scale. For building AI agents into your applications, AWS provides Amazon Bedrock AgentCore, the open source Strands Agents SDK, and the AWS Well-Architected Agentic AI Lens for design guidance.

[![AWS Videos](https://img.youtube.com/vi/OJD3UMuU8Zk/0.jpg)](https://www.youtube.com/watch?v=OJD3UMuU8Zk)

## Understand
<a name="understand"></a>

Developers and data engineers might have different compute requirements. For example, a developer might choose AWS Lambda because it is optimized for event-driven patterns and gives access to hundreds of managed integrations.

Alternatively, a data engineer might choose an open-source framework like Kubeflow or Ray on [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) (Amazon EKS) because it simplifies deployment of machine-learning models but allows access to the right high-powered instances.

[![AWS Videos](https://img.youtube.com/vi/1hN9SuRsnNQ/0.jpg)](https://www.youtube.com/watch?v=1hN9SuRsnNQ)

Each role tends to develop skills in technology stacks over time and has preferences about the tools they use. Both developers and data engineers look at their compute choice on a workload-by-workload basis, which means operational roles need to support a variety of workloads since they often work across teams. These roles include platform engineers, cloud administrators, or site reliability engineers (SREs).

Those in operational roles are challenged to provide autonomy for developers and data engineers while making sure they can deploy, operate, and monitor all workloads consistently to meet security, performance, resiliency, and cost requirements. Over time, as you develop more modern applications, these roles need to standardize on the tools to automate the deployment and monitoring of their workloads.

![Diagram showing the operational models for modular architecture patterns.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/operational-models-for-modular-architecture.png)

The choice between serverless compute and Kubernetes as an operational model is often driven by the need to have the right balance between autonomy and standardization with the number of resources one dedicates to running and operating workloads. Many workloads can be built successfully using either of these options. But, for some workloads, there are inherent advantages of one over the other.

A good team can make the compute choice entirely transparent to developers. Poor choices can limit developers' options, and lead to sub-standard outcomes. Operators are always affected by the selected operating model and it will determine needs such as common libraries and networking configuration—as well as how the organization will interact with underlying services it needs to configure.

The operational model will often be determined by your organizational structure and skill around automation and operations. These roles might be distributed across development teams, different parts of your organization, or be centralized. The structure and skills of these teams are often among the most important considerations when choosing between a serverless or Kubernetes operational model.

The serverless operational model prioritizes shifting much of the work involved in provisioning and managing compute resources to AWS. This model includes services such as [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) and the [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html).

The second model, Kubernetes on AWS, meets an important need for organizations that prioritize the [Cloud Native Computing Foundation (CNCF) ecosystem](https://www.cncf.io/) with a managed experience using [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html).

## Consider
<a name="consider"></a>

For developers and data engineers, we recommend that you evaluate the most appropriate compute option on a workload-by-workload basis within your operational strategy. Here are some of the key criteria to consider when determining your strategy.

------
#### [ Organizational structure and skill ]

Enterprises tend to organize their development teams around one of the following models:
+ **Distributed:** Each team owns their development, deployment, and operational functions. This model provides a high level of autonomy and allows teams to innovate at their own pace.
+ **Centralized:** A centralized team maintains standards, creates automations, and facilitates the sharing of knowledge and best practices.

These are separate ends of a spectrum. Organizations can start with a distributed model and later migrate toward a centralized model. This shift often happens as the number of workloads increases and consistency across cost, performance, and security becomes more important. However, in both models, serverless can reduce the infrastructure management overhead.

Organizations adopt another model, especially in the Kubernetes space: central teams that specialize in platform engineering. These skilled engineering teams have developer skills and build and maintain platforms made up of common automation, deployment, and observability tools. Amazon EKS is often the choice for these organizations.

Identifying the structure and skill of your development teams can be critical to choosing the appropriate platform.

------
#### [ Operational model ]

Organizations standardize on automation technologies to take full advantage of the cloud. The strategy and tools that infrastructure, platform, and DevOps teams use often drive these decisions.

For example, organizations have choices for tooling that automates the creation, configuration, and maintenance of infrastructure, resources, and workloads. These tools include infrastructure as code (IaC) tools such as Terraform, AWS CDK, CloudFormation, and other community tools.

Organizations that use Kubernetes might use Kubernetes-based tools for automation using GitOps tools such as Argo CD, and Kubernetes API-based cloud provisioning tools like [AWS Controllers for Kubernetes (ACK)](https://github.com/aws-controllers-k8s/community), [Kube Resource Orchestrator (kro)](https://github.com/kro-run/kro), or the [CNCF Crossplane project](https://www.cncf.io/projects/crossplane/). Amazon EKS Capabilities provides managed Argo CD, AWS Controllers for Kubernetes, and kro, so platform teams can use these tools without installing and operating them in their clusters.

These tooling choices also cover security, testing, networking, observability, performance, and more. For each of these categories, there is a stack of available tools.

These automation tools often have built-in integrations and accelerators for compute choices. For example, AWS Serverless Application Model (AWS SAM) is optimized for serverless developers to build and quickly deploy Lambda functions. Other tools, such as Argo CD, automate the deployment and configuration of Kubernetes workloads.

As customers increase workloads, it can be a burden to support a large number of tooling choices. We recommend standardizing a set that supports the most workload patterns.

------
#### [ Workload characteristics ]

It is important to evaluate the most appropriate compute option on a workload-by-workload basis within the default strategy. You should always strive to achieve the desired performance, security, and cost benefit for each workload.

A good standardization strategy allows for different use cases such as microservices, modernized monoliths, event-driven architectures, tools built by operations teams, and data processing workloads, such as machine learning, batch processing, and stream processing.

These workloads have different architectural characteristics. The strategy adopted should allow flexibility to support all the stages of a developer or data scientist workflow.
+ **Application developer:** Needs to run multiple environments such as development, prototyping, test, staging, and production.
+ **Data engineer:** These workflows involve streaming and acting on large data models, cleaning, training, running inference with models, and building applications and data pipelines that experiment with the data, including Jupyter Notebooks.
+ **AI/ML scientist:** Generative Artificial Intelligence (AI) Large Language Models (LLM) might require accelerated compute such as AWS Trainium or GPU instances.

------
#### [ Integrations ]

Applications do not exist in isolation. They are supported by technologies such as databases, messaging, streaming, orchestration, and other services. An effective modern app development strategy requires integration with these services. Managed integrations simplify operational overhead as much as management of the underlying infrastructure.

AWS [serverless compute options](https://docs.aws.amazon.com/serverless/latest/devguide/welcome.html), such as AWS Lambda, are integrated into the AWS ecosystem. Lambda can subscribe to events from more than 250 other services.

AWS-managed offerings for Kubernetes also provide integrations with many AWS managed offerings. For example, you can use AWS Controllers for Kubernetes to provision native AWS resources using a Kubernetes API. In addition, Kubernetes has a rich ecosystem, offering integration with numerous open-source projects. Amazon EKS works [with many other AWS services](https://docs.aws.amazon.com/eks/latest/userguide/eks-integrations.html) to provide additional solutions for business challenges.

------
#### [ Prototyping ]

Many organizations need to create experiments to validate ideas. The ability to provide an environment where you can quickly write, deploy, and validate ideas is essential for a healthy environment.

This environment is often overlooked when developing a modern app development strategy, but the ability to innovate can depend on it. Enabling teams to use services that allow builders to rapidly build, test, and iterate help in discovering new business opportunities and receive feedback faster.

Serverless compute options such as AWS Lambda and Amazon ECS Express Mode are optimized to help organizations write code quickly, deploy it, and change it. These capabilities provide useful options for fast prototyping work that does not require many choices upfront. Developers can quickly turn an idea into a modern, working application. The [AWS serverless compute option](https://docs.aws.amazon.com/serverless/latest/devguide/welcome.html) provides choices to prototype with minimal cost or operational overhead.

You can also use other options for prototyping. For Amazon ECS, you can create dedicated clusters and use AWS Fargate or dedicated nodes. For Kubernetes, platform teams can create dedicated clusters or dedicate namespaces within a cluster to prototyping teams. You can use open source projects such as [CNCF BuildPacks on the buildpacks.io website](https://buildpacks.io/) or [Knative on the Knative website](https://knative.dev/docs/) to simplify the configuration experience.

------
#### [ AI-assisted modernization ]

If you are modernizing existing applications, consider services that use AI to accelerate the work. Choose AWS Transform when you need AI-assisted .NET, VMware, or mainframe modernization at scale. AWS Transform uses agentic AI to automate discovery, planning, and code transformation, with human review at key steps.

AWS Transform includes the following options:
+ **AWS Transform custom:** Transforms code patterns such as language version upgrades, framework migrations, and code refactoring. For more information, see [AWS Transform custom](https://docs.aws.amazon.com/transform/latest/userguide/custom.html).
+ **AWS Transform continuous modernization:** A managed option that analyzes and remediates technical debt across connected repositories on an ongoing basis. For more information, see [AWS Transform continuous modernization](https://docs.aws.amazon.com/transform/latest/userguide/continuous-modernization.html).

------
#### [ Agentic architecture patterns ]

Modern applications increasingly include AI agents. If you are building agents into your applications, consider the following AWS options:
+ **Amazon Bedrock AgentCore:** Choose Amazon Bedrock AgentCore when you need managed infrastructure to deploy and operate AI agents, including runtime, memory, identity, and tool access. AgentCore works with open source agent frameworks and models in or outside Amazon Bedrock. For more information, see [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/).
+ **Amazon ECS and Amazon EKS:** Choose Amazon ECS or Amazon EKS when you want to run agents alongside your existing containerized applications, with the same deployment, networking, security, and scaling controls you already use.
+ **Strands Agents SDK:** Choose the Strands Agents SDK when you want an open source, model-driven SDK to build agents in code. For more information, see [Introducing Strands Agents, an open source AI agents SDK](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/).
+ **AWS Well-Architected Agentic AI Lens:** Use the Agentic AI Lens for design guidance that covers agent infrastructure, orchestration patterns, and operational practices. For more information, see [AWS Well-Architected Agentic AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentic-ai-lens.html).

------
#### [ AI-augmented development ]

AI coding tools can help development teams write, review, and refactor code. Choose Kiro when you need an agentic development tool with spec-driven workflows, chat, and Model Context Protocol (MCP) support. For more information, see [Kiro on the kiro.dev website](https://kiro.dev/).

If your teams use the Amazon Q Developer IDE plugins, note that AWS will discontinue support for them on April 30, 2027, and stopped accepting new sign-ups on May 15, 2026. Kiro is the recommended successor for similar IDE and agentic coding capabilities. For more information, see [Amazon Q Developer IDE plugins end of support](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-developer-ide-end-of-support.html).

------

## Choose
<a name="choose"></a>

The following comparison table can help you determine your approach based on your workload requirements. You might choose pieces of both approaches, or have different teams that use different approaches. Large organizations commonly have departments with different strategies.

| Modern application approach | When would you use it? | What workload is it optimized for? | Serverless services |
| --- |--- |--- |--- |
| Serverless | Use when AWS managed services and tools are your first choice, such as AWS Lambda and Amazon ECS with AWS Fargate, including Amazon ECS Express Mode. | Optimized to let developers focus on writing code without provisioning or managing servers, which minimizes operational overhead. | [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)<br />[Amazon ECS Express Mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-overview.html)<br />[AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)<br />[AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) |
|  Kubernetes  |  Use when Kubernetes is your primary compute platform interface.  |  Optimized for teams that want Kubernetes and the CNCF ecosystem as their standard platform interface. Teams with platform engineering skills can customize and operate clusters directly. Teams without them can use Amazon EKS Auto Mode, which manages compute, storage, and networking and keeps nodes patched and up to date.  |  [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) [Amazon EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/automode.html) [Red Hat OpenShift Service on AWS (ROSA)](https://docs.aws.amazon.com/rosa/latest/userguide/what-is-rosa.html)  |
| --- |--- |--- |--- |

If you are modernizing existing applications rather than starting new ones, choose AWS Transform when you need AI-assisted .NET, VMware, or mainframe modernization at scale. AWS Transform uses agentic AI to automate discovery, planning, and code transformation, with human review at key steps. For more information, see [AWS Transform](https://aws.amazon.com/transform/).

**Note**
App2Container, Microservice Extractor for .NET, and AWS Migration Hub Refactor Spaces closed to new customers on November 7, 2025. AWS Transform is the recommended successor for these modernization tasks. For more information, see [AWS Transform custom](https://docs.aws.amazon.com/transform/latest/userguide/custom.html).

## Use
<a name="use"></a>

Now that you have determined which approach best fits your workload for your environment, we recommend that you review the following service-specific resources to help you begin implementing your approach. This includes links to in-depth documentation, hands-on tutorials, and other key assets to help get you started.

------
#### [ Amazon ECS ]
+ **Getting started with Amazon ECS**

  We provide an introduction to the tools available to access Amazon ECS and introductory step-by-step procedures to run containers.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started.html)
+ **Tutorials for Amazon ECS**

  Explore more than a dozen tutorials on how to perform common tasks—including the creation of clusters and VPCs.

  [Get started with the tutorials](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-tutorials.html)
+ **Containers on AWS**

  Learn about containers on AWS through blog posts, code patterns, and visuals.

  [Explore the site](https://containersonaws.com/)
+ **Amazon ECS deployment**

  This guide offers an overview of Amazon ECS deployment options on AWS and shows how to use it to manage a simple containerized application.

  [Explore the guide](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/amazon-elastic-container-service.html)
+ **Amazon ECS Immersion Day**

  This workshop expands on your foundational understanding of containers and provides practical experience scaling, monitoring, and managing container workflows using Amazon ECS and AWS Fargate.

  [Explore the workshop](https://catalog.workshops.aws/ecs-immersion-day/en-US)

------
#### [ AWS App Runner ]

**Note**
AWS App Runner closed to new customers on April 30, 2026. If you are a new customer, use Amazon ECS Express Mode instead. Existing App Runner customers can continue to use the resources that follow.
+ **Getting started with AWS App Runner**

  Learn how to configure the source code and deployment, service build, and service runtime to deploy your application to App Runner.

  [Get started with the tutorial](https://docs.aws.amazon.com/apprunner/latest/dg/getting-started.html)
+ **AWS App Runner: From code to a scalable, secure web application in minutes**

  Explore how AWS App Runner was designed to make it easier for you to deploy web apps and APIs to the cloud, regardless of the language they are written in, even for teams that lack prior experience deploying and managing containers or infrastructure.

  [Read the blog](https://aws.amazon.com/blogs/aws/app-runner-from-code-to-scalable-secure-web-apps/)
+ **Deploy a web app using AWS App Runner**

  Learn how to deploy a containerized web app using AWS App Runner. Start with your source code or a container image. App Runner automatically builds and deploys the web application and load balances traffic with encryption.

  [Get started with the tutorial](https://aws.amazon.com/getting-started/guides/deploy-webapp-apprunner/)

------
#### [ Amazon ECS Express Mode ]
+ **Create your first Amazon ECS Express Mode service**

  Follow a step-by-step tutorial to deploy your first web application or API with Amazon ECS Express Mode.

  [Get started with the tutorial](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-getting-started.html)
+ **Amazon ECS Express Mode overview**

  Learn how Amazon ECS Express Mode provisions and configures the infrastructure to run a web application or API, including a Fargate-based service, a load balancer with SSL/TLS, auto scaling, monitoring, and networking.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-overview.html)

------
#### [ AWS Transform ]
+ **AWS Transform custom**

  Learn how AWS Transform custom uses agentic AI to transform code patterns such as language version upgrades, framework migrations, and code refactoring.

  [Explore the guide](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)
+ **AWS Transform continuous modernization**

  Learn how AWS Transform analyzes and remediates technical debt across connected repositories as a managed, ongoing process.

  [Explore the guide](https://docs.aws.amazon.com/transform/latest/userguide/continuous-modernization.html)
+ **AWS Transform**

  Explore how AWS Transform accelerates .NET, VMware, and mainframe modernization.

  [Explore the service](https://aws.amazon.com/transform/)

------
#### [ AWS Fargate ]
+ **Getting started with AWS Fargate**

  Understand the basics of AWS Fargate, a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of EC2 instances.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html)
+ **Getting started with the console using Linux containers on AWS Fargate**

  Get started with Amazon ECS on AWS Fargate by using the Fargate launch type for your tasks in the Regions where Amazon ECS supports AWS Fargate.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/userguide/getting-started-fargate.html)

------
#### [ AWS Lambda ]
+ **What is AWS Lambda**

  Learn more about AWS Lambda, a compute service that lets you run code without provisioning or managing servers.

  [Explore the guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
+ **Using AWS Lambda with other services**

  Explore common use cases and learn how invocation works. This guide includes a table of the services that work with Lambda and how each service invokes it.

  [Explore the guide](https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html)
+ **Serverless Land**

  Get the latest information, blogs, videos, code, and resources for AWS serverless.

  [Explore the site](https://serverlessland.com/)
+ **Guide to AWS Lambda Pricing**

  Explore and understand AWS Lambda pricing. You are charged based on the number of requests for your functions and the duration your code runs.

  [Explore the guide](https://aws.amazon.com/lambda/pricing/)

------
#### [ Amazon EKS ]
+ **Getting started with Amazon EKS**

  Learn more about Amazon EKS, a managed service that you can use to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes.

  [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)
+ **Amazon EKS deployment**

  Explore Amazon EKS deployment options on AWS and learn how it can be used to manage a general containerized application.

  [Explore the guide](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/amazon-elastic-kubernetes-service.html)
+ **Deploy a Kubernetes application on Linux**

  Learn how to deploy a containerized application to a Kubernetes cluster managed by Amazon EKS on Linux nodes.

  [Get started with the tutorial](https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment.html)
+ **Deploy a Kubernetes application on Windows**

  Learn how to deploy a containerized application onto a Kubernetes cluster managed by Amazon EKS on Windows nodes.

  [Get started with the tutorial](https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment-win.html)
+ **Amazon EKS workshop**

  Explore practical exercises to learn about Amazon EKS.

  [Visit the workshop](https://www.eksworkshop.com/)
+ **Streamline Kubernetes cluster management with Amazon EKS Auto Mode**

  Learn how you can automate cluster management without deep Kubernetes expertise using Amazon EKS Auto Mode.

  [Read the blog](https://aws.amazon.com/blogs/aws/streamline-kubernetes-cluster-management-with-new-amazon-eks-auto-mode/)
+ **Use your on-premises infrastructure in Amazon EKS clusters with Amazon EKS Hybrid Nodes**

  With Amazon EKS Hybrid Nodes, you can unify Kubernetes management across your cloud and on-premises environments, and take advantage of the scale and availability of Amazon EKS in all the places your applications need to run.

  [Read the blog](https://aws.amazon.com/blogs/aws/use-your-on-premises-infrastructure-in-amazon-eks-clusters-with-amazon-eks-hybrid-nodes/)

------
#### [ ROSA ]
+ **Getting started with Red Hat OpenShift Service on AWS**

  Learn how to get started using Red Hat OpenShift Service on AWS.

  [Explore the guide](https://docs.aws.amazon.com/ROSA/latest/userguide/getting-started.html)
+ **Why would you use ROSA?**

  Learn when you might use Red Hat OpenShift instead of standard Kubernetes, and explore ROSA on AWS in depth.

  [Watch the video](https://pages.awscloud.com/apn-tv-596.html)

------

## Explore
<a name="explore"></a>
+ **Architecture diagrams**

  Explore reference architecture diagrams to help you implement your modern app development approach.

  [ Explore architecture diagrams](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&amp;cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23modern-applications%7Ctech-category%23serverless%7Ctech-category%23containers&awsf.industries=*all&awsf.business-category=*all&awsm.page-cards-all=1)
+ **Whitepapers**

  Explore whitepapers to learn best practices in implementing your modern app development approach.

  [Explore whitepapers ](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=tech-category%23modern-applications%7Ctech-category%23serverless&awsf.industries=*all&awsf.business-category=*all&awsm.page-cards-all=2)
+ **AWS Solutions**

  Explore vetted solutions and architectural guidance for common modern app development use cases.

  [Explore solutions](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23solution&awsf.methodology=*all&awsf.tech-category=tech-category%23modern-applications%7Ctech-category%23serverless%7Ctech-category%23containers&awsf.industries=*all&awsf.business-category=*all&awsm.page-cards-all=1)
+ **AWS Well-Architected Agentic AI Lens**

  Explore design guidance and best practices for building agentic AI into your applications, including agent infrastructure, orchestration, and operations.

  [Explore the lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentic-ai-lens.html)
