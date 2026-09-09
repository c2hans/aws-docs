---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_CreateResourceMetricsConfiguration.html
---

# CreateResourceMetricsConfiguration
<a name="API_CreateResourceMetricsConfiguration"></a>

Creates a resource metrics configuration for an AWS resource. After you create a configuration, Amazon CloudWatch collects detailed metrics for that resource.

Each AWS resource can have only one resource metrics configuration. If a configuration already exists for the specified resource ARN, this operation returns a `ConflictException`. To modify an existing configuration, use [UpdateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateResourceMetricsConfiguration.html).

If the AWS resource that you specify in `ResourceArn` does not exist, this operation returns a `ResourceNotFoundException`. Verify that the resource ARN is correct and that the resource exists before you retry the request.

To create a resource metrics configuration, you must have the `cloudwatch:CreateResourceMetricsConfiguration` permission. For information about scoping this permission to specific resources, see [Condition keys for resource metrics configuration access](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-resource-arn.html) in the *Amazon CloudWatch User Guide*.

## Request Parameters
<a name="API_CreateResourceMetricsConfiguration_RequestParameters"></a>

 ** MetricSelections **
Specifies which metrics Amazon CloudWatch collects for the resource. If you omit this parameter, Amazon CloudWatch collects all available detailed metrics for the resource.
Type: Array of [ResourceMetricSelection](API_ResourceMetricSelection.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** ResourceArn **
The Amazon Resource Name (ARN) of the AWS resource to enable detailed monitoring for.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-zA-Z0-9-]+:[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:.+`
Required: Yes

## Response Elements
<a name="API_CreateResourceMetricsConfiguration_ResponseElements"></a>

The following element is returned by the service.

 ** ResourceMetricsConfiguration **
The resource metrics configuration that was created by this operation.
Type: [ResourceMetricsConfiguration](API_ResourceMetricsConfiguration.md) object

## Errors
<a name="API_CreateResourceMetricsConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
This operation attempted to create a resource that already exists.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The named resource does not exist.
HTTP Status Code: 404

## See Also
<a name="API_CreateResourceMetricsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/CreateResourceMetricsConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/CreateResourceMetricsConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/CreateResourceMetricsConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/CreateResourceMetricsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/CreateResourceMetricsConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/CreateResourceMetricsConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/CreateResourceMetricsConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/CreateResourceMetricsConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/CreateResourceMetricsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/CreateResourceMetricsConfiguration)
