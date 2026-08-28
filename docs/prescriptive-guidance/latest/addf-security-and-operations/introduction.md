---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/addf-security-and-operations/introduction.html
---

# Autonomous Driving Data Framework (ADDF) security and operations guide
<a name="introduction"></a>

*Andreas Falkenberg, Srinivas Reddy Cheruku, Torsten Reitemeyer, and Junjie Tang, Amazon Web Services*

Autonomous Driving Data Framework (ADDF) is an open-source project designed to provide reusable, modular code artifacts for automotive teams who want to implement common tasks for advanced driver-assistance systems (ADAS), such as configuring centralized data storage, data processing pipelines, visualization mechanisms, search interfaces, simulation workloads, analytics interfaces, and prebuilt dashboards. Using ADDF, you can share, modify, or create fully customizable modules that reduce the amount of effort required to create and deploy these solutions.

This guide is intended to help you understand best practices for securely deploying and operating ADDF in the AWS Cloud. It discusses the following topics:
+ [ADDF architecture and terminology](addf-architecture-terminology.md) – Review the general architecture, workflows, and important terms.
+ [Shared responsibility model](shared-responsibility-model.md) – Understand your role and the role of AWS in securing your ADDF deployment and cloud resources.
+ [ADDF security review process](addf-security-review-process.md) – Because ADDF is an open-source project, review how AWS and contributors complete security reviews.
+ [Built-in security features](built-in-security-features.md) – Review how security best practices and features are built into the ADDF open-source project and its deployment framework.
+ [Secure setup and operation](secure-setup-and-operation.md) – Learn how to deploy and operate ADDF in the AWS Cloud.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for Development Operations (DevOps) teams, infrastructure engineers, administrators, IT security staff, and incident response teams who are tasked with assessing, deploying, customizing, and operating ADDF. You can apply the recommendations in this guide for proof-of-concept or production environments.

This guide assumes you have no prior knowledge of ADDF. However, we recommend that you read the [ADDF readme](https://github.com/awslabs/autonomous-driving-data-framework#readme) (GitHub) before proceeding.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

This guide is designed to help you more confidently and securely set up and operate ADDF in development and production environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
