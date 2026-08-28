---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/infrastructure-as-code.html
---

# Infrastructure as code
<a name="infrastructure-as-code"></a>

As serverless AI systems scale, the complexity of provisioning, managing, and evolving cloud infrastructure increases rapidly. Manual setup of APIs, AWS Lambda functions, Amazon Bedrock agents, IAM roles, and state machines is error-prone, non-repeatable, and not compliant at scale.

Infrastructure as code (IaC) is the foundational discipline that ensures all infrastructure components are:
+ Version-controlled
+ Repeatable across environments
+ Auditable and reviewable
+ Modular and testable

By adopting IaC, enterprises gain not only automation, but governance, speed, and resilience in deploying and operating serverless AI workloads.

## AWS services for IaC deployment of serverless AI on AWS
<a name="9999999999999999aws-services--for-iac-deployment-of-serverless-ai-on-9999999999999999aws-.666c43ae-a55d-5892-8070-fde7ffdc07da"></a>

The following AWS services and third-party tools support IaC deployment of serverless AI on AWS. AWS CloudFormation, AWS CDK, and AWS SAM provide native AWS capabilities for infrastructure deployment. HashiCorp Terraform offers a popular third-party solution. Each has distinct advantages and is suited to different team requirements and use cases.

### CloudFormation
<a name="9999999999999999cfn-.22206551-da4e-5beb-b6e6-d5f7b056393a"></a>

[CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) is a native, declarative IaC service that lets you define infrastructure as structured JSON or YAML templates.

Strengths of CloudFormation include the following:
+ Highly stable and mature, widely supported across all AWS services
+ Integrated rollback and drift detection
+ Managed stacks and change sets allow safer deployments
+ Directly supported in the AWS Management Console for visual tracking

CloudFormation is ideal for the following requirements:
+ Teams that need explicit, auditable templates with fine-grained control
+ Regulatory environments where code traceability is mandatory
+ Environments where DevOps pipelines enforce strict promotion workflows

### AWS CDK
<a name="9999999999999999cdk-.e7e911a0-43da-5429-a29e-a6fab197f488"></a>

The [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) is an open-source framework. With the AWS CDK, you can define AWS infrastructure by using familiar programming languages like TypeScript, Python, Java, or C\#.

Strengths of the AWS CDK include the following:
+ Imperative and declarative hybrid that supports the use of loops, conditionals, and abstractions in code
+ Availability of many constructs and reusable patterns
+ Easier for developers to adopt (code-first mindset)
+ Enables multi-environment deployments with environment-aware stacks

The AWS CDK is ideal for the following requirements:
+ Teams with strong software engineering skills
+ Use cases that need dynamic infrastructure generation
+ Projects involving construct reuse, customization, and rapid iteration

### AWS SAM
<a name="9999999999999999sam-.7cddfb45-0bcf-58a0-b90e-d912967b24de"></a>

[AWS Serverless Application Model (AWS SAM)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) is a CloudFormation extension that's optimized for defining serverless applications such as [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html), and [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html).

Strengths of AWS SAM include the following:
+ Minimal syntax that's ideal for pipelines that are based in Lambda
+ Native support for local emulation and debugging
+ Integrated command line interface (CLI) that simplifies deploy, test, and package workflows

AWS SAM is ideal for the following requirements:
+ Small- to mid-sized projects that focus primarily on Lambda, API Gateway, and Amazon Bedrock
+ Teams that want simple YAML-based templates with built-in continuous integration and continuous deployment (CI/CD) support

### Terraform
<a name="terraform.9ca10465-592b-535d-b731-799401d228a2"></a>

[HashiCorp Terraform](https://developer.hashicorp.com/terraform/intro) is an IaC tool that helps you use code to provision and manage cloud infrastructure and resources.

Strengths of Terraform include the following:
+ Broad provider ecosystem beyond AWS that's ideal for multicloud scenarios
+ Rich state management and dependency graph resolution
+ Popular in enterprises that have a DevOps-first culture and use GitOps workflows

Terraform is ideal for the following requirements:
+ Teams with an existing Terraform investment
+ Multicloud deployments or AWS native services that are integrated with software as a service (SaaS) tools
+ Organizations that standardize on Terraform for consistency across teams

## Best practices for IaC in serverless AI projects
<a name="best-practices-for-iac-in-serverless-ai-projects.c405c743-3f3d-5c65-a4b7-6295868caee4"></a>

When implementing IaC in serverless AI projects, consider the following best practices and their importance:
+ **Version control everything** – Ensures reproducibility, enables rollback, and supports change approval through Git.
+ **Use environment-specific stacks** – Cleanly separates development, test, and production deployments. Prevents accidental cross-contamination.
+ **Modularize infrastructure** – Encourages reuse, speeds up onboarding, and reduces the blast radius of changes (for example, one module for [Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) and another module for EventBridge rules).
+ **Use parameterization and tags** – Enables dynamic stack behavior and cost tracking. Improves observability in billing and [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).
+ **Integrate IaC into CI/CD** – Automates infrastructure updates during deployments, helping to ensure that the app and infrastructure stay in sync.
+ **Apply schema validation and linting** – Prevents deployment errors and enforces consistency across team contributions.
+ **Implement drift detection and audit trails** – Helps to ensure that infrastructure matches expected definitions and simplifies compliance reviews (for example, by using CloudFormation [drift detection ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html)or Terraform state validation).

## Example: Versioned deployment of a serverless AI assistant
<a name="example--versioned-deployment-of-a-serverless-ai-assistant.354f0362-7d73-5209-bcb7-c229a5688622"></a>

Using AWS CDK or CloudFormation, a support assistant powered by Amazon Bedrock might include the following:
+ An API Gateway endpoint
+ An Amazon Bedrock agent with three tools that are based in Lambda
+ A knowledge base that references Amazon S3 documents
+ A Step Functions workflow for fallback/error-handling
+ Logging and observability infrastructure, such as CloudWatch or [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)

With IaC, all these elements are defined in a repository, promoted through CI/CD, and version-tagged with every deployment. This approach provides full traceability, auditability, and rollback if needed.

## Summary of IaC deployment of serverless AI
<a name="summary-of-iac-deployment-of-serverless-ai.d8d9316b-e77c-5ef2-98f2-0a7f322ff74d"></a>

IaC for enterprise-grade serverless AI systems is the foundation that transforms experimentation into production, giving organizations confidence that their infrastructure is:
+ Consistent across development, test, and production environments
+ Governable through policy, review, and audit mechanisms
+ Scalable with the same pace as AI adoption

Whether using AWS CDK for dynamic constructs, CloudFormation for audit-aligned deployments, or AWS SAM for focused pipelines, IaC is the control plane of the intelligent, event-driven cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
