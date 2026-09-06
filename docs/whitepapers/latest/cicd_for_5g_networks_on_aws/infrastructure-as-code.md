---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/infrastructure-as-code.html
---

# Infrastructure as Code
<a name="infrastructure-as-code"></a>

As detailed in the [*5G Network Evolution with AWS*](https://d1.awsstatic.com/whitepapers/5g-network-evolution-with-aws.pdf)* whitepaper*, IaC is a key driver to automate the provisioning process and life cycle management for both the application and its environment. Rather than relying on manually performed steps, both network/IT administrators and developers can instantiate infrastructure using configuration files. IaC treats these configuration files as software code. These files can be used to produce a set of artifacts: namely the compute, storage, network, and application services that comprise an operating environment. IaC eliminates configuration drift through automation, thereby increasing the speed and agility of infrastructure deployments.

In the case of Network Function Virtualization (NFV) implementation on AWS, this IaC framework brings a value from the perspective of orchestration. From the Virtual Private Cloud (VPC) creation to the network function deployment, every step can be programmed, managed as a source code, and maintained with version control in [AWS CodeCommit](https://aws.amazon.com/codecommit/).

This IaC framework for network function results in repeatable and reliable infrastructure and network function creation and deployment, which can be stretched to the end-to-end (E2E) automation of network slice management and service lifecycle management. AWS provides a comprehensive toolset for creating, maintaining, and deploying infrastructure in a programmatic, descriptive, and declarative way, using services such as CloudFormation, AWS CDK, AWS CDK for Kubernetes, and API exposure of all AWS Services.
