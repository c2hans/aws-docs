---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_Query.html
---

# Query
<a name="API_Query"></a>

A SQL string of criteria about events that you want to collect in an event data store.

## Contents
<a name="API_Query_Contents"></a>

 ** CreationTime **   <a name="awscloudtrail-Type-Query-CreationTime"></a>
The creation time of a query.
Type: Timestamp
Required: No

 ** QueryId **   <a name="awscloudtrail-Type-Query-QueryId"></a>
The ID of a query.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9\-]+$`
Required: No

 ** QueryStatus **   <a name="awscloudtrail-Type-Query-QueryStatus"></a>
The status of the query. This can be `QUEUED`, `RUNNING`, `FINISHED`, `FAILED`, `TIMED_OUT`, or `CANCELLED`.
Type: String
Valid Values: `QUEUED | RUNNING | FINISHED | FAILED | CANCELLED | TIMED_OUT`
Required: No

## See Also
<a name="API_Query_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Query)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Query)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Query)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
