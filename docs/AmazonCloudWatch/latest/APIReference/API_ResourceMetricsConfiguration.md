---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ResourceMetricsConfiguration.html
---

# ResourceMetricsConfiguration
<a name="API_ResourceMetricsConfiguration"></a>

Represents a resource metrics configuration for an AWS resource. A resource metrics configuration enables detailed metric collection for the resource that is identified by its Amazon Resource Name (ARN). Each AWS resource can have only one resource metrics configuration.

This structure is returned by the [CreateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_CreateResourceMetricsConfiguration.html), [UpdateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateResourceMetricsConfiguration.html), and [GetResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetResourceMetricsConfiguration.html) operations.

## Contents
<a name="API_ResourceMetricsConfiguration_Contents"></a>

 ** CreatedAt **   <a name="ACW-Type-ResourceMetricsConfiguration-CreatedAt"></a>
The date and time that the resource metrics configuration was created.
Type: Timestamp
Required: Yes

 ** ResourceArn **   <a name="ACW-Type-ResourceMetricsConfiguration-ResourceArn"></a>
The Amazon Resource Name (ARN) of the AWS resource that this configuration applies to.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-zA-Z0-9-]+:[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:.+`
Required: Yes

 ** UpdatedAt **   <a name="ACW-Type-ResourceMetricsConfiguration-UpdatedAt"></a>
The date and time that the resource metrics configuration was last updated. When the configuration is first created, this value is the same as `CreatedAt`.
Type: Timestamp
Required: Yes

 ** MetricSelections **   <a name="ACW-Type-ResourceMetricsConfiguration-MetricSelections"></a>
The metrics that Amazon CloudWatch collects for the resource. If this field is not present, Amazon CloudWatch collects all available detailed metrics for the resource.
Type: Array of [ResourceMetricSelection](API_ResourceMetricSelection.md) objects
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_ResourceMetricsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ResourceMetricsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ResourceMetricsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ResourceMetricsConfiguration)
