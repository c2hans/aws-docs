---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_AggregatedSourceStatus.html
---

# AggregatedSourceStatus
<a name="API_AggregatedSourceStatus"></a>

The current sync status between the source and the aggregator account.

## Contents
<a name="API_AggregatedSourceStatus_Contents"></a>

 ** AwsRegion **   <a name="config-Type-AggregatedSourceStatus-AwsRegion"></a>
The region authorized to collect aggregated data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** LastErrorCode **   <a name="config-Type-AggregatedSourceStatus-LastErrorCode"></a>
The error code that AWS Config returned when the source account aggregation last failed.
Type: String
Required: No

 ** LastErrorMessage **   <a name="config-Type-AggregatedSourceStatus-LastErrorMessage"></a>
The message indicating that the source account aggregation failed due to an error.
Type: String
Required: No

 ** LastUpdateStatus **   <a name="config-Type-AggregatedSourceStatus-LastUpdateStatus"></a>
Filters the last updated status type.
+ Valid value FAILED indicates errors while moving data.
+ Valid value SUCCEEDED indicates the data was successfully moved.
+ Valid value OUTDATED indicates the data is not the most recent.
Type: String
Valid Values: `FAILED | SUCCEEDED | OUTDATED`
Required: No

 ** LastUpdateTime **   <a name="config-Type-AggregatedSourceStatus-LastUpdateTime"></a>
The time of the last update.
Type: Timestamp
Required: No

 ** SourceId **   <a name="config-Type-AggregatedSourceStatus-SourceId"></a>
The source account ID or an organization.
Type: String
Required: No

 ** SourceType **   <a name="config-Type-AggregatedSourceStatus-SourceType"></a>
The source account or an organization.
Type: String
Valid Values: `ACCOUNT | ORGANIZATION`
Required: No

## See Also
<a name="API_AggregatedSourceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/AggregatedSourceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/AggregatedSourceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/AggregatedSourceStatus)
