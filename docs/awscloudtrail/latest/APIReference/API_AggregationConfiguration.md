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
