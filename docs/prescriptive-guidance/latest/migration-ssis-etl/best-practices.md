---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-ssis-etl/best-practices.html
---

# Best practices
<a name="best-practices"></a>

Follow these general best practices when migrating your SSIS jobs to AWS:
+ If you're migrating your databases to an AWS managed service such as Amazon Relational Database Service (Amazon RDS), descope [maintenance tasks](https://docs.microsoft.com/en-us/sql/integration-services/control-flow/integration-services-tasks) (such as backup, restore, update statistics, or check database integrity) that are not applicable or managed by AWS.
+ Build reusable [scripts](https://docs.aws.amazon.com/glue/latest/dg/console-custom-created.html) and methods to standardize development and reduce effort.
+ Always test migrated jobs on infrastructure and data volumes that match production resources.
+ SSIS packages are in XML format. Build XML parser utilities to automate migration activities where possible. The following example shows an SSIS package in XML format.
![SSIS package in XML format](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-ssis-etl/images/guide-img/ae5b08b7-f641-4524-9650-6ac5a0f71dd9/images/911c221a-c9f5-4a6a-a596-0f57176ac2c7.png)

The following illustration shows a sample XML parser.

![Sample XML parser for SSIS jobs](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-ssis-etl/images/guide-img/ae5b08b7-f641-4524-9650-6ac5a0f71dd9/images/fc6be370-c6b5-4a87-805c-cc06d9f7c103.png)

+ Use checksums and hash values to test correctness and completeness.
+ If you're building custom libraries, implement threading to run tasks in parallel. This improves job performance.
+ Decommission the existing environment only after all jobs are stable on AWS for a period of time.
+ Use Amazon CloudWatch for logging, to reduce logging customization efforts.
+ Use Amazon Simple Notification Service (Amazon SNS) to replace custom tasks for sending notifications. Use Amazon Simple Email Service (Amazon SES) to replace custom email tasks.
