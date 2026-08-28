---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableAwsNetworkPerformanceMetricSubscription.html
---

# EnableAwsNetworkPerformanceMetricSubscription
<a name="API_EnableAwsNetworkPerformanceMetricSubscription"></a>

Enables Infrastructure Performance subscriptions.

## Request Parameters
<a name="API_EnableAwsNetworkPerformanceMetricSubscription_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Destination**
The target Region (like `us-east-2`) or Availability Zone ID (like `use2-az2`) that the metric subscription is enabled for. If you use Availability Zone IDs, the Source and Destination Availability Zones must be in the same Region.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Metric**
The metric used for the enabled subscription.
Type: String
Valid Values: `aggregate-latency`
Required: No

 **Source**
The source Region (like `us-east-1`) or Availability Zone ID (like `use1-az1`) that the metric subscription is enabled for. If you use Availability Zone IDs, the Source and Destination Availability Zones must be in the same Region.
Type: String
Required: No

 **Statistic**
The statistic used for the enabled subscription.
Type: String
Valid Values: `p50`
Required: No

## Response Elements
<a name="API_EnableAwsNetworkPerformanceMetricSubscription_ResponseElements"></a>

The following elements are returned by the service.

 **output**
Indicates whether the subscribe action was successful.
Type: Boolean

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_EnableAwsNetworkPerformanceMetricSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_EnableAwsNetworkPerformanceMetricSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/EnableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/EnableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EnableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/EnableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EnableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/EnableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/EnableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/EnableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/EnableAwsNetworkPerformanceMetricSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EnableAwsNetworkPerformanceMetricSubscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
