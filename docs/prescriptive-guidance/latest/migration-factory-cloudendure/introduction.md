---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/introduction.html
---

# Automating large-scale server migrations with Cloud Migration Factory
<a name="introduction"></a>

*Wally Lu and Shraddha Ghogare, Amazon Web Services*

Many companies today want to migrate their servers to Amazon Web Services (AWS) as quickly as possible. This is not an easy job, especially if you want to migrate thousands of servers in a short period of time, such as 6–12 months.

Large-scale migrations present a few challenges:
+ Integrating multiple tools is difficult. There are many tools that support migration, such as discovery tools, migration tools, and configuration management database (CMDB) tools. These tools must be connected so that data flows from one tool to another. However, different tools use different data formats, and that makes integration difficult. A migration is more likely to be successful if there is a way to integrate all the tools.
+ Manual processes are slow and hard to scale. Migrations involve many small tasks, and each task takes a few minutes to complete. A migration is faster when these tasks are automated.

Cloud Migration Factory was designed to solve these problems for migrations that require rehosting (lift and shift). [AWS Transform MGN](https://aws.amazon.com/application-migration-service/) simplifies, expedites, and reduces the cost of cloud migration by offering a highly automated lift-and-shift solution. Cloud Migration Factory is an orchestration platform for rehosting servers to AWS at scale. It helps customers with their medium-scale to large-scale migrations by automating manual processes, which are often slow or complex to scale. Thousands of servers have been migrated to AWS using Cloud Migration Factory. For example, AWScustomers used Cloud Migration Factory to migrate 1,200 servers in 5 months, and were able to cut over more than 600 servers in a single cutover window.

This guide describes the Cloud Migration Factory process for rehosting servers at scale, for migration architects, program managers, and technical leads. For more information about migration factories, see [Mobilize your organization to accelerate large-scale migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/migrations-phase.html) on the AWS Prescriptive Guidance website.

|
|
| How to get access to Cloud Migration FactoryCloud Migration Factory is available to all AWS customers and partners. To use Cloud Migration Factory, see the [AWS Cloud Migration Factory](https://aws.amazon.com/solutions/implementations/cloud-migration-factory-on-aws/) on the AWS Solutions website. The source code is available in a [GitHub repository](https://github.com/awslabs/aws-cloudendure-migration-factory-solution). If you have any questions, email AWS Professional Services at *migration-factory-support@amazon.com*. |
| --- |

If you want to get hands-on experience before using Cloud Migration Factory for your production migration, email us at *migration-immersion-day@amazon.com* to arrange a [migration immersion day](https://migration-immersionday.workshop.aws/en).
