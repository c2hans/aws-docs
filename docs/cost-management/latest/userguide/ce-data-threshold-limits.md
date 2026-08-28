---
source_url: https://docs.aws.amazon.com/cost-management/latest/userguide/ce-data-threshold-limits.html
---

# Understanding Cost Explorer data threshold limits
<a name="ce-data-threshold-limits"></a>

Cost Explorer supports up to 500 million usage records for resource-level data at daily granularity and up to 500 million usage records for hourly granularity features (EC2 resource-level data at hourly granularity and hourly granularity for all services without resources).

To make sure Cost Explorer can deliver an optimal customer experience, if your estimated usage records is above these limits, you’ll receive a data threshold error and you won’t be able to save your preferences.

If you receive the data threshold error while setting resource-level data at daily granularity, you can reduce the number of services you want to enable resource-level data for. If the error still persists, consider retrieving your data using Cost and Usage Reports (CUR). You can set CUR to include resource IDs.

If you receive the data threshold error while setting hourly granularity, consider choosing between hourly cost and usage data for all services without resource-level data and EC2 resource-level data at hourly granularity. If the error still persists, consider retrieving your data using Cost and Usage Reports (CUR). You can set CUR to get cost and usage information at hourly granularity with resource IDs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
