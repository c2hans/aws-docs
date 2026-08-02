---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/introduction.html
---

# Introduction
<a name="introduction"></a>

Historically, development, lab and field integration testing, and production deployment of new network nodes or new features in a cellular network took weeks or even months to ensure the stability of mission and business critical telecommunications (telecom) services. The long cycle of deployment was caused by the monolithic architecture of traditional network nodes, a multi-vendor environment, and many point-to-point interfaces among network entities in the 2G, 3G, and 4G mobile networks.

As introduced in the [https://d1.awsstatic.com/whitepapers/5g-network-evolution-with-aws.pdf](https://d1.awsstatic.com/whitepapers/5g-network-evolution-with-aws.pdf) whitepaper, 5G mobile networks, as standardized by 3GPP, now support a cloud-native architecture enabled by virtualization and containerization. More specifically, 5G networks introduce and support a new paradigm of the microservice, stateless, and service-based architecture.

This 5G architecture means that different network functions can work as loosely coupled independent services that communicate with each other through well-defined interfaces and APIs. Most importantly, each network function can be updated independently. This architecture shift in 5G enables CSPs to achieve more agility and operational efficiency by making it easier to roll out updates for network functions more frequently, while maintaining the testing, security requirements, and standards through automation.

Integration and deployment of new features for a CSP generally start when the network function vendor releases a new network function software package, such as a [Docker](https://hub.docker.com/) image in a container-based network function, or a new configuration file, such as a [Helm](https://helm.sh/docs/topics/charts/) chart in the [Kubernetes](https://kubernetes.io/) application case. (A Helm chart is a collection of files that describe a related set of Kubernetes resources).

The idea of using the paradigm of CI/CD for 5G network function deployment is gaining traction, but the practical realization of this idea has been a challenge in the telecom industry.

AAWSWS has pioneered the development of new CI/CD tools for software delivery to help a broad spectrum of industries develop and roll out software changes rapidly, while maintaining systems stability and security. These tools include a set of Software Development and Operations (DevOps) services such as [AWS CodeStar](https://aws.amazon.com/codestar/), [CodeCommit](https://aws.amazon.com/codecommit/), [CodePipeline](https://aws.amazon.com/codepipeline/), [CodeBuild](https://aws.amazon.com/codebuild/), and [CodeDeploy](https://aws.amazon.com/codedeploy/).

AWS also evangelizes the idea of Infrastructure as Code (IaC) using the [AWS Cloud Development Kit ](https://aws.amazon.com/cdk/) (AWS CDK), [AWS CloudFormation](https://aws.amazon.com/cloudformation/), and API-based third-party tools such as [Terraform](https://www.terraform.io/). Using these tools, AWS can store the deployment processes of network function within AWS as a source code, and maintain this IaC source code in the CI/CD pipeline to realize continuous delivery.

This whitepaper describes detailed processes for leveraging AWS IaC and CI/CD tools for the deployment and update of the 5G network function. Additionally, this whitepaper covers integration with third-party tools for testing, observability, and orchestration.

AWS CI/CD tools are not restricted to 5G network functions. They are also employed for automating the deployment of 4G networks, which enables CSPs to rapidly and efficiently deploy and update 4G network functions. Most 4G network functions are Virtual Network Function (VNF) based. AWS CI/CD toolsets like AWS CloudFormation can be used to automate the deployment of 4G VNFs, bringing scale and time efficiency for 4G network deployments.
