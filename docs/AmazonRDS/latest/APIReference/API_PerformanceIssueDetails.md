---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_PerformanceIssueDetails.html
---

# PerformanceIssueDetails
<a name="API_PerformanceIssueDetails"></a>

Details of the performance issue.

## Contents
<a name="API_PerformanceIssueDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Analysis **
The analysis of the performance issue. The information might contain markdown.
Type: String
Required: No

 ** EndTime **
The time when the performance issue stopped.
Type: Timestamp
Required: No

 ** Metrics.member.N **
The metrics that are relevant to the performance issue.
Type: Array of [Metric](API_Metric.md) objects
Required: No

 ** StartTime **
The time when the performance issue started.
Type: Timestamp
Required: No

## See Also
<a name="API_PerformanceIssueDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/PerformanceIssueDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/PerformanceIssueDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/PerformanceIssueDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
