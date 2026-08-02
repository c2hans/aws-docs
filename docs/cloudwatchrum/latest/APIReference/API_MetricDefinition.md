---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_MetricDefinition.html
---

# MetricDefinition
<a name="API_MetricDefinition"></a>

A structure that displays the definition of one extended metric that RUM sends to CloudWatch or CloudWatch Evidently. For more information, see [ Additional metrics that you can send to CloudWatch and CloudWatch Evidently](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-vended-metrics.html).

## Contents
<a name="API_MetricDefinition_Contents"></a>

 ** MetricDefinitionId **   <a name="cloudwatchrum-Type-MetricDefinition-MetricDefinitionId"></a>
The ID of this metric definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** Name **   <a name="cloudwatchrum-Type-MetricDefinition-Name"></a>
The name of the metric that is defined in this structure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** DimensionKeys **   <a name="cloudwatchrum-Type-MetricDefinition-DimensionKeys"></a>
This field is a map of field paths to dimension names. It defines the dimensions to associate with this metric in CloudWatch The value of this field is used only if the metric destination is `CloudWatch`. If the metric destination is `Evidently`, the value of `DimensionKeys` is ignored.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 29 items.
Key Length Constraints: Minimum length of 1. Maximum length of 280.
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `(?!:).*[^\s].*`
Required: No

 ** EventPattern **   <a name="cloudwatchrum-Type-MetricDefinition-EventPattern"></a>
The pattern that defines the metric. RUM checks events that happen in a user's session against the pattern, and events that match the pattern are sent to the metric destination.
If the metrics destination is `CloudWatch` and the event also matches a value in `DimensionKeys`, then the metric is published with the specified dimensions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4000.
Required: No

 ** Namespace **   <a name="cloudwatchrum-Type-MetricDefinition-Namespace"></a>
If this metric definition is for a custom metric instead of an extended metric, this field displays the metric namespace that the custom metric is published to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 237.
Pattern: `.*[a-zA-Z0-9-._/#:]+`
Required: No

 ** UnitLabel **   <a name="cloudwatchrum-Type-MetricDefinition-UnitLabel"></a>
Use this field only if you are sending this metric to CloudWatch. It defines the CloudWatch metric unit that this metric is measured in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ValueKey **   <a name="cloudwatchrum-Type-MetricDefinition-ValueKey"></a>
The field within the event object that the metric value is sourced from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 280.
Required: No

## See Also
<a name="API_MetricDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/MetricDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/MetricDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/MetricDefinition)
