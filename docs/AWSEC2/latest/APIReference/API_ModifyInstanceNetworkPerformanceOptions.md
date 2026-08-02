---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceNetworkPerformanceOptions.html
---

# ModifyInstanceNetworkPerformanceOptions
<a name="API_ModifyInstanceNetworkPerformanceOptions"></a>

Change the configuration of the network performance options for an existing instance.

## Request Parameters
<a name="API_ModifyInstanceNetworkPerformanceOptions_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **BandwidthWeighting**
Specify the bandwidth weighting option to boost the associated type of baseline bandwidth, as follows:
default
This option uses the standard bandwidth configuration for your instance type.
vpc-1
This option boosts your networking baseline bandwidth and reduces your EBS baseline bandwidth.
ebs-1
This option boosts your EBS baseline bandwidth and reduces your networking baseline bandwidth.
Type: String
Valid Values: `default | vpc-1 | ebs-1`
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId**
The ID of the instance to update.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyInstanceNetworkPerformanceOptions_ResponseElements"></a>

The following elements are returned by the service.

 **bandwidthWeighting**
Contains the updated configuration for bandwidth weighting on the specified instance.
Type: String
Valid Values: `default | vpc-1 | ebs-1`

 **instanceId**
The instance ID that was updated.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ModifyInstanceNetworkPerformanceOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyInstanceNetworkPerformanceOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyInstanceNetworkPerformanceOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyInstanceNetworkPerformanceOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyInstanceNetworkPerformanceOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyInstanceNetworkPerformanceOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyInstanceNetworkPerformanceOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyInstanceNetworkPerformanceOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyInstanceNetworkPerformanceOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyInstanceNetworkPerformanceOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyInstanceNetworkPerformanceOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyInstanceNetworkPerformanceOptions)
