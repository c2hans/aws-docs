---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-oracle-database-homogeneous-migration/plan.html
---

# Phase 2: Plan
<a name="plan"></a>

After you gather information about the database during the preparation phase, you decide the migration strategy in the planning phase. There are seven common migration strategies (7 Rs):
+ Rehost
+ Replatform
+ Refactor (re-architect)
+ Repurchase
+ Retire
+ Retain
+ Relocate

For help determining the R type, see the [decision tree](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/prioritization-and-migration-strategy.html#migration-r-type) in *Application portfolio assessment guide for AWS Cloud migration*. The migration strategy for your database depends on factors such as your business need, time and financial constraints, and resource requirements. However, in a homogeneous migration, where the source and target database engines are both Oracle, the migration strategy is limited to rehost, replatform, and relocate. The migration strategy also helps determine the target. If you choose rehost or relocate as the migration type, the target for Oracle Database is an EC2 instance. If you choose the replatform strategy, the target is Amazon RDS for Oracle or Amazon RDS Custom for Oracle.

The following table lists the supported R types for homogeneous database migrations based on the source Oracle Database technology.

|
|
| Source Oracle Database technology | Rehost | Replatform | Relocate |
| --- |--- |--- |--- |
| Oracle Database Enterprise Edition | Yes | Yes | Yes |
| Oracle Database Standard Edition 2 | Yes | Yes | Yes |
| Oracle Real Application Clusters (RAC) | Not available | Not available | Not available |
| Oracle RAC with Data Guard | Not available | Not available | Yes |
| Oracle Standalone Cluster with Data Guard | Yes | Yes | Yes |
| Oracle Exadata | Not available | Yes | Not available |
| Oracle Data Warehouse | Yes | Not available | Yes |
| Oracle Enterprise Resource Planning (ERP) | Yes | Not available | Yes |

Choosing a migration strategy also depends on the workload. You can use [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_GettingStarted.html) or [AWS Database Migration Service (AWS DMS) Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html) to evaluate and decide the migration strategy. The following table shows examples of application workloads and their corresponding migration strategies.

|
|
| Application type | Description | Migration strategy |
| --- |--- |--- |
| In-house applications | Online Database Connectivity (ODBC) or Java Database Connectivity (JDBC) workloads, and light workloads with proprietary features | Candidate for replatform |
| SaaS or ISV-provided software | Heavy workloads with proprietary features | Candidate for replatform |
| ERP applications | Engine-specific workloads | Candidate for replatform or rehost |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
