---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/data-quality-checks.html
---

# Data quality checks
<a name="data-quality-checks"></a>

Data quality is an integral yet often overlooked part of the data cleaning process. The following diagram shows how data quality checks fit into the data engineering automation and access control lifecycle.

![Data quality diagram](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/images/guide-img/058e3d2f-f726-4dc0-989b-0f15dcd3bc33/images/fc535f9d-6171-437b-86e0-f271e20b516e.png)

The following table provides an overview of different data quality solutions based on use case.

|
|
| Use case | Solution | Example |
| --- |--- |--- |
| No-code solution to add column-level or table-level quality conditions | [AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/) | Checks if all column values are between 1 and 12, or if a table or column is empty |
| Custom code added to an AWS Glue job or a no-code solution (in preview) to add column-level or table-level quality conditions | [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html) | Checks if the column `first_name` is not null, or if the column `phone_number` contains only numbers or a "\+" operator and/or statistical functions, such as average or sum |
| Custom checks | ETL of choice, such as [AWS Lambda](https://aws.amazon.com/lambda/), [AWS Glue,](https://aws.amazon.com/glue/) or [Amazon EMR](https://aws.amazon.com/emr/) | Checks if the value of column A is always greater than the corresponding value of column B and column C, or if the value of column `continent` is always geographically correct and derived from the `city` column |
| Sophisticated solution with a metrics report, constraint validation, and constraint suggestions | [Deequ](https://aws.amazon.com/blogs/big-data/test-data-quality-at-scale-with-deequ/) | Checks if the `CompletenessConstraint` for the Completeness of column metric `review_id` is equal to `1` |
