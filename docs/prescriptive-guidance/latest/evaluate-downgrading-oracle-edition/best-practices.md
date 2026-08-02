---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-oracle-edition/best-practices.html
---

# Best practices
<a name="best-practices"></a>

We recommend the following best practices for assessing and downgrading your Oracle Database Enterprise Edition (EE) to Standard Edition 2 (SE2) on Amazon RDS for Oracle:
+ **Validate vendor support for Oracle Database SE2** – Confirm that your application is certified to run on Oracle Database SE2. Check directly with the software vendor or their documentation. Downgrading to Oracle Database SE2 without vendor confirmation might invalidate support for an application.
+ **Identify the use of Oracle Database EE features for administration activities** – Database or application administrators sometimes rely on Oracle Database EE features to improve operational processes. Examples include online maintenance activities, such as index rebuild, and table move, and parallelism for maintenance activities. Identify usage of such features and make an informed decision. You can modify your operations or apply workarounds where possible to mitigate the loss of Oracle Database EE features.
+ **Assess workload patterns of the database** – Oracle Database SE2 automatically restricts usage to a maximum of 16 CPU threads. Analyze your database workload pattern to determine whether the 16 CPU thread limit will negatively impact service levels when you downgrade to Oracle Database SE2. You can use tools such as the Automatic Workload Repository (AWR) reports, "DBA\_HIST\_\*" views, and server-level metrics for this analysis. For more information about  the available instance class for Oracle Database SE2, see the [Amazon RDS for Oracle documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html#Oracle.Concepts.InstanceClasses).
+ **Test your workload against Oracle Database SE2** – Run multiple tests using a representative workload to determine whether the 16-thread limit imposed by Oracle Database SE2 has any negative impact on your workload. Monitor results and tune the database as required.
+ **Test database administration activities** – Test activities such as monitoring, performance assessments, tuning, and maintenance tasks to build comfort levels around new ways of working in the Oracle Database SE2 environment.
+ **Test the migration process** – Run end-to-end migration tests to build operator confidence, fine-tune the approach, and document every issue and its resolution.
