---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_MetricDefinition.html
---

# MetricDefinition
<a name="API_MetricDefinition"></a>

Contains the full definition of a metric, including its calculation, unit, status, and trend indicator.

## Contents
<a name="API_MetricDefinition_Contents"></a>

 ** Arn **   <a name="connect-Type-MetricDefinition-Arn"></a>
The Amazon Resource Name (ARN) of the metric. May be qualified with `$SAVED` or `$LATEST`.
Type: String
Required: Yes

 ** Category **   <a name="connect-Type-MetricDefinition-Category"></a>
The category of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** Filters **   <a name="connect-Type-MetricDefinition-Filters"></a>
The filters applied to the metric.
Type: Array of [AvailableFilter](API_AvailableFilter.md) objects
Required: Yes

 ** Groupings **   <a name="connect-Type-MetricDefinition-Groupings"></a>
The groupings available for this metric.
Type: Array of strings
Required: Yes

 ** Id **   <a name="connect-Type-MetricDefinition-Id"></a>
The identifier of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: Yes

 ** Name **   <a name="connect-Type-MetricDefinition-Name"></a>
The name of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** SupportsCustomCalculation **   <a name="connect-Type-MetricDefinition-SupportsCustomCalculation"></a>
Specifies whether the metric can be used as a component of custom metrics.
Type: Boolean
Required: Yes

 ** SupportsPreaggregateCalculation **   <a name="connect-Type-MetricDefinition-SupportsPreaggregateCalculation"></a>
Specifies whether the metric can be used inside aggregating statistical functions (SUM, AVG, etc.) in custom metric calculations.
Type: Boolean
Required: Yes

 ** Type **   <a name="connect-Type-MetricDefinition-Type"></a>
The type of the metric. Valid values: `AWS_MANAGED` \| `CUSTOMER_MANAGED`.
Type: String
Valid Values: `AWS_MANAGED | CUSTOMER_MANAGED`
Required: Yes

 ** Unit **   <a name="connect-Type-MetricDefinition-Unit"></a>
The display unit for the metric's data.
Type: String
Valid Values: `INTEGER | DOUBLE | PERCENT | SECONDS`
Required: Yes

 ** CreatedTime **   <a name="connect-Type-MetricDefinition-CreatedTime"></a>
The timestamp of when the metric was created.
Type: Timestamp
Required: No

 ** CreatedUser **   <a name="connect-Type-MetricDefinition-CreatedUser"></a>
The user that created the metric. The creator for metrics created through the CreateMetric API will be `Amazon Connect API`.
Type: [CreatedByInfo](API_CreatedByInfo.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** CreationMethod **   <a name="connect-Type-MetricDefinition-CreationMethod"></a>
The method used to create the metric. Valid values: `SERVICE_LEVEL_BUILDER` (created with the guided service-level experience) \| `METRIC_BUILDER` (created with the free-form metric builder).
Type: String
Valid Values: `SERVICE_LEVEL_BUILDER | METRIC_BUILDER`
Required: No

 ** DefaultStat **   <a name="connect-Type-MetricDefinition-DefaultStat"></a>
The default stat aggregation for the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** Description **   <a name="connect-Type-MetricDefinition-Description"></a>
The description of the metric.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** EffectiveTime **   <a name="connect-Type-MetricDefinition-EffectiveTime"></a>
The earliest time that can be queried for this metric.
Type: Timestamp
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-MetricDefinition-LastModifiedRegion"></a>
The region where the metric was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-MetricDefinition-LastModifiedTime"></a>
The timestamp of when the metric was last modified.
Type: Timestamp
Required: No

 ** LastModifiedUser **   <a name="connect-Type-MetricDefinition-LastModifiedUser"></a>
The user that last modified the metric. For modifications made through the API, this will be `Amazon Connect API`.
Type: [CreatedByInfo](API_CreatedByInfo.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** MetricCalculation **   <a name="connect-Type-MetricDefinition-MetricCalculation"></a>
The calculation definition for the metric.
Type: [MetricCalculation](API_MetricCalculation.md) object
Required: No

 ** PositiveTrendIndicator **   <a name="connect-Type-MetricDefinition-PositiveTrendIndicator"></a>
How an increase in the metric value should be interpreted. Valid values: `POSITIVE`, `NEUTRAL`, `NEGATIVE`.
Type: String
Valid Values: `POSITIVE | NEGATIVE | NEUTRAL`
Required: No

 ** PrimaryEventSource **   <a name="connect-Type-MetricDefinition-PrimaryEventSource"></a>
The primary event source for the metric data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** PrimaryEventSourceEffectiveTimestampType **   <a name="connect-Type-MetricDefinition-PrimaryEventSourceEffectiveTimestampType"></a>
The timestamp type that determines where the metric appears on a time series.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** RefreshRate **   <a name="connect-Type-MetricDefinition-RefreshRate"></a>
The minimum interval, in seconds, between data refreshes for this metric.
Type: Long
Required: No

 ** Status **   <a name="connect-Type-MetricDefinition-Status"></a>
The publish status of the metric. Valid values: `PUBLISHED` \| `SAVED`.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: No

 ** SupportedStats **   <a name="connect-Type-MetricDefinition-SupportedStats"></a>
The stat aggregations available for this metric.
Type: Array of strings
Required: No

 ** Tags **   <a name="connect-Type-MetricDefinition-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_MetricDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/MetricDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/MetricDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/MetricDefinition)
