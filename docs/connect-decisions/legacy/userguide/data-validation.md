---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/data-validation.html
---

# Data Validation
<a name="data-validation"></a>

Data Validation is a crucial step early in the forecast creation process that ensures the input data meets the necessary quality standards for forecasting. This feature runs a series of checks on your data, surfacing data errors that need to be fixed before proceeding to forecast creation, helping you identify and resolve issues early in the process.

The data validation step is preceded by a set of preprocessing activities to prepare the data, based on the plan settings or definition, which includes the following:
+ *Aggregation to align with forecast granularity.* For example:
  + If your forecast granularity is set to weekly, daily demand history data will be aggregated to weekly totals.
  + If your demand history contains product, site, customer, and channel dimensions, but your forecast granularity is set to product-site level, the system will aggregate sales across all customers and channels for each product-site combination.
+ *Data transformations from Demand Plan settings.* These transformations are based on your Demand Planning configuration settings. For example, if you have configured the system to ignore negative values, these will be handled accordingly.
+ *Product lineage consideration*. The system takes into account product relationships, such as predecessor-successor pairs or product alternatives, as defined in your configuration.
+ *Supplementary time series transformation*. The system transforms supplementary time series data into demand drivers that can influence the forecast generation. These transformed demand drivers provide additional context to the items above.

**Topics**
+ [Data Validation Process](data-validation-process.md)
+ [Data Validation Report Access](data-validation-report-access.md)
+ [Data Validation Error Export](data-validation-error-export.md)
+ [Data Validation Rules](data-validation-rules.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
