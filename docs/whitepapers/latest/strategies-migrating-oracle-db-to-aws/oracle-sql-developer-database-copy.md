---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/oracle-sql-developer-database-copy.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Oracle SQL Developer database copy
<a name="oracle-sql-developer-database-copy"></a>

 If the total size of the data you are migrating is under 200 MB, the simplest solution is to use the Oracle SQL Developer **Database Copy** function. [Oracle SQL Developer](https://www.oracle.com/database/technologies/appdev/sqldeveloper-landing.html) is a no- cost GUI tool available from Oracle for data manipulation, development, and management. This easy-to-use, Java-based tool is available for Microsoft Windows, Linux, or Mac OS X. With this method, data transfer from a source database to a destination database is done directly, without any intermediary steps.

 Because SQL Developer can handle a large number of objects, it can comfortably migrate small databases, even if the database contains numerous objects. You will need a reliable network connection between the source database and the destination database to use this method. Keep in mind that this method does **not** encrypt data during transfer.

 To migrate a database using the Oracle SQL Developer **Database Copy** function, perform the following steps:

1.  Install Oracle SQL Developer.

1.  Connect to your source and destination databases.

1.  From the **Tools** menu of Oracle SQL Developer, choose the **Database Copy** command to copy your data to your Amazon RDS or Amazon EC2 instance.

1.  Follow the steps in the **Database Copy Wizard**. You can choose the objects you want to migrate and use filters to limit the data.

 The following screenshot shows the **Database Copy Wizard**.

![Screen capture showing the Database Copy Wizard](http://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/images/database-copy-wizard.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
