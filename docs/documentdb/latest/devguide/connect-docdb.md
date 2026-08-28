---
source_url: https://docs.aws.amazon.com/documentdb/latest/devguide/connect-docdb.html
---

# Connect to Amazon DocumentDB
<a name="connect-docdb"></a>

Amazon DocumentDB provides multiple connection options, including programmatic connections using MongoDB drivers, connecting from outside a VPC through SSH tunneling or AWS VPN, and popular tools like Studio 3T and DataGrip. The service supports replica set connections for high availability. For analytics and reporting, you can connect using JDBC or ODBC drivers. EC2 instances in the same VPC can connect directly to DocumentDB clusters. All connections require TLS and proper AWS credentials/authentication.

**Topics**
+ [Connecting programmatically](connect_programmatically.md)
+ [Connecting from outside an Amazon VPC](connect-from-outside-a-vpc.md)
+ [Connecting as a replica set](connect-to-replica-set.md)
+ [Connect using Studio 3T](studio3t.md)
+ [Connect using DataGrip](data-grip-connect.md)
+ [Connect using Amazon EC2](connect-ec2.md)
+ [Connect using the JDBC driver](connect-jdbc.md)
+ [Connect using the ODBC driver](connect-odbc.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
