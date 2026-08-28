---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-db2-database-on-aws/introduction.html
---

# Migrating a Db2 for LUW database to Amazon EC2
<a name="introduction"></a>

*Feng Cai, Venkatesan Govindan, and Shunan Xiang, Amazon Web Services*

[Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) now supports the [IBM Db2 database engine](https://www.ibm.com/products/db2).

[Amazon RDS for Db2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Db2.html) automates time-consuming database administration tasks, such as provisioning, backups, software patching, and monitoring, to free up time to innovate and drive business value. However, Amazon RDS for Db2 doesn't provide host access or `SYSADM` access, and it has other limitations for users who want to control the architecture. If you need host access, you can run Db2 for LUW (Linux, UNIX, and Windows) on [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/).

One of the biggest migration challenges that customers face is moving on-premises Db2 LUW workloads that are running on a big-endian platform such as [IBM AIX](https://www.ibm.com/products/aix?utm_content=SRCWW&p1=Search&p4=43700050386406196&p5=e&gclid=CjwKCAiA9qKbBhAzEiwAS4yeDYixQiVVWOfFuAmW12DoDSaELhAwZNJZ7qGWwa4lajG673OSHxjAZhoCqwEQAvD_BwE&gclsrc=aw.ds) to Amazon EC2, which is a little-endian platform. Currently, there is no easy way to convert Db2 data from big endian to little endian without unloading and reloading.

Considering these challenges, this guide covers the pros and cons of tested options for both big-endian and little-endian migration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
