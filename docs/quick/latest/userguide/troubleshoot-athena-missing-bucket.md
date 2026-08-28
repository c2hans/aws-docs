---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-athena-missing-bucket.html
---

# Staging bucket no longer exists when using Athena with Amazon Quick Sight
<a name="troubleshoot-athena-missing-bucket"></a>

Use this section to help solve this error: "**The staging bucket for this query result no longer exists in the underlying data source.**"

 When you create a dataset using Athena, Amazon Quick Sight creates an Amazon S3 bucket. By default, this bucket has a name similar to "`aws-athena-query-results-{{<REGION>}}-{{<ACCOUNTID>}}`". If you remove this bucket, then your next Athena query might fail with an error saying the staging bucket no longer exists.

 To fix this error, create a new bucket with the same name in the correct AWS Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
