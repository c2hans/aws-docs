---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/least-privilege-cloudformation/introduction.html
---

# Implementing policies for least-privilege permissions for AWS CloudFormation
<a name="introduction"></a>

*Nima Fotouhi, Philip Allchin, and Moumita Saha, Amazon Web Services*

[AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) is an infrastructure as code (IaC) service that helps you scale your cloud infrastructure development by provisioning AWS resources. It also helps you manage those resources throughout their lifecycle, across AWS accounts and AWS Regions. In CloudFormation, you define [templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html#cfn-concepts-templates), which act as a blueprint for a set of resources. You then provision those resources by creating and deploying a [stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html#w2ab1b5c15b9), which is a group of related resources that you manage as a single unit. You can also use CloudFormation to deploy [stack sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html), which are groups of stacks that you can create, update, and delete across multiple accounts and AWS Regions with a single operation. This guide provides an overview of how you can implement least-privilege permissions for AWS CloudFormation and resources provisioned through CloudFormation.

You can deploy CloudFormation stacks or stack sets by doing one of the following:
+ Directly access the AWS environment through an AWS Identity and Access Management (IAM) [principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) and deploy CloudFormation stacks.
+ Push the CloudFormation stacks in a deployment pipeline and initiate stack deployment through the pipeline. The pipeline accesses the AWS environment through an IAM principal and deploys the stacks. This approach is a recommended best practice.

For either of these approaches, permissions are required to deploy CloudFormation stacks. For example, consider a user planning to use CloudFormation to create an Amazon Elastic Compute Cloud (Amazon EC2) instance. That instance would require an IAM [instance profile](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) to access other AWS services. The IAM principal used to deploy the CloudFormation stack would require the following permissions:
+ Permissions to access CloudFormation
+ Permissions to create stacks in CloudFormation
+ Permissions to create instances in Amazon EC2
+ Permissions to create the required IAM instance profiles

## What is least privilege?
<a name="what-is-least-privilege"></a>

[Least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) is the security best practice of granting the minimum permissions required to perform a task. The principle of least privilege is part of the [Security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html) in the AWS Well-Architected Framework. When you implement this best practice, it can help protect your AWS environment from privilege escalation risks, reduce the attack surface, improve data security, and prevent user error (such as misconfiguring or deleting a resource by mistake).

To implement least privilege for your AWS resources, you configure policies, such as identity-based policies in [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html). These policies define permissions and specify access conditions. Organizations might start with AWS managed policies, but then they typically create custom policies that limit the scope of permissions to only the actions required for the workload or use case.

Least-privilege permissions for the CloudFormation service is an important security consideration. Because users and developers who interact with CloudFormation can have the ability to rapidly create, modify, or delete resources at scale, least privilege is especially critical. However, CloudFormation requires the permissions necessary to create, update, and modify resources in your AWS accounts. You must balance the need for permissions to operate CloudFormation with the principle of least privilege.

When applying the principle of least privilege to CloudFormation, you need to consider the following:
+ **Permissions for the CloudFormation service** – Which users require access to CloudFormation, what level of access do they require, and what actions can they take to create, update, or delete stacks?
+ **Permissions to provision resources** – Which resources can users provision through CloudFormation?
+ **Permissions for provisioned resources** – How do you configure least-privilege permissions for the resources you provision through CloudFormation?

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

By following the best practices and recommendations in this guide, you can:
+ Determine which users in your organization require access to CloudFormation, and then configure least-privilege permissions for those users.
+ Use stack policies to help protect CloudFormation stacks from unintended updates.
+ Configure least-privilege permissions for CloudFormation users and resources to help prevent privilege escalation and the confused deputy problem.
+ Use AWS CloudFormation to provision AWS resources with least-privilege permissions. This helps your organization maintain a more robust security posture.
+ Proactively reduce the amount of time, energy, and money required to investigate and mitigate security incidents.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for Cloud Infrastructure Architects, DevOps engineers, and site reliability engineers (SREs) who manage and provision resources by using CloudFormation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
