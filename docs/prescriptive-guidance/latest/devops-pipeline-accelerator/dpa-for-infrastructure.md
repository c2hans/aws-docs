---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/devops-pipeline-accelerator/dpa-for-infrastructure.html
---

# DPA for infrastructure provisioning
<a name="dpa-for-infrastructure"></a>

In DPA version 1.0.0, plug-and-play templates for infrastructure-provisioning pipelines are available. These templates follow DevOps best practices, such as built-in security controls, automated deployments, versioning, and artifact management.

This section describes how to use DPA to implement centralized pipeline templates for infrastructure as code (IaC) tools. DPA supports widely used IaC tools, such as Terraform, AWS CDK, and CloudFormation. These templates are readily consumable with CI/CD services and tools, such as AWS CodePipeline and GitLab CI/CD.

The following image shows the DPA architecture for infrastructure provisioning. You use the CI/CD pipeline templates to provision infrastructure by using Terraform, CodePipeline, and AWS CDK.

![The DPA architecture for infrastructure provisioning.](http://docs.aws.amazon.com/prescriptive-guidance/latest/devops-pipeline-accelerator/images/guide-img/e56ba347-e180-48ee-bbf9-0b76e10e70f2/images/c0449d88-9345-4bee-90ae-ef257db6abb3.png)

The following image shows a reference pipeline for a Terraform-based application, which consumes the Terraform entry point. At the end of the post-deploy stage, the code enters a release pipeline for deployment to staging and production environments.

![A reference pipeline for a Terraform-based application](http://docs.aws.amazon.com/prescriptive-guidance/latest/devops-pipeline-accelerator/images/guide-img/e56ba347-e180-48ee-bbf9-0b76e10e70f2/images/1e6a599c-5f38-4ca3-8c7c-9bdc7d855d90.png)

Note the following when using DPA for infrastructure provisioning:
+ The type of events that occur in a repository affect the pipeline construction. For example, `pull` requests don't provision resources to the AWS Cloud. However, when a `pull` request merges into the main branch, the pipeline provisions the resources to the AWS Cloud.
+ The pipeline uses security scanning tools, such as [tfsec](https://aquasecurity.github.io/tfsec/v1.28.4/), [Checkov](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html), and [Terrascan](https://runterrascan.io/docs/) to apply security controls before Terraform pipeline proceeds for deployment. For CloudFormation, the pipeline also uses [cfn\_nag](https://github.com/stelligent/cfn_nag) and [cfn-lint](https://github.com/aws-cloudformation/cfn-lint). For AWS CDK, the pipeline also uses [cdk-nag](https://github.com/cdklabs/cdk-nag).
+ DPA creates a dedicated Docker image and hosts it on an Amazon ECR repository. These Docker images contain tools, such as the Terraform CLI, AWS CLI, and AWS CDK Toolkit. The pipeline uses these tools during runtime, regardless of which CI/CD solution you choose.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
