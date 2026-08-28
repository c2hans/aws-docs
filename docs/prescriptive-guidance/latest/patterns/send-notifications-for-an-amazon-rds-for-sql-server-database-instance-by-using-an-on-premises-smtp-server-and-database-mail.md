---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/send-notifications-for-an-amazon-rds-for-sql-server-database-instance-by-using-an-on-premises-smtp-server-and-database-mail.html
---

# Send notifications for an Amazon RDS for SQL Server database instance by using an on-premises SMTP server and Database Mail
<a name="send-notifications-for-an-amazon-rds-for-sql-server-database-instance-by-using-an-on-premises-smtp-server-and-database-mail"></a>

*Nishad Mankar, Amazon Web Services*

## Summary
<a name="send-notifications-for-an-amazon-rds-for-sql-server-database-instance-by-using-an-on-premises-smtp-server-and-database-mail-summary"></a>

[Database Mail](https://learn.microsoft.com/en-us/sql/relational-databases/database-mail/database-mail?view=sql-server-ver16) (Microsoft documentation) sends email messages, such as notifications or alerts, from a Microsoft SQL Server database by using a Simple Mail Transfer Protocol (SMTP) server. The Amazon Relational Database Service (Amazon RDS) for Microsoft SQL Server documentation provides instructions for using Amazon Simple Email Service (Amazon SES) as the SMTP server for Database Mail. For more information, see [Using Database Mail on Amazon RDS for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.DBMail.html). As an alternative configuration, this pattern explains how to configure Database Mail to send email from an Amazon RDS for SQL Server database (DB) instance by using an on-premises SMTP server as the mail server.

## Prerequisites and limitations
<a name="send-notifications-for-an-amazon-rds-for-sql-server-database-instance-by-using-an-on-premises-smtp-server-and-database-mail-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An Amazon RDS DB instance running a Standard or Enterprise edition of SQL Server
+ The IP address or hostname of the on-premises SMTP server
+ An inbound [security group rule](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html#working-with-security-group-rules) that allows connections to the Amazon RDS for SQL Server DB instance from the IP address of the SMTP server
+ A connection, such as an [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) connection, between your on-premises network and the virtual private cloud (VPC) that contains the Amazon RDS DB instance

**Limitations**
+ Express editions of SQL Server aren't supported.
+ For more information about limitations, see [Limitations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.FeatureSupport.Limits) in *Using Database Mail on Amazon RDS for SQL Server* in the Amazon RDS documentation.

**Product versions**
+ Standard and Enterprise editions of [SQL Server versions supported in RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.VersionSupport)

## Architecture
<a name="send-notifications-for-an-amazon-rds-for-sql-server-database-instance-by-using-an-on-premises-smtp-server-and-database-mail-architecture"></a>

**Target technology stack**
+ Amazon RDS for SQL Server database instance
+ Amazon Route 53 forwarding rule
+ Database Mail
+ On-premises SMTP server
+ Microsoft SQL Server Management Studio (SSMS)

**Target architecture**

The following image shows the target architecture for this pattern. When an event or action occurs that initiates a notification or alert regarding the database instance, Amazon RDS for SQL Server uses Database Mail to send an email notification. Database Mail uses the on-premises SMTP server to send the email.

![Amazon RDS for SQL server using an on-premises SMTP server to send email notifications to users.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e5599724-43cf-4fe1-8c5a-8fca1a424993/images/47efb12f-3505-4a60-ac43-194a176e71c8.png)

## Tools
<a name="send-notifications-for-an-amazon-rds-for-sql-server-database-instance-by-using-an-on-premises-smtp-server-and-database-mail-tools"></a>

**AWS services**
+ [Amazon Relational Database Service (Amazon RDS) for Microsoft SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html) helps you set up, operate, and scale a SQL Server relational database in the AWS Cloud.
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) is a highly available and scalable DNS web service.

**Other tools**
+ [Database Mail](https://learn.microsoft.com/en-us/sql/relational-databases/database-mail/database-mail) is a tool that sends e-mail messages, such as notifications and alerts, from the SQL Server Database Engine to users.
+ [Microsoft SQL Server Management Studio (SSMS)](https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms) is a tool for managing SQL Server, including accessing, configuring, and administering SQL Server components. In this pattern, you use SSMS to run the SQL commands to set up Database Mail on an Amazon RDS for SQL Server DB instance.

## Epics
<a name="send-notifications-for-an-amazon-rds-for-sql-server-database-instance-by-using-an-on-premises-smtp-server-and-database-mail-epics"></a>

### Enable network connectivity with the on-premises SMTP server
<a name="enable-network-connectivity-with-the-on-premises-smtp-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remove Multi-AZ from the RDS DB instance. | If you're using a Multi-Zone RDS DB instance, convert the Multi-AZ instance to a Single-AZ instance. When you have finished configuring Database Mail, you will convert the DB instance back to a Multi-AZ deployment. The Database Mail configuration then works in both the primary and secondary nodes. For instructions, see [Removing Multi-AZ from a Microsoft SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerMultiAZ.html#USER_SQLServerMultiAZ.Removing). | DBA |
| Create an allow list for the Amazon RDS endpoint or IP address on the on-premises SMTP server. | The SMTP server is outside of the AWS network. On the on-premises SMTP server, create an allow list that permits the server to communicate with the outbound endpoint or IP address for the Amazon RDS instance or the Amazon Elastic Compute Cloud (Amazon EC2) instance hosted on Amazon RDS. This procedure varies from organization to organization. For more information about the DB instance endpoint, see [Finding the DB instance endpoint and port number](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMicrosoftSQLServerInstance.html#sqlserver-endpoint). | DBA |
| Remove port 25 restrictions. | By default, AWS restricts port 25 on EC2 instances. To remove the port 25 restriction, do the following:1. Sign in with your AWS account, and then open the [Request to remove email sending limitations form](https://aws-portal.amazon.com/gp/aws/html-forms-controller/contactus/ec2-email-limit-rdns-request).<br />2. Enter your email address so that AWS Support can contact you with updates about your request.<br />3. Provide the required information in the **Use case description** field.<br />4. Choose **Submit**.+ If you have instances in more than one AWS Region, then submit a separate request for each Region.<br />+ It can take up to 48 hours to process your request. | General AWS |
| Add a Route 53 rule to resolve DNS queries for the SMTP server. | Use Route 53 to resolve DNS queries between your AWS resources and the on-premises SMTP server. You must create a rule that forwards the DNS queries to the SMTP server domain, such as `example.com`. For instructions, see [Creating forwarding rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-rules-managing.html#resolver-rules-managing-creating-rules) in the Route 53 documentation. | Network administrator |

### Set up Database Mail on the Amazon RDS for SQL Server DB instance
<a name="set-up-database-mail-on-the-amazon-rds-for-sql-server-db-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Enable Database Mail. | Create a parameter group for Database Mail, set the `database mail xps` parameter to `1`, and then associate the Database Mail parameter group with the target RDS DB instance. For instructions, see [Enabling Database Mail](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.DBMail.html#SQLServer.DBMail.Enable) in the Amazon RDS documentation. Do not proceed to the *Configuring Database Mail* section in these instructions. The configuration for the on-premises SMTP server differs from Amazon SES. | DBA |
| Connect to the DB instance. | From a bastion host, use Microsoft SQL Server Management Studio (SSMS) to connect to the Amazon RDS for SQL Server database instance. For instructions, see [Connecting to a DB instance running the Microsoft SQL Server database engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMicrosoftSQLServerInstance.html). If you encounter any errors, see the connection troubleshooting references in the [Related resources](#send-notifications-for-an-amazon-rds-for-sql-server-database-instance-by-using-an-on-premises-smtp-server-and-database-mail-resources) section. | DBA |
| Create the profile. | In SSMS, enter the following SQL statement to create the Database Mail profile. Replace the following values:+ For `profile_name`, enter a name for the new profile.<br />+ For `description`, enter a brief description of the new profile.<br />For more information about this stored procedure and its arguments, see [sysmail\_add\_profile\_sp](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-profile-sp-transact-sql) in the Microsoft documentation.<pre>EXECUTE msdb.dbo.sysmail_add_profile_sp<br /> @profile_name = 'SQL Alerts profile',<br /> @description = 'Profile used for sending outgoing notifications using OM SMTP Server.';</pre> | DBA |
| Add principals to the profile. | Enter the following SQL statement to add public or private principals to the Database Mail profile. A *principal* is an entity that can request SQL Server resources. Replace the following values:+ For `profile_name`, enter the name of the profile you created previously.<br />+ For `principal_name`, enter the name of the database user or role. This value must map to an SQL Server authentication user, a Windows Authentication user, or a Windows Authentication group.<br />For more information about this stored procedure and its arguments, see [sysmail\_add\_principalprofile\_sp](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-principalprofile-sp-transact-sql) in the Microsoft documentation.<pre>EXECUTE msdb.dbo.sysmail_add_principalprofile_sp<br /> @profile_name = 'SQL Alerts profile',<br /> @principal_name = 'public',<br /> @is_default = 1 ;</pre> | DBA |
| Create the account. | Enter the following SQL statement to create the Database Mail account. Replace the following values:+ For `account_name`, enter a name for the new account.<br />+ For `description`, enter a brief description of the new account.<br />+ For `email_address`, enter the e-mail address to send the Database Mail messages from.<br />+ For `display_address`, enter a display name to use for outgoing messages for this account, such as `SQL Server Automated Notification`. You can also use the value you entered for `email_address`.<br />+ For `mailserver_name`, enter the name or IP address of the SMTP mail server.<br />+ For `port`, leave the value of `25`.<br />+ For `enable_ssl`, leave the value at `1` or enter `0` if you don't want Database Mail to encrypt communication by using SSL.<br />+ For `username`, enter the username for logging on to the SMTP mail server. If the server doesn't require authentication, enter `NULL`.<br />+ For `password`, enter the password for logging on to the SMTP mail server. If the server doesn't require authentication, enter `NULL`.<br />For more information about this stored procedure and its arguments, see [sysmail\_add\_account\_sp](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-account-sp-transact-sql) in the Microsoft documentation.<pre>EXECUTE msdb.dbo.sysmail_add_account_sp<br /> @account_name = 'SQL Alerts account',<br /> @description = 'Database Mail account for sending outgoing notifications.',<br /> @email_address = 'xyz@example.com',<br /> @display_name = 'xyz@example.com',<br /> @mailserver_name = 'test_smtp.example.com',<br /> @port = 25,<br /> @enable_ssl = 1,<br /> @username = 'SMTP-username',<br /> @password = 'SMTP-password';</pre> | DBA |
| Add the account to the profile. | Enter the following SQL statement to add the Database Mail account to the Database Mail profile. Replace the following values:+ For `profile_name`, enter the name of the profile you created previously.<br />+ For `account_name`, enter the name of the account you created previously.<br />For more information about this stored procedure and its arguments, see [sysmail\_add\_profileaccount\_sp](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-profileaccount-sp-transact-sql) in the Microsoft documentation.<pre>EXECUTE msdb.dbo.sysmail_add_profileaccount_sp<br /> @profile_name = 'SQL Alerts profile',<br /> @account_name = 'SQL Alerts account',<br /> @sequence_number = 1;</pre> | DBA |
| (Optional) Add Multi-AZ to the RDS DB instance.  | If you want to add Multi-AZ with Database Mirroring (DBM) or Always On Availability Groups (AGs), see the instructions in [Adding Multi-AZ to a Microsoft SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerMultiAZ.html#USER_SQLServerMultiAZ.Adding). | DBA |

## Related resources
<a name="send-notifications-for-an-amazon-rds-for-sql-server-database-instance-by-using-an-on-premises-smtp-server-and-database-mail-resources"></a>
+ [Using Database Mail on Amazon RDS for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.DBMail.html) (Amazon RDS documentation)
+ [Working with file attachments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.DBMail.html#SQLServer.DBMail.MAZ) (Amazon RDS documentation)
+ [Troubleshooting connections to your SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMicrosoftSQLServerInstance.html#USER_ConnectToMicrosoftSQLServerInstance.Troubleshooting) (Amazon RDS documentation)
+ [Can't connect to Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Troubleshooting.html#CHAP_Troubleshooting.Connecting) (Amazon RDS documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
