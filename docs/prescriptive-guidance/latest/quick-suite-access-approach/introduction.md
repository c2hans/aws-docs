---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/introduction.html
---

# Choosing the right access approach for Amazon Quick
<a name="introduction"></a>

*Henry Kong, Amazon Web Services*

[Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/what-is.html) is a comprehensive, AI-powered business intelligence platform that makes it easy to analyze data, create visualizations, automate workflows, and collaborate across your organization. Access to most AWS services is configured through AWS Identity and Access Management (IAM) and policies. You can configure access to Quick by using IAM, or you can use one of the other available approaches that can be configured directly in the service, such as local users, federation, and directory integration. For most use cases, AWS IAM Identity Center is the recommended way to manage Quick access. This guide describes the available options for provisioning access to Quick so that you can select the appropriate option for your organization. It also discusses use cases and configuration and operations factors that can influence this decision.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for enterprise architects, data architects, and identity and access architects who are making strategic technical decisions about the use of Quick within their organization.

## Objectives
<a name="objectives"></a>

This guide can help you and your organization achieve the following objectives:
+ Understand the different approaches to manage user access to Quick
+ Identify the various access features in Quick that are important for your organization and align best with your processes and use case
+ Make an informed decision about which Quick access approach is the best for your organization

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
