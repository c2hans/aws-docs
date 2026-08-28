---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-microsoft-workloads-aws/introduction.html
---

# Options, tools, and best practices for migrating Microsoft workloads to AWS
<a name="introduction"></a>

*Dror Helper, Yogi Barot, Rich Benoit, Phil Ekins, Saleha Haider, Rob Higareda, Siavash Irani, Daniel Maldonado, Christine Megit, Siddharth Mehta, Mani Pachnanda, and Reut Almog Talmi, Amazon Web Services*

Organizations have been migrating and running their Microsoft workloads on AWS for over a decade—longer than any other cloud provider. Based on the knowledge and expertise that AWS has gained from migration and modernization efforts over the years, this guide is designed to streamline the migration of your Microsoft workloads to the AWS Cloud. You can use this guide to plan and implement all phases of your Windows migration. This guide is applicable to a variety of migration use cases, including the following:
+ You're starting a Windows migration as part of a digital transformation and modernization journey in your organization.
+ The lease on the data center where you run your Microsoft workloads is nearing expiration.
+ You have a variety of Windows applications with varying availability requirements, but you don't have the resources to deploy your workloads across geographically distributed locations.

In this guide, you learn about a variety of AWS tools that can help streamline your migration journey, such as AWS Transform, AWS Transform MGN, and more. To align with AWS best practices, this guide follows the [three-phase AWS migration process](https://aws.amazon.com/migrate-modernize-build/cloud-migration/how-to-migrate/): assess, mobilize, and migrate and modernize. This process is based on a time-tested migration framework that can help you structure and streamline your Windows migration. In the assess phase, you evaluate your readiness for operating in the cloud. In the mobilize phase, you draft migration plans and close readiness gaps identified in the assess phase. Then, you start to migrate your workloads in the migrate and modernize phase by using a combination of automation tools and templates to systematically migrate your workloads and meet your business requirements.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for IT architects, migration leads, technical leads, AWS Partner teams, and other roles responsible for the following:
+ Migrating Microsoft workloads from a data center to the AWS Cloud
+ Managing a Windows environment in the AWS Cloud

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

This guide can help you and your organization achieve the following objectives:

1. Learn about the strategies, programs, and services available for migrating Microsoft workloads to AWS.

1. Understand the AWS migration paths for specific Microsoft workloads, such as Active Directory, Windows File Server, SQL Server, and .NET workloads.

1. Run your Microsoft workloads on AWS while meeting your security, availability, and reliability requirements.

1. Familiarize yourself with licensing best practices for running Microsoft workloads on AWS.

## Attachments
<a name="attachments-6418e52b-6b3a-4cae-8215-281ccb6e07b5"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
