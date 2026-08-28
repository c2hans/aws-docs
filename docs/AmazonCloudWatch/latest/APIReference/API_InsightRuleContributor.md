---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_InsightRuleContributor.html
---

# InsightRuleContributor
<a name="API_InsightRuleContributor"></a>

One of the unique contributors found by a Contributor Insights rule. If the rule contains multiple keys, then a unique contributor is a unique combination of values from all the keys in the rule.

If the rule contains a single key, then each unique contributor is each unique value for this key.

For more information, see [GetInsightRuleReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetInsightRuleReport.html).

## Contents
<a name="API_InsightRuleContributor_Contents"></a>

 ** ApproximateAggregateValue **   <a name="ACW-Type-InsightRuleContributor-ApproximateAggregateValue"></a>
An approximation of the aggregate value that comes from this contributor.
Type: Double
Required: Yes

 ** Datapoints **   <a name="ACW-Type-InsightRuleContributor-Datapoints"></a>
An array of the data points where this contributor is present. Only the data points when this contributor appeared are included in the array.
Type: Array of [InsightRuleContributorDatapoint](API_InsightRuleContributorDatapoint.md) objects
Required: Yes

 ** Keys **   <a name="ACW-Type-InsightRuleContributor-Keys"></a>
One of the log entry field keywords that is used to define contributors for this rule.
Type: Array of strings
Required: Yes

## See Also
<a name="API_InsightRuleContributor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/InsightRuleContributor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/InsightRuleContributor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/InsightRuleContributor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
