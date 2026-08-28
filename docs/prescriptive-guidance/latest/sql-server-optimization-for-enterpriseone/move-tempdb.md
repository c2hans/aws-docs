---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/move-tempdb.html
---

# Move tempdb to instance storage
<a name="move-tempdb"></a>

When RCSI is enabled, a significant IOPS and throughput load can be created in `tempdb `to maintain versions of records during transactions. Because of this load, you should move `tempdb `to NVMe instance storage. For information about how to move `tempdb `to the instance store, follow the steps in the [Best practices for deploying SQL Server on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-best-practices/tempdb.html) guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
