---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-microsoft-sql-server-database-to-microsoft-sql-server-on-amazon-ec2-running-linux.html
---

# Migrate an on-premises Microsoft SQL Server database to Microsoft SQL Server on Amazon EC2 running Linux
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-microsoft-sql-server-on-amazon-ec2-running-linux"></a>

*Tirumala Dasari, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-microsoft-sql-server-on-amazon-ec2-running-linux-summary"></a>

This pattern describes how to migrate from an on-premises Microsoft SQL Server database running on Microsoft Windows, to Microsoft SQL Server on an Amazon Elastic Compute Cloud (Amazon EC2) Linux instance by using backup and restore utilities.

## Prerequisites and limitations
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-microsoft-sql-server-on-amazon-ec2-running-linux-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Amazon EC2 Linux AMI (Amazon Machine Image) with Microsoft SQL Server
+ AWS Direct Connect between on-premises Windows and Microsoft SQL Server on the Linux EC2 instance

## Architecture
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-microsoft-sql-server-on-amazon-ec2-running-linux-architecture"></a>

**Source technology stack**
+ On-premises Microsoft SQL Server database

**Target technology stack**
+ Linux EC2 instance with a Microsoft SQL Server database

**Database migration architecture**

![Architecture diagram to migrate an on-premises SQL Server database to a Linux EC2 instance.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f331ad15-2d41-4087-a6d1-60e3443e2acf/images/f50a779a-ce5d-44b1-8d37-dedd6400a12c.png)

## Tools
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-microsoft-sql-server-on-amazon-ec2-running-linux-tools"></a>
+ **WinSCP** - This tool enables Windows users to easily share files with Linux users.
+ **Sqlcmd** - This command-line utility lets you submit T-SQL statements or batches to local and remote instances of SQL Server. The utility is extremely useful for repetitive database tasks such as batch processing or unit testing.

## Epics
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-microsoft-sql-server-on-amazon-ec2-running-linux-epics"></a>

### Prepare the EC2 Linux instance with SQL Server
<a name="prepare-the-ec2-linux-instance-with-sql-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Select an AMI that provides the Linux operating system and includes Microsoft SQL Server. |  | Sysadmin |
| Configure the AMI to create an EC2 instance. |  | Sysadmin |
| Create inbound and outbound rules for security groups. |  | Sysadmin |
| Configure the Linux EC2 instance for a Microsoft SQL Server database. |  | DBA |
| Create users and provide permissions as in the source database. |  | Appowner, DBA |
| Install SQL Server tools and the sqlcmd utility on the Linux EC2 instance. |  | DBA |

### Back up the database and move backup file to Linux EC2 instance
<a name="back-up-the-database-and-move-backup-file-to-linux-ec2-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Back up the on-premises SQL Server database. |  | DBA |
| Install WinSCP on Microsoft SQL Server. |  | DBA |
| Move the backup file to the Linux EC2 instance running Microsoft SQL Server. |  | DBA |

### Restore the database on Linux EC2 instance running SQL Server
<a name="restore-the-database-on-linux-ec2-instance-running-sql-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Restore the database from the database backup file by using the sqlcmd utility. |  | DBA |
| Validate database objects and data. |  | Developer, Test engineer |

### Cut over from Windows SQL Server to Windows SQL Server on Linux EC2 instance
<a name="cut-over-from-windows-sql-server-to-windows-sql-server-on-linux-ec2-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate database objects and data. |  | Developer, Test engineer |
| Cut over from the on-premises Microsoft SQL Server database to the Linux EC2 instance running Microsoft SQL Server. |  | DBA |

## Related resources
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-microsoft-sql-server-on-amazon-ec2-running-linux-resources"></a>
+ [How to configure SQL Server 2017 on Amazon Linux and Ubuntu AMIs](https://aws.amazon.com/blogs/database/configuring-sql-server-2017-on-amazon-linux-2-and-ubuntu-amis/)
+ [Installation of SQL tools on a Linux instance](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-2017#RHEL)
+ [Backup and restoration from an on-premises Microsoft SQL Server database to Microsoft SQL Server on a Linux EC2 instance](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-migrate-restore-database?view=sql-server-2017#create-a-backup-on-windows)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
