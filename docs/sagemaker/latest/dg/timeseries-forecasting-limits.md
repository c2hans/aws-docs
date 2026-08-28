---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-forecasting-limits.html
---

# Time-series forecasting resource limits for Autopilot
<a name="timeseries-forecasting-limits"></a>

The following table lists the resource limits for time-series forecasting jobs in Amazon SageMaker Autopilot and whether or not you can adjust each limit.

| **Resource limits** | **Default limit** | **Adjustable** |
| --- | --- | --- |
| Size of input dataset | 30 GB | Yes |
| Size of a single Parquet file | 2 GB | No |
| Maximum number of rows in a dataset | 3 billion | Yes |
| Maximum number of grouping columns | 5 | No |
| Maximum number of numerical features | 13 | No |
| Maximum number of categorical features | 10 | No |
| Maximum number of time-series (unique combinations of item and grouping columns) per dataset | 5,000,000 | Yes |
| Maximum Forecast horizon | 500 | Yes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
