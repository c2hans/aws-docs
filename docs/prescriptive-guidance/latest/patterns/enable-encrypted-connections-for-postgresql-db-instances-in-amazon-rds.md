---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds.html
---

# Enable encrypted connections for PostgreSQL DB instances in Amazon RDS
<a name="enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds"></a>

*Rohit Kapoor, Amazon Web Services*

## Summary
<a name="enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds-summary"></a>

Amazon Relational Database Service (Amazon RDS) supports SSL encryption for PostgreSQL DB instances. Using SSL, you can encrypt a PostgreSQL connection between your applications and your Amazon RDS for PostgreSQL DB instances. By default, Amazon RDS for PostgreSQL uses SSL/TLS and expects all clients to connect by using SSL/TLS encryption. Amazon RDS for PostgreSQL supports TLS versions 1.1 and 1.2.

This pattern describes how you can enable encrypted connections for an Amazon RDS for PostgreSQL DB instance. You can use the same process to enable encrypted connections for Amazon Aurora PostgreSQL-Compatible Edition.

## Prerequisites and limitations
<a name="enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds-prereqs"></a>
+ An active AWS account
+ An [Amazon RDS for PostgreSQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_RDS_Configuring.html)
+ An [SSL bundle](https://www.postgresql.org/docs/current/ssl-tcp.html)

## Architecture
<a name="enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds-architecture"></a>

![Enabling encrypted connections for PostgreSQL DB instances in Amazon RDS](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4f87c6a3-b4ff-4248-96d3-a4a498659735/images/ccc5c880-1191-4c12-a255-6908b96b96a5.png)

## Tools
<a name="enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds-tools"></a>
+ [pgAdmin](https://www.pgadmin.org/) is an open-source administration and development platform for PostgreSQL. You can use pgAdmin on Linux, Unix, macOS, and Windows to manage your database objects in PostgreSQL 10 and later.
+ [PostgreSQL editors](https://wiki.postgresql.org/wiki/PostgreSQL_Clients) provide a more user-friendly interface to help you create, develop, and run queries, and to edit code according to your requirements.

## Best practices
<a name="enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds-best-practices"></a>
+ Monitor unsecure database connections.
+ Audit database access rights.
+ Make sure that backups and snapshots are encrypted at rest.
+ Monitor database access.
+ Avoid unrestricted access groups.
+ Enhance your notifications with [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html).
+ Monitor policy adherence regularly.

## Epics
<a name="enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds-epics"></a>

### Download a trusted certificate and import it into your trust store
<a name="download-a-trusted-certificate-and-import-it-into-your-trust-store"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Load a trusted certificate to your computer. | To add certificates to the Trusted Root Certification Authorities store for your computer, follow these steps. (These instructions use Window Server as a example.)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds.html) | DevOps engineer, Migration engineer, DBA |

### Force SSL connections
<a name="force-ssl-connections"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a parameter group and set the rds.force\_ssl parameter. | If the PostgreSQL DB instance has a custom parameter group, edit the parameter group and change `rds.force_ssl` to 1.<br />If the DB instance uses the default parameter group that doesn’t have `rds.force_ssl` enabled, create a new parameter group. You can modify the new parameter group by using the Amazon RDS API or manually as in the following instructions.<br />To create a new parameter group:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds.html)<br />To associate the parameter group with your PostgreSQL DB instance:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds.html)<br />For more information, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithDBInstanceParamGroups.html). | DevOps engineer, Migration engineer, DBA |
| Force SSL connections. | Connect to the Amazon RDS for PostgreSQL DB instance. Connection attempts that don’t use SSL are rejected with an error message. For more information, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.SSL.html#PostgreSQL.Concepts.General.SSL.Requiring). | DevOps engineer, Migration engineer, DBA |

### Install SSL extension
<a name="install-ssl-extension"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the SSL extension. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds.html)For more information, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.SSL.html). | DevOps engineer, Migration engineer, DBA |

### Configure your PostgreSQL client for SSL
<a name="configure-your-postgresql-client-for-ssl"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure a client for SSL. | By using SSL, you can start the PostgreSQL server with support for encrypted connections that use TLS protocols. The server listens for both standard and SSL connections on the same TCP port, and negotiates with any connecting client on whether to use SSL. By default, this is a client option.<br />If you’re using the psql client:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds.html)<br />For other PostgreSQL clients:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds.html)<br />Review the following pages for these clients:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds.html) | DevOps engineer, Migration engineer, DBA |

## Troubleshooting
<a name="enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Cannot download the SSL certificate. | Check your connection to the website, and retry downloading the certificate to your local computer. |

## Related resources
<a name="enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds-resources"></a>
+ [Amazon RDS for PostgreSQL documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)
+ [Using SSL with a PostgreSQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.SSL.html) (Amazon RDS documentation)
+ [Secure TCP/IP Connections with SSL](https://www.postgresql.org/docs/9.1/ssl-tcp.html) (PostgreSQL documentation)
+ [Using SSL](https://jdbc.postgresql.org/documentation/ssl/) (JDBC documentation)
