---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-ssis-etl/analyze.html
---

# Analysis phase
<a name="analyze"></a>

Analyzing the information from the discovery phase helps you understand the patterns and design the target architecture better. Follow these pointers to improve the outcome of analysis:
+ The logging option at the [package level](https://learn.microsoft.com/en-us/sql/integration-services/performance/integration-services-ssis-logging) logs events and captures runtime information for each component. Use custom logging so that you can configure log files to include additional information, such as execution IDs and other runtime values.
+ Redirect bad records to a different storage location for analysis, correction, and reprocessing.
+ Understand the data archival and purging strategies implemented in your on-premises SSIS environment.
+ Send alerts and notifications by using tasks that are included with SSIS (such as the [Send Mail task](https://docs.microsoft.com/en-us/sql/integration-services/control-flow/send-mail-task)) or custom scripts (such as the [Script task](https://docs.microsoft.com/en-us/sql/integration-services/control-flow/script-task)).
+ Understand the behavior of [transformations](https://docs.microsoft.com/en-us/sql/integration-services/data-flow/transformations/integration-services-transformations) in scope to avoid corrupted data. For example, the [Lookup transformation](https://learn.microsoft.com/en-us/sql/integration-services/data-flow/transformations/lookup-transformation) is an equi-join between two datasets, and its comparison is case-sensitive.

You can map each entry in the inventory to an estimated complexity, either in terms of duration (minutes or hours) or level (simple, medium, or complex). This expanded inventory, shown in the following table, is an outcome of the analysis phase.

![SSIS ETL inventory mapped to estimated complexity, as a output of the analysis phase in migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-ssis-etl/images/guide-img/ae5b08b7-f641-4524-9650-6ac5a0f71dd9/images/b985d8ed-ad92-4d13-aea7-79f7dc6905db.png)
