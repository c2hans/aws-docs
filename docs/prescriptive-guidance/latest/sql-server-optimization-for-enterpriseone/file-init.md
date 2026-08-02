---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/file-init.html
---

# Enable instant file initialization
<a name="file-init"></a>

When a database files grows, it fills the new disk space with zeros (`0x0`) by default. This creates significant system I/O and can degrade system performance. Instant file initialization prevents zeroing operations on the allocated disk space. To enable instant file initialization, follow the steps in the [Best practices for deploying SQL Server on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-best-practices/instance-file.html) guide.
