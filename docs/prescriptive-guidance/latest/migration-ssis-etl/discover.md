---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-ssis-etl/discover.html
---

# Discovery phase
<a name="discover"></a>

In the discovery phase, you create a list of the SSIS packages that you want to migrate to AWS. Different development teams follow different styles, standards, and patterns for developing ETL jobs. We recommend that you review your organization's existing documents to understand these patterns. However, the documentation is often incomplete. You can automate the extraction of important information from the ETL scripts. This saves manual effort and time, reduces human errors, and standardizes the migration approach. Here are some of the important details you'll want to extract:
+ Total number of control flow tasks
+ Details of control flow tasks
+ Total number of data flow tasks
+ Data flow transformations used
+ Event handlers
+ Connection managers

Use this information to understand the ETL patterns used at your organization, to evaluate their complexity, and to identify the appropriate AWS service to migrate this information to.

Migrating these ETL details from SSIS forms the bulk of the migration effort. However, additional properties can provide insights into design and architectural decisions. Some of these SSIS properties are:
+ [Check points](https://docs.microsoft.com/en-us/sql/integration-services/packages/restart-packages-by-using-checkpoints), which are used in SSIS to restart jobs from points of failure
+ [Propagate variables](https://docs.microsoft.com/en-us/sql/integration-services/system-variables), which help an SSIS package succeed in specific use cases, even when there is an error
+ [Transaction isolation levels](https://docs.microsoft.com/en-us/sql/integration-services/set-package-properties), which control the quality of data being read from databases
+ [Logging](https://docs.microsoft.com/en-us/sql/integration-services/performance/integration-services-ssis-logging), to understand the types of logs being captured by the current design and their storage locations

The outcome of the discovery phase can be an inventory, as the following table shows.

![SSIS ETL inventory, as a output of the discovery phase in migrations](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-ssis-etl/images/guide-img/ae5b08b7-f641-4524-9650-6ac5a0f71dd9/images/2687b291-b057-4018-b256-f947e113d611.png)

This inventory might include the following information:
+ Package: Name of the SSIS package to migrate
+ Flow: [Control flow](https://docs.microsoft.com/en-us/sql/integration-services/control-flow/control-flow) or [data flow](https://docs.microsoft.com/en-us/sql/integration-services/data-flow/data-flow)
+ Task: Name of the control flow task or data flow component
+ Count: Number of times a task was used in the SSIS package

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
