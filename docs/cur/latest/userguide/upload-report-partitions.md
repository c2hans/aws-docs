---
source_url: https://docs.aws.amazon.com/cur/latest/userguide/upload-report-partitions.html
---

# Uploading your report partitions
<a name="upload-report-partitions"></a>

To query your Cost and Usage Reports data, you need to upload the data into your Athena table. You must do this for each new AWS CUR report that AWS delivers to you.<a name="upload-partitions"></a>

**To upload your latest partitions**

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. Choose the vertical three dots next to your table name.

1. Choose **Load partitions**.

If you don't upload your partitions, Athena returns either no results or an error message that indicates missing data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cur` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
