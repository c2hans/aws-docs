---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/overview.html
---

# Overview
<a name="overview"></a>

Terraform providers are plugins that let Terraform interact with APIs. The Terraform AWS Provider is the official plugin for managing AWS infrastructure as code with Terraform. It handles authentication and translates Terraform configuration into AWS API calls that create, read, update, and delete AWS resources.

You configure the provider with a `provider` block in the root module. Each provider configuration works in one AWS account, the account of the credentials or role that it uses, and has a default AWS Region. For an example that manages resources in two Regions of one account, see **Configure providers for Regions and accounts** in [Structure for modularity](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/structure.html#modularity).

The practices in this guide apply the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) to Terraform. The security practices (temporary credentials, least privilege, encrypted state, secrets kept out of state) follow the [Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html). The backend, testing, and version management practices follow the [Operational Excellence Pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) and the infrastructure as code capabilities in [AWS Well-Architected DevOps Guidance](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/devops-guidance.html): changes reviewed before they run, repeatable deployments, and detecting drift.

## Objectives
<a name="objectives"></a>

This guide helps you gain operational knowledge on the Terraform AWS Provider and addresses the following business goals that you can achieve by following Infrastructure as Code (IaC) best practices around security, reliability, compliance, and developer productivity.
+ Improve infrastructure code quality and consistency across Terraform projects.
+ Accelerate developer onboarding and ability to contribute to infrastructure code.
+ Increase business agility through faster infrastructure changes.
+ Reduce errors and downtime related to infrastructure changes.
+ Optimize infrastructure costs by following IaC best practices.
+ Strengthen your overall security posture by implementing best practices.

## Target audience
<a name="target-audience"></a>

The target audience for this guide includes technical leads and managers who oversee teams that use Terraform for infrastructure as code (IaC) on AWS.

Other potential readers include infrastructure engineers, DevOps engineers, solutions architects, and developers who actively use Terraform to manage AWS infrastructure.

These best practices help you save time and realize the benefits of IaC in your role.
