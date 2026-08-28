---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/security-formatting-best-practices.html
---

# Scan for security vulnerabilities and formatting errors
<a name="security-formatting-best-practices"></a>

Infrastructure as code (IaC) and automation have become essential for enterprises. With IaC being so robust, you have a large responsibility to manage security risks. Common IaC security risks can include the following:
+ Over-permissive AWS Identity and Access Management (IAM) privileges
+ Open security groups
+ Unencrypted resources
+ Access logs not turned on

## Security approaches and tools
<a name="security-approaches-and-tools.c1d77dd7-ae49-5e43-8340-ac17fca39c48"></a>

We recommend that you implement the following security approaches:
+ **Vulnerability detection in development** – Remediating vulnerabilities in production is expensive and time-consuming due to the complexity of developing and distributing software patches. Additionally, vulnerabilities in production carry the risk of exploitation. We recommend that you use code scanning on your IaC resources so that vulnerabilities can be detected and remediated prior to release into production.
+ **Compliance and auto-remediation **– AWS Config offers AWS managed rules. These rules help you enforce compliance and enable you to attempt auto-remediation by using [AWS Systems Manager automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html). You can also create and associate custom automation documents by using AWS Config rules.

## Common development tools
<a name="common-dev-tools"></a>

The tools covered in this section help you to extend their built-in functionality with your own custom rules. We recommend that you align your custom rules with your organization's standards. Here are some common development tools to consider:
+ Use cdk-nag to validate that constructs within a given scope comply with a defined set of rules. You can also use cdk-nag for rule suppression and compliance reporting. The cdk-nag tool validates constructs by extending [aspects](https://docs.aws.amazon.com/cdk/v2/guide/aspects.html) in the AWS CDK. For more information, see [Manage application security and compliance with the AWS CDK and cdk-nag](https://aws.amazon.com/blogs/devops/manage-application-security-and-compliance-with-the-aws-cloud-development-kit-and-cdk-nag/) in the AWS DevOps Blog.
+ Use the open-source tool Checkov to perform static analysis on your IaC environment. Checkov helps identify cloud misconfigurations by scanning your infrastructure code in Kubernetes, Terraform, or CloudFormation. You can use Checkov to get outputs in different formats, including JSON, JUnit XML, or CLI. Checkov can handle variables effectively by building a graph that shows dynamic code dependency. For more information, see the GitHub [Checkov](https://github.com/bridgecrewio/checkov) repository from Bridgecrew.
+ Use TFLint to check for errors and deprecated syntax and to help you enforce best practices. Note that TFLint may not validate provider-specific issues. For more information on TFLint, see the GitHub [TFLint](https://github.com/terraform-linters/tflint) repository from Terraform Linters.
+ Use Amazon Q Developer to perform [security scans](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-scans.html). When used in an integrated development environment (IDE), Amazon Q Developer provides AI-powered software development assistance. It can chat about code, provide inline code completions, generate net new code, scan your code for security vulnerabilities, and make code upgrades and improvements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
