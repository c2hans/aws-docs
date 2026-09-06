---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_AggregationSummary.html
---

# AggregationSummary
<a name="API_AggregationSummary"></a>

Provides additional information about the aggregation key.

## Contents
<a name="API_AggregationSummary_Contents"></a>

 ** aggregatedAccounts **   <a name="Notifications-Type-AggregationSummary-aggregatedAccounts"></a>
Indicates the AWS accounts in the aggregation key.
Type: [SummarizationDimensionOverview](API_SummarizationDimensionOverview.md) object
Required: Yes

 ** aggregatedBy **   <a name="Notifications-Type-AggregationSummary-aggregatedBy"></a>
Indicates the criteria or rules by which notifications have been grouped together.
Type: Array of [AggregationKey](API_AggregationKey.md) objects
Required: Yes

 ** aggregatedRegions **   <a name="Notifications-Type-AggregationSummary-aggregatedRegions"></a>
Indicates the AWS Regions in the aggregation key.
Type: [SummarizationDimensionOverview](API_SummarizationDimensionOverview.md) object
Required: Yes

 ** eventCount **   <a name="Notifications-Type-AggregationSummary-eventCount"></a>
Indicates the number of events associated with the aggregation key.
Type: Integer
Required: Yes

 ** additionalSummarizationDimensions **   <a name="Notifications-Type-AggregationSummary-additionalSummarizationDimensions"></a>
List of additional dimensions used to group and summarize data.
Type: Array of [SummarizationDimensionOverview](API_SummarizationDimensionOverview.md) objects
Required: No

 ** aggregatedOrganizationalUnits **   <a name="Notifications-Type-AggregationSummary-aggregatedOrganizationalUnits"></a>
Indicates the collection of organizational units that are involved in the aggregation key.
Type: [SummarizationDimensionOverview](API_SummarizationDimensionOverview.md) object
Required: No

## See Also
<a name="API_AggregationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/AggregationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/AggregationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/AggregationSummary)
