---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-linked-servers.html
---

# Migrate an on-premises Microsoft SQL Server database to Amazon RDS for SQL Server using linked servers
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-linked-servers"></a>

*Kevin Yung, Viqash Adwani, and Vishal Singh, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-linked-servers-summary"></a>

Linked servers enable Microsoft SQL Server to run SQL statements on other instances of database servers. This pattern describes how you can migrate your on-premises Microsoft SQL Server database to Amazon Relational Database Service (Amazon RDS) for Microsoft SQL Server to achieve lower cost and higher availability. Currently, Amazon RDS for Microsoft SQL Server doesn't support connections outside an Amazon Virtual Private Cloud (Amazon VPC) network.

You can use this pattern to achieve the following objectives:
+ To migrate Microsoft SQL Server to Amazon RDS for Microsoft SQL Server without breaking linked server capabilities.
+ To prioritize and migrate linked Microsoft SQL Server in different waves.

## Prerequisites and limitations
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-linked-servers-prerequisites-and-limitations"></a>

**Prerequisites**
+ Check whether [Microsoft SQL Server on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html) supports the features you require.
+ Make sure that you can use either [Amazon RDS for Microsoft SQL Server with default collations or collations set over database levels](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.Collation.html).

## Architecture
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-linked-servers-architecture"></a>

**Source technology stack**
+ On-premises databases (Microsoft SQL Server)

 **Target technology stack**
+ Amazon RDS for SQL Server

**Source state architecture**

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/95234758-cb8b-46e5-afd2-3d4aaf6ed668/images/776b453a-7fa0-43fd-b1ca-fb9e5cc21820.png)

**Target state architecture**

In the target state, you migrate Microsoft SQL Server to Amazon RDS for Microsoft SQL Server by using linked servers. This architecture uses a Network Load Balancer to proxy the traffic from Amazon RDS for Microsoft SQL Server to on-premises servers running Microsoft SQL Server. The following diagram shows the reverse proxy capability for the Network Load Balancer.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/95234758-cb8b-46e5-afd2-3d4aaf6ed668/images/6bdbdfbf-b048-4fbd-acef-0aeb826edb50.png)

## Tools
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-linked-servers-tools"></a>
+ AWS CloudFormation
+ Network Load Balancer
+ Amazon RDS for SQL Server in multiple Availability Zones (Multi-AZs)
+ AWS Database Migration Service (AWS DMS)

## Epics
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-linked-servers-epics"></a>

### Create a landing zone VPC
<a name="create-a-landing-zone-vpc"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the CIDR allocation. |  | AWS SysAdmin |
| Create a virtual private cloud (VPC). |  | AWS SysAdmin |
| Create the VPC subnets. |  | AWS SysAdmin |
| Create the subnet access control lists (ACLs). |  | AWS SysAdmin |
| Create the subnet route tables. |  | AWS SysAdmin |
| Create a connection with AWS Direct Connect or AWS Virtual Private Network (VPN). |  | AWS SysAdmin |

### Migrate the database to Amazon RDS
<a name="migrate-the-database-to-amazon-rds"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon RDS for Microsoft SQL Server DB instance. |  | AWS SysAdmin |
| Create an AWS DMS replication instance. |  | AWS SysAdmin |
| Create the source and target database endpoints in AWS DMS. |  | AWS SysAdmin |
| Create the migration task and set continuous replication to ON after a full load. |  | AWS SysAdmin |
| Request a firewall change to allow Amazon RDS for Microsoft SQL Server to access the on-premises SQL Server databases. |  | AWS SysAdmin |
| Create a Network Load Balancer. |  | AWS SysAdmin |
| Create a target group that targets the database servers in your data center | We recommend that you use hostnames in the target setup to incorporate data center (DC) failover events. | AWS SysAdmin |
| Run the SQL statement for linked server setup. | Run the SQL statements for adding a linked server by using the Microsoft SQL management tool against the Amazon RDS for Microsoft SQL Server DB instance. In the SQL statement, set @datasrc to use the Network Load Balancer hostname. Add linked server login credentials by using the Microsoft SQL management tool against the Amazon RDS for Microsoft SQL Server DB instance. | AWS SysAdmin |
| Test and validate the SQL Server functions. |  | AWS SysAdmin |
| Create a cutover. |  | AWS SysAdmin |

## Related resources
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-linked-servers-related-resources"></a>
+ [Common Management Tasks for Microsoft SQL Server on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General)
+ [Collations and Character Sets for Microsoft SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.Collation.html)
+ [Network Load Balancer documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
+ [Implement Linked Servers with Amazon RDS for Microsoft SQL Server (blog post)](https://aws.amazon.com/blogs/database/implement-linked-servers-with-amazon-rds-for-microsoft-sql-server/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
