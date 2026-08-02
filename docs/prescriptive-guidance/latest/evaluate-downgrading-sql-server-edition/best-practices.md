---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-sql-server-edition/best-practices.html
---

# Best practices
<a name="best-practices"></a>

## Best practices for downgrading SQL Server Enterprise edition to Standard edition
<a name="best-practices-for-downgrading-sql-server-enterprise-edition-to-standard-edition.2a97e35e-8c21-52c4-b963-93458f1d782b"></a>

The following best practices are recommended for assessing and downgrading your SQL Server Enterprise edition to Standard edition on Amazon RDS for SQL Server.
+ **Validate vendor support for SQL Server Standard edition** - Ensure that your application is certified to run on SQL Server Standard edition. Check directly with the software vendor or their documentation. Downgrading to Standard edition without vendor confirmation might invalidate support for the application.
+ **Identify the use of Enterprise edition features for administration activities** - Database administrators or application administrators sometimes rely on Enterprise edition features to improve operational processes. Some examples are online maintenance activities (such as online index create and rebuild). Identify usage of such features and make an informed decision. You can modify your operations or apply workarounds where possible to mitigate the loss of Enterprise edition features.
+ **Assess workload patterns of SQL Server Enterprise edition **- SQL Server Standard edition automatically restricts usage to a maximum of 24 CPU cores or 4 sockets at any time. For a list of instance types that are available for SQL Server Standard edition, see the [Amazon RDS for SQL Server documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.InstanceClasses). Analyze your database workload pattern to determine whether the maximum limit of 24 CPU cores will negatively impact service levels when you downgrade to Standard edition.
+ **Test your workload against SQL Server Standard edition **- Run multiple tests using representative workload to determine whether the 24-core limit imposed by Standard edition will have a negative impact on your workload. Monitor results and tune the database as required.
+ **Test database administration activities **- Monitoring, performance assessments, tuning, and maintenance tasks to build comfort levels around new ways of working in the Standard edition environment.
+ **Test the migration process** - Run comprehensive migration tests to build operator confidence, fine-tune the approach, and document every issue with resolution.

## Best practices for Amazon RDS for SQL Server
<a name="best-practices-for-amazon-rds-for-sql-server.878f34bf-466c-57cc-9cb0-5051d7257bb1"></a>

For best practices for working with Amazon RDS for SQL Server, see the [User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html#CHAP_BestPractices.SQLServer) and view the [Deep dive on new features in Amazon RDS for SQL Server video](https://www.youtube.com/watch?v=R4Vj88iqu5s).
