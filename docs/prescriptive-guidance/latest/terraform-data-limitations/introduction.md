---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-data-limitations/introduction.html
---

# Working around Terraform data source limitations on AWS
<a name="introduction"></a>

*Ram Kandaswamy, Amazon Web Services*

This guide provides automated solutions for handling one-time DevOps setup tasks that can't be addressed with standard resources when using HashiCorp Terraform on AWS. It covers two use cases: AWS Batch revision management for job definitions and Amazon Bedrock agent deployments.

The guide discusses how you can use null resources and other key components in Terraform to extend your infrastructure automation beyond traditional resource boundaries. The `terraform_data` type lets you inject custom scripts, run remote commands, and orchestrate complex deployment scenarios. By implementing null resources, you can create adaptive infrastructure that meets your unique operational challenges. This solution helps you transition from manual interventions to a programmable infrastructure that simplifies your DevOps process.

## About Terraform
<a name="about"></a>

Terraform is a popular infrastructure as code (IaC) tool by HashiCorp that enables users to define and manage their cloud and on-premises infrastructure by using a human-readable configuration file. As an IaC tool, Terraform solves the problem of manual provisioning and managing of infrastructure, which can be time-consuming, error-prone, and difficult to replicate. You can write infrastructure configurations in a declarative language, such as YAML or HashiCorp Configuration Language (HCL), and then use Terraform to create and manage the corresponding infrastructure resources.

AWS provides native IaC feature with the CloudFormation service. Some organizations use Terraform to manage their infrastructure, especially when they have hybrid cloud and on-premises resource management needs.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

Using the solutions described in this guide to define and manage your infrastructure provides the following benefits:
+ **Protecting enterprise investments**: The `null_resource` type in Terraform extends traditional enterprise systems with cloud infrastructure when standard resources are insufficient. It runs custom scripts, commands, and processes to maintain business continuity during cloud migrations. You can integrate your existing tools and workflows into your DevOps processes while meeting compliance requirements that differ from standard cloud configurations. This helps you enforce specific policies and perform specialized actions beyond what traditional Terraform resources can provide.
+ **Business agility**: Terraform's modular architecture supports complex deployments and system integrations through the use of custom provisioners. Your teams can build solutions for unique technical challenges without waiting for official provider support. This capability helps you:
  + Manage mixed environments of legacy and cloud systems.
  + Implement rapid prototypes of new infrastructure patterns.
  + Adapt quickly to changing business requirements.
  + Support ongoing digital transformation initiatives.
+ **Business continuity**: You can use custom provisioners and null resources to automate infrastructure operations by:
  + Eliminating manual interventions in deployment workflows.
  + Reducing human error in processes.
  + Orchestrating system updates with minimal downtime.
  + Maintaining uninterrupted business operations during infrastructure changes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
