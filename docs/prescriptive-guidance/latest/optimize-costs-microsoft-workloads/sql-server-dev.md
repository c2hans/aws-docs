---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-dev.html
---

# Evaluate SQL Server Developer edition
<a name="sql-server-dev"></a>

## Overview
<a name="sql-server-dev-overview"></a>

[SQL Server Developer edition](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) is a free edition of SQL Server that contains all the features of the Enterprise edition and can be used in any non-production environment. In the cloud, where Microsoft Developer Network (MSDN) licensing can't be used, SQL Server Developer edition is a good way to save on costs without having to provide licenses for development and testing workloads. This is especially true for teams that run large development and testing environments and seek to reduce unnecessary costs.

A production environment is defined as an environment that's accessed by the end users of an application (such as an internet website) and is used for more than gathering feedback or acceptance testing of that application. Other scenarios that constitute production environments include:
+ Environments that connect to a production database
+ Environments that support disaster recovery or backup for a production environment
+ Environments that are used for production at least some of the time, such as a server that is rotated into production during peak periods of activity

For more licensing information, see [Amazon Web Services and Microsoft: Frequently Asked Questions](https://aws.amazon.com/windows/faq/) in the AWS documentation.

## Cost impact
<a name="sql-server-dev-cost-impact"></a>

If you use SQL Server Developer edition for non-production workloads, you can save 100 percent of your current SQL Server licensing costs for development and testing environments.

|
|
| SQL Server version | SQL Server Enterprise edition (2 cores pack) | SQL Server Standard edition (2 cores pack) | SQL Server Developer edition |
| --- |--- |--- |--- |
| 2022 | $15,123 | $3,945 | Free |
| 2019 | $13,748 | $3,586 | Free |

|
|
| Note: Pricing in the preceding table is based on Microsoft's public pricing for [SQL Server 2022](https://www.microsoft.com/en-us/sql-server/sql-server-2022-pricing) and [SQL Server 2019](https://www.microsoft.com/en-us/sql-server/sql-server-2019-pricing). |
| --- |

The following table compares the cost of different SQL Server editions running with 4 vCPUs and using on-demand pricing in the `us-east-2` Region. This applies to scenarios that rely on license-included instances from AWS.

|
|
| EC2 instance | AMI | Compute price | Windows license price | SQL Server license price | Total price |
| --- |--- |--- |--- |--- |--- |
| r5.xlarge | Linux (compute pricing) | $183.96 | – | – | $183.96 |
| r5.xlarge | Linux \+ SQL Server Developer edition | $183.96 | $0 | $0 | $183.96 |
| r5.xlarge | Windows Server (LI) | $183.96 | $134.32 | – | $318.28 |
| r5.xlarge | Windows \+ SQL Server Developer edition | $183.96 | $134.32 | $0 | $318.28 |
| r5.xlarge | Windows \+ SQL Server Web edition (LI) | $183.96 | $134.32 | $49.64 | $367.92 |
| r5.xlarge | Windows \+ SQL Server Standard edition (LI) | $183.96 | $134.32 | $350.4 | $668.68 |
| r5.xlarge | Windows \+ SQL Server Enterprise edition (LI) | $183.96 | $134.32 | $1095 | $1413.28 |

### Cost optimization scenario
<a name="cost-optimization-scenario.d72b15ee-9e9a-5a1e-ab5b-a22b5c8b5d10"></a>

After a data integrity company made a new acquisition, it wanted to migrate the newly acquired workload from its current location on a managed hosting provider to consolidate with its other workloads in the AWS Cloud. Initial pricing showed that the company's SQL Server workload would cost 60 percent more running on AWS than on the current managed service provider. A MACO SME evaluated the estimation and found that the customer was actually paying for SQL Server licenses at the managed hosting provider for their development and testing environments. By switching the non-production workloads to SQL Server Developer edition during the migration, the company reduced their SQL Server licensing by 40 percent.

### SQL Server license included on Amazon EC2
<a name="sql-server-license-included-on-9999999999999999ec2-.a7168993-3043-5859-a712-e5430f70e82b"></a>

If you have SQL Server on EC2 instances that use [license-included AMIs](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-server-on-ec2-amis.html), it's not possible to do a direct conversion from Enterprise edition to Developer edition. The licensing costs for license-included instances are bound to the AMI. Even if SQL Server is uninstalled from within the operating system, the EC2 instance is still charged for licensing costs.

To convert to Developer edition, you must [download SQL Server Developer edition](https://download.microsoft.com/download/c/c/9/cc9c6797-383c-4b24-8920-dc057c1de9d3/SQL2022-SSEI-Dev.exe), install it on a new EC2 instance, and then migrate your databases. You can migrate SQL Server databases between EC2 instances by using a variety of methods. For more information, see [SQL Server database migration methods](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/methods.html) in the *Migrating Microsoft SQL Server databases to the AWS Cloud* guide. You can also use the [Automated SQL Server Developer solution](https://aws.amazon.com/blogs/modernizing-with-aws/automating-sql-server-developer-deployments/) to prep the new instance that you plan to migrate to.

### SQL Server BYOL on Amazon EC2
<a name="sql-server-byol-on-9999999999999999ec2-.ee6268e7-a292-54b4-9dfa-44dc551f5f8b"></a>

If you have SQL Server instances that use a BYOL, you can choose from the following in-place conversion or side-by-side downgrade options:
+ Download [SQL Server Developer edition](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) from the Microsoft website. For manual or automated installation instructions, see the [Automating SQL Server Developer deployments](https://aws.amazon.com/blogs/modernizing-with-aws/automating-sql-server-developer-deployments/) post on the AWS Blog.
+ Use [SQL Server native backup and restore](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver16) to migrate databases or detach/attach databases from one SQL instance to another.
+ Use an [automation tool](https://github.com/aws-samples/ssm-automation-deploy-sql-developer) for bulk deployments.

|
|
| Note: SQL Server Developer edition is for non-production environments only.  |
| --- |

## Additional resources
<a name="additional-resources"></a>
+ [Automating SQL Server Developer deployments for deploying SQL Server Developer Edition on EC2](https://aws.amazon.com/blogs/modernizing-with-aws/automating-sql-server-developer-deployments/) (AWS Blog)
+ [SQL 2022 pricing](https://www.microsoft.com/en-us/sql-server/sql-server-2022-pricing) (Microsoft)
+ [SQL 2019 pricing](https://www.microsoft.com/en-us/sql-server/sql-server-2019-pricing) (Microsoft)
+ [Licensing options](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-server-on-ec2-licensing-options.html) (SQL Server on Amazon EC2)
+ [AWS Pricing Calculator](https://calculator.aws/#/addService/ec2-enhancement) (SQL Server on Amazon EC2 documentation)
+ [Microsoft SQL Server 2019 Licensing guide](https://download.microsoft.com/download/e/2/9/e29a9331-965d-4faa-bd2e-7c1db7cd8348/SQL_Server_2019_Licensing_guide.pdf) (download from Microsoft)
+ [SQL Server 2022 Developer edition](https://download.microsoft.com/download/c/c/9/cc9c6797-383c-4b24-8920-dc057c1de9d3/SQL2022-SSEI-Dev.exe) (download from Microsoft)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
