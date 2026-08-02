---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/move-tempdb.html
---

# Move tempdb to instance storage
<a name="move-tempdb"></a>

When RCSI is enabled, a significant IOPS and throughput load can be created in `tempdb `to maintain versions of records during transactions. Because of this load, you should move `tempdb `to NVMe instance storage. For information about how to move `tempdb `to the instance store, follow the steps in the [Best practices for deploying SQL Server on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-best-practices/tempdb.html) guide.
