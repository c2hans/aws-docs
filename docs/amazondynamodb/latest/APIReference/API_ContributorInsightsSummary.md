---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ContributorInsightsSummary.html
---

# ContributorInsightsSummary
<a name="API_ContributorInsightsSummary"></a>

Represents a Contributor Insights summary entry.

## Contents
<a name="API_ContributorInsightsSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContributorInsightsMode **   <a name="DDB-Type-ContributorInsightsSummary-ContributorInsightsMode"></a>
Indicates the current mode of CloudWatch Contributor Insights, specifying whether it tracks all access and throttled events or throttled events only for the DynamoDB table or index.
Type: String
Valid Values: `ACCESSED_AND_THROTTLED_KEYS | THROTTLED_KEYS`
Required: No

 ** ContributorInsightsStatus **   <a name="DDB-Type-ContributorInsightsSummary-ContributorInsightsStatus"></a>
Describes the current status for contributor insights for the given table and index, if applicable.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | FAILED`
Required: No

 ** IndexName **   <a name="DDB-Type-ContributorInsightsSummary-IndexName"></a>
Name of the index associated with the summary, if any.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** TableName **   <a name="DDB-Type-ContributorInsightsSummary-TableName"></a>
Name of the table associated with the summary.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_ContributorInsightsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ContributorInsightsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ContributorInsightsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ContributorInsightsSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
