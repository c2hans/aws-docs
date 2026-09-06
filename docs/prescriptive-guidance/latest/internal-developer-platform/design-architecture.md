---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/internal-developer-platform/design-architecture.html
---

# Designing an internal developer platform architecture
<a name="design-architecture"></a>

The following image shows the core components of an internal developer platform.

![Core components of an internal developer platform](http://docs.aws.amazon.com/prescriptive-guidance/latest/internal-developer-platform/images/guide-img/f2111ed6-8e9c-4bdd-8ade-3154f49ca33b/images/ec915990-1fc1-4414-a6d7-4241674c2ee9.png)

AWS recommends that organizations adopt a [multi-account strategy](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) to isolate and manage their applications and data. The same principle applies when building an internal developer platform. Deploy the internal developer platform in a [shared services](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/infrastructure-ou-and-accounts.html#shared-service-accounts) or a [tooling](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/deployments-ou.html) AWS account that has access to the rest of your organization's accounts. This supports different development teams that use different AWS accounts for their environments. It also centralizes management and provides cost visibility for all of the different components that are managed by the internal developer platform.

The internal developer platform requires an orchestrator to deploy its different components. You can use [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) or [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html). Build a cluster that hosts the different internal developer platform services to enable its capabilities. This architecture provides the ability to scale the platform infrastructure as it serves more end users. More information about platform capabilities is provided later in this guide, but in summary, these capabilities need to address the functionalities that developers need to manage their workloads. Examples include:
+ Security for workload protection
+ Infrastructure as code to manage the workload infrastructure
+ Continuous integration and continuous deployment (CI/CD) to automate the testing and deployment of workloads
+ Secure ingress to provide access to the workload services
+ Tenancy to isolate different teams and workloads
+ Observability to address logging, metrics, tracing, and alerting for workloads and their infrastructure

[Backstage](https://backstage.io/docs/overview/what-is-backstage) is the developer portal that connects all of these capabilities together. This helps developers manage all of their workloads in one place. It also centralizes costs so that you have visibility across all of the resources that the workloads use.

For reference architectures for internal developer platforms, see the following:
+ [Cloud-native internal developer platform architecture on Amazon EKS](https://github.com/cnoe-io/reference-implementation-aws)
+ [Harmonix on AWS](https://github.com/awslabs/harmonix)
