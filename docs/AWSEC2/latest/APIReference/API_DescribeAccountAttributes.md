---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAccountAttributes.html
---

# DescribeAccountAttributes
<a name="API_DescribeAccountAttributes"></a>

Describes attributes of your AWS account. The following are the supported account attributes:
+  `default-vpc`: The ID of the default VPC for your account, or `none`.
+  `max-instances`: This attribute is no longer supported. The returned value does not reflect your actual vCPU limit for running On-Demand Instances. For more information, see [On-Demand Instance Limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html#ec2-on-demand-instances-limits) in the *Amazon Elastic Compute Cloud User Guide*.
+  `max-elastic-ips`: The maximum number of Elastic IP addresses that you can allocate.
+  `supported-platforms`: This attribute is deprecated.
+  `vpc-max-elastic-ips`: The maximum number of Elastic IP addresses that you can allocate.
+  `vpc-max-security-groups-per-interface`: The maximum number of security groups that you can assign to a network interface.

**Note**
The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Request Parameters
<a name="API_DescribeAccountAttributes_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AttributeName.N**
The account attribute names.
Type: Array of strings
Valid Values: `supported-platforms | default-vpc`
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_DescribeAccountAttributes_ResponseElements"></a>

The following elements are returned by the service.

 **accountAttributeSet**
Information about the account attributes.
Type: Array of [AccountAttribute](API_AccountAttribute.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeAccountAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeAccountAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeAccountAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeAccountAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeAccountAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeAccountAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeAccountAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeAccountAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeAccountAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeAccountAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeAccountAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeAccountAttributes)
