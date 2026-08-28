---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AggregationConfiguration.html
---

# AggregationConfiguration
<a name="API_AggregationConfiguration"></a>

An object that contains configuration settings for aggregating events.

## Contents
<a name="API_AggregationConfiguration_Contents"></a>

 ** EventCategory **   <a name="awscloudtrail-Type-AggregationConfiguration-EventCategory"></a>
Specifies the event category for which aggregation should be performed.
Type: String
Valid Values: `Data`
Required: Yes

 ** Templates **   <a name="awscloudtrail-Type-AggregationConfiguration-Templates"></a>
A list of aggregation templates that can be used to configure event aggregation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Valid Values: `API_ACTIVITY | RESOURCE_ACCESS | USER_ACTIONS`
Required: Yes

## See Also
<a name="API_AggregationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/AggregationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/AggregationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/AggregationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
