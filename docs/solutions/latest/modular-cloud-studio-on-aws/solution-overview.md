---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/solution-overview.html
---

# Overview
<a name="solution-overview"></a>

Modular Cloud Studio (MCS) on AWS is a solution that helps studios and production teams to build secure, scalable, and highly customizable content production studios in the AWS Cloud. You can build a tailored, cloud-based production environment within hours without extensive cloud expertise or costly upfront investments. MCS simplifies the setup by providing you with integration choices and automating deployment. Its modular framework presents options to launch remote workstations, storage, and other modules with Amazon Web Services (AWS) services and AWS Partner production systems. You can securely expand studio access to global talent, scale resources to meet project demands, and add capabilities with additional modules from the AWS Marketplace, where you can find software that runs on AWS. This way, your teams can focus on creative innovation, not technical logistics.

Media companies and entertainment studios face the growing need to become more flexible, responsive businesses that can pursue creative opportunities as they arise. Using the cloud can help these companies to:
+ Accommodate new projects without complex planning and capital expenditure
+ Access remote talent and vendors globally using distributed workflows

Some organizations might have concerns about migrating to the [cloud](https://aws.amazon.com/what-is-cloud-computing/). MCS helps mitigate many of these concerns:
+ MCS automates and simplifies the process of setting up, integrating, and configuring regional environments for geographically diverse teams.
+ MCS provides the capability to use Third-Party Modules and custom modules, so that you can keep using the products you’re already familiar with.
+ MCS deploys within 5-10 minutes, and you can then deploy the modules within hours.

This guide will help you build and configure a cloud studio on AWS with MCS. Read this guide for the reference architecture, components, planning considerations, and steps involved in deploying and configuring your cloud studio.

The intended audience for using this solution’s features and capabilities in their environment includes system administrators, solution architects, and cloud professionals who are responsible for content production workloads and studio technology.

Use this navigation table to quickly find answers to these questions:

|  **If you want to …​**  |  **Read …​**  |
| --- | --- |
| Know the cost for running this solution.<br />The estimated cost for running this solution varies based on your deployment configuration and use.<br />For example, the estimated cost in the US East (N. Virginia) Region is USD $591.55 per month for AWS resources when deploying internal MCS modules in the hub Region. This cost doesn’t include modules containing AWS Independent Software Vendor (ISV) software. |  [Cost](cost.md)  |
| Understand the security considerations for this solution.<br />The solution deploys AWS resources within a virtual private cloud (VPC) with limited access. The solution automatically creates a default administrator user in an [Amazon Cognito user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html), which is a user directory for web and mobile app authentication and authorization. |  [Security](aws-well-architected-design-considerations.md#security)  |
| Know how to plan for quotas for this solution.<br />Make sure you have sufficient [quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) for each of the services implemented in this solution, including [AWS CloudFormation](https://aws.amazon.com/cloudformation/) quotas that you should be aware when launching the stack. CloudFormation launches this solution from a template and takes care of provisioning and configuring the necessary AWS resources for you. |  [Quotas](quotas.md)  |
| Know which AWS Regions support this solution.<br />Individual MCS modules might be available in different AWS Regions. An [AWS Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) is a physical location in the world where AWS has clustered data centers. Each group of logical data centers is called an Availability Zone. Each AWS Region consists of a minimum of three, isolated, and physically separate Availability Zones within a geographic area. |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
| View or download the CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution. [Templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) are declarative configuration files that specify the resources you want to provision in your CloudFormation stacks. |  [AWS CloudFormation template](aws-cloudformation-template.md)  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
