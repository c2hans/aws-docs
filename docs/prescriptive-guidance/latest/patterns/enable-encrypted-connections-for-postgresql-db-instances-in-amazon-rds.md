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

![Enabling encrypted connections for PostgreSQL DB instances in Amazon RDS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4f87c6a3-b4ff-4248-96d3-a4a498659735/images/ccc5c880-1191-4c12-a255-6908b96b96a5.png)

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
| Load a trusted certificate to your computer. | To add certificates to the Trusted Root Certification Authorities store for your computer, follow these steps. (These instructions use Window Server as a example.)1. In Windows Server, choose **Start**, **Run**, and then type **mmc**.<br />2. In the console, choose **File**, **Add/Remove Snap-in**.<br />3. Under **Available snap-ins**, choose **Certificates**, and then choose **Add**.<br />4. Under **This snap-in will always manage certificates for**, choose **Computer account**, **Next**.<br />5. Choose **Local computer**, **Finish**.<br />6. If you have no more snap-ins to add to the console, choose **OK**.<br />7. In the console tree, double-click **Certificates**.<br />8. Right-click **Trusted Root Certification Authorities**.<br />9. Choose **All Tasks**, **Import** to import the downloaded certificates.<br />10. Follow the steps in the Certificate Import Wizard. | DevOps engineer, Migration engineer, DBA |

### Force SSL connections
<a name="force-ssl-connections"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a parameter group and set the rds.force\_ssl parameter. | If the PostgreSQL DB instance has a custom parameter group, edit the parameter group and change `rds.force_ssl` to 1.<br />If the DB instance uses the default parameter group that doesn’t have `rds.force_ssl` enabled, create a new parameter group. You can modify the new parameter group by using the Amazon RDS API or manually as in the following instructions.<br />To create a new parameter group:1. Sign in to the AWS Management console and open [the Amazon RDS console](https://console.aws.amazon.com/rds/) for the AWS Region that hosts the DB instance.<br />2. In the navigation pane, choose **Parameter groups**.<br />3. Choose **Create parameter group**, and set the following values: For **Parameter group family**, choose **postgres14**.For **Group name**, type **pgsql-<database\_instance>-ssl**.For **Description**, enter a free-form description for the parameter group you’re adding.Choose **Create**.<br />4. Choose the parameter group that you created.<br />5. From **Parameter group actions**, choose **Edit**.<br />6. Find **rds.force\_ssl** and change its setting to **1**.Conduct client-side testing before changing this parameter.<br />7. Choose **Save changes**.<br />To associate the parameter group with your PostgreSQL DB instance:1. On the Amazon RDS console, in the navigation pane, choose **Databases**, and then choose the PostgreSQL DB instance.<br />2. Choose **Modify**.<br />3. Under **Additional configuration**, choose the new parameter group, and then choose **Continue**.<br />4. Under **Schedule modifications**, choose **Apply immediately**.<br />5. Choose **Modify DB instance**.<br />For more information, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithDBInstanceParamGroups.html). | DevOps engineer, Migration engineer, DBA |
| Force SSL connections. | Connect to the Amazon RDS for PostgreSQL DB instance. Connection attempts that don’t use SSL are rejected with an error message. For more information, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.SSL.html#PostgreSQL.Concepts.General.SSL.Requiring). | DevOps engineer, Migration engineer, DBA |

### Install SSL extension
<a name="install-ssl-extension"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the SSL extension. | 1. Launch a psql or pgAdmin connection as a DBA.<br />2. Call the **ssl\_is\_used()** function to determine if SSL is being used.<pre>select ssl_is_used();</pre><br />The function returns `t` if the connection is using SSL; otherwise, it returns `f`.<br />3. Install the SSL extension.<pre>create extension sslinfo;<br />show ssl;<br />select ssl_cipher();</pre>For more information, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.SSL.html). | DevOps engineer, Migration engineer, DBA |

### Configure your PostgreSQL client for SSL
<a name="configure-your-postgresql-client-for-ssl"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure a client for SSL. | By using SSL, you can start the PostgreSQL server with support for encrypted connections that use TLS protocols. The server listens for both standard and SSL connections on the same TCP port, and negotiates with any connecting client on whether to use SSL. By default, this is a client option.<br />If you’re using the psql client:1. Make sure that the Amazon RDS certificate has been loaded to your local computer.<br />2. Launch an SSL client connection by adding the following:<pre>psql postgres -h SOMEHOST.amazonaws.com -p 8192 -U someuser sslmode=verify-full sslrootcert=rds-ssl-ca-cert.pem<br />select ssl_cipher();</pre><br />For other PostgreSQL clients:+ Modify the respective application public key parameter. This might be available as an option, as part of your connection string, or as a property on the connection page in GUI tools. <br />Review the following pages for these clients:+ [pgAdmin documentation](https://www.pgadmin.org/docs/)<br />+ [JDBC documentation](https://jdbc.postgresql.org/documentation/ssl/) | DevOps engineer, Migration engineer, DBA |

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
