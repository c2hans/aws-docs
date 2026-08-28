---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_QuerySummary.html
---

# QuerySummary
<a name="API_QuerySummary"></a>

Contains summary information about a query.

## Contents
<a name="API_QuerySummary_Contents"></a>

 ** queryId **   <a name="iotsitewise-Type-QuerySummary-queryId"></a>
The unique identifier for the query execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** status **   <a name="iotsitewise-Type-QuerySummary-status"></a>
The current query status.
Type: String
Valid Values: `SUBMITTED | RUNNING | COMPLETED | FAILED | CANCELED | CANCELING`
Required: Yes

 ** submittedAt **   <a name="iotsitewise-Type-QuerySummary-submittedAt"></a>
The date and time when the query was submitted, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** completedAt **   <a name="iotsitewise-Type-QuerySummary-completedAt"></a>
The date and time when the query reached a terminal state, in Unix epoch time.
Type: Timestamp
Required: No

## See Also
<a name="API_QuerySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/QuerySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/QuerySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/QuerySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
