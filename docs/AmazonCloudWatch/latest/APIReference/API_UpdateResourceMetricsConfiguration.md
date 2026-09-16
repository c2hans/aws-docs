---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateResourceMetricsConfiguration.html
---

# UpdateResourceMetricsConfiguration
<a name="API_UpdateResourceMetricsConfiguration"></a>

Updates the resource metrics configuration for an AWS resource. The `MetricSelections` value that you provide replaces any existing metric selections for the resource; it is not merged with them.

If you omit `MetricSelections`, Amazon CloudWatch removes any existing metric selection filter and collects all available detailed metrics for the resource.

This operation returns a `ResourceNotFoundException` if no resource metrics configuration exists for the specified resource ARN. To create a configuration, use [CreateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_CreateResourceMetricsConfiguration.html).

To update a resource metrics configuration, you must have the `cloudwatch:UpdateResourceMetricsConfiguration` permission. For information about scoping this permission to specific resources, see [Condition keys for resource metrics configuration access](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-resource-arn.html) in the *Amazon CloudWatch User Guide*.

## Request Parameters
<a name="API_UpdateResourceMetricsConfiguration_RequestParameters"></a>

 ** MetricSelections **
Specifies which metrics Amazon CloudWatch collects for the resource. The selections that you provide completely replace any existing metric selections.
If you omit this parameter, Amazon CloudWatch removes any existing metric selection filter and collects all available detailed metrics for the resource.
Type: Array of [ResourceMetricSelection](API_ResourceMetricSelection.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** ResourceArn **
The Amazon Resource Name (ARN) of the AWS resource to update the resource metrics configuration for.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-zA-Z0-9-]+:[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:.+`
Required: Yes

## Response Elements
<a name="API_UpdateResourceMetricsConfiguration_ResponseElements"></a>

The following element is returned by the service.

 ** ResourceMetricsConfiguration **
The resource metrics configuration after the update was applied.
Type: [ResourceMetricsConfiguration](API_ResourceMetricsConfiguration.md) object

## Errors
<a name="API_UpdateResourceMetricsConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The named resource does not exist.
HTTP Status Code: 404

## See Also
<a name="API_UpdateResourceMetricsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/UpdateResourceMetricsConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/UpdateResourceMetricsConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/UpdateResourceMetricsConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/UpdateResourceMetricsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/UpdateResourceMetricsConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/UpdateResourceMetricsConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/UpdateResourceMetricsConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/UpdateResourceMetricsConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/UpdateResourceMetricsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/UpdateResourceMetricsConfiguration)
