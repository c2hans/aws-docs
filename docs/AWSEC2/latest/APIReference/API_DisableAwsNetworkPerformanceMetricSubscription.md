---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableAwsNetworkPerformanceMetricSubscription.html
---

# DisableAwsNetworkPerformanceMetricSubscription
<a name="API_DisableAwsNetworkPerformanceMetricSubscription"></a>

Disables Infrastructure Performance metric subscriptions.

## Request Parameters
<a name="API_DisableAwsNetworkPerformanceMetricSubscription_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Destination**
The target Region or Availability Zone that the metric subscription is disabled for. For example, `eu-north-1`.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Metric**
The metric used for the disabled subscription.
Type: String
Valid Values: `aggregate-latency`
Required: No

 **Source**
The source Region or Availability Zone that the metric subscription is disabled for. For example, `us-east-1`.
Type: String
Required: No

 **Statistic**
The statistic used for the disabled subscription.
Type: String
Valid Values: `p50`
Required: No

## Response Elements
<a name="API_DisableAwsNetworkPerformanceMetricSubscription_ResponseElements"></a>

The following elements are returned by the service.

 **output**
Indicates whether the unsubscribe action was successful.
Type: Boolean

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DisableAwsNetworkPerformanceMetricSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DisableAwsNetworkPerformanceMetricSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisableAwsNetworkPerformanceMetricSubscription)
