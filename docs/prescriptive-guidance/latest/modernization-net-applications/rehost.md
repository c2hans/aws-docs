---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications/rehost.html
---

# Rehosting
<a name="rehost"></a>

Rehosting (lift and shift) is the process of migrating your on-premises application to the cloud without modifying it. This strategy is used mostly to migrate large-scale applications to satisfy specific business goals, such as launching a product in an accelerated timeline or leaving an on-premises data center. The applications are rehosted on Amazon Elastic Compute Cloud (Amazon EC2) Windows instances that meet the requirements of the applications you migrate.

## Use cases
<a name="rehost-use-cases"></a>

This migration strategy is useful in any of the following scenarios:
+ The legacy .NET application must run as a native Windows application.
+ Time and resources to modernize the application are not available.
+ The legacy .NET application is a commercial off-the-shelf (COTS) application.

## Advantages
<a name="rehost-pros"></a>

Rehosting provides the following benefits, when compared with on-premises .NET applications:
+ Minimum effort, because it requires no code or architectural changes
+ Reduced cost
+ Better compliance and security, because it uses the AWS infrastructure and security best practices

## Disadvantages
<a name="rehost-cons"></a>
+ Doesn't take full advantage of the performance, scalability, and resiliency options of the AWS Cloud
+ Difficult to integrate with state-of-the-art cloud services

## AWS services
<a name="rehost-services"></a>
+ [Amazon EC2](https://aws.amazon.com/ec2)
+ [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)
+ [AWS Application Migration Service](https://aws.amazon.com/application-migration-service/)

## Tools
<a name="rehost-tools"></a>

|
|
| Tool |   | Purpose | Resource |
| --- |--- |--- |--- |
| Windows Web Application Migration Assistant |   | This tool is an interactive PowerShell script that migrates entire websites and their configurations to Elastic Beanstalk. | [Migrating ASP.NET applications to Elastic Beanstalk](https://aws.amazon.com/blogs/devops/migrating-asp-net-applications-to-elastic-beanstalk-with-windows-web-application-migration-assistant/) (AWS blog post) |

## Deployment decisions
<a name="rehost-deployment"></a>

You can choose from two deployment options:
+ If you want complete control over the configuration of your compute environment, including memory and storage settings, and control over operating system patches: migrate your .NET application to Amazon EC2.
+ If you don't require full control over the infrastructure: use Elastic Beanstalk. Elastic Beanstalk automatically sets up a managed environment for your application.

![Rehosting legacy .NET apps on AWS](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications/images/guide-img/e6435ff7-ff5b-43b9-841d-7a90ca834432/images/8fa53bdf-393e-4a2c-9abd-d6b3dd2f1e0b.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
