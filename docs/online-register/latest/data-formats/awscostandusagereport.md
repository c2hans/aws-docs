---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/awscostandusagereport.html
---

# Data retrieval APIs for AWS Cost and Usage Report
<a name="awscostandusagereport"></a>

AWS Cost and Usage Report provides the following APIs for data retrieval.

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="cur-DescribeReportDefinitions"></a>[DescribeReportDefinitions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_DescribeReportDefinitions.html) | Get Cost and Usage Report Definitions | Read |
| <a name="cur-GetClassicReport"></a>[GetClassicReport](https://docs.aws.amazon.com/cur/latest/userguide/security.html#user-permissions) | Get Bills CSV report | Read |
| <a name="cur-GetClassicReportPreferences"></a>[GetClassicReportPreferences](https://docs.aws.amazon.com/cur/latest/userguide/security.html#user-permissions) | Get the classic report enablement status for Usage Reports | Read |
| <a name="cur-GetUsageReport"></a>[GetUsageReport](https://docs.aws.amazon.com/cur/latest/userguide/security.html#user-permissions) | Get list of AWS services, usage type and operation for the Usage Report workflow. Allows or denies download of usage reports too | Read |
| <a name="cur-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_ListTagsForResource.html) | List tags for a resource | Read |
| <a name="cur-ValidateReportDestination"></a>[ValidateReportDestination](https://docs.aws.amazon.com/cur/latest/userguide/security.html#user-permissions) | Validates if the s3 bucket exists with appropriate permissions for CUR delivery | Read |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query online-register` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
