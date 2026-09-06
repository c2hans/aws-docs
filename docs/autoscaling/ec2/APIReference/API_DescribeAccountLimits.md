---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html
---

# DescribeAccountLimits
<a name="API_DescribeAccountLimits"></a>

Describes the current Amazon EC2 Auto Scaling resource quotas for your account.

When you establish an AWS account, the account has initial quotas on the maximum number of Auto Scaling groups and launch configurations that you can create in a given Region. For more information, see [Quotas for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Response Elements
<a name="API_DescribeAccountLimits_ResponseElements"></a>

The following elements are returned by the service.

 ** MaxNumberOfAutoScalingGroups **
The maximum number of groups allowed for your account. The default is 200 groups per Region.
Type: Integer

 ** MaxNumberOfLaunchConfigurations **
The maximum number of launch configurations allowed for your account. The default is 200 launch configurations per Region.
Type: Integer

 ** NumberOfAutoScalingGroups **
The current number of groups for your account.
Type: Integer

 ** NumberOfLaunchConfigurations **
The current number of launch configurations for your account.
Type: Integer

## Errors
<a name="API_DescribeAccountLimits_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_DescribeAccountLimits_Examples"></a>

### Example
<a name="API_DescribeAccountLimits_Example_1"></a>

This example illustrates one usage of DescribeAccountLimits.

#### Sample Request
<a name="API_DescribeAccountLimits_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DescribeAccountLimits
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeAccountLimits_Example_1_Response"></a>

```
<DescribeAccountLimitsResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DescribeAccountLimitsResult>
    <NumberOfLaunchConfigurations>5</NumberOfLaunchConfigurations>
    <MaxNumberOfLaunchConfigurations>200</MaxNumberOfLaunchConfigurations>
    <NumberOfAutoScalingGroups>10</NumberOfAutoScalingGroups>
    <MaxNumberOfAutoScalingGroups>200</MaxNumberOfAutoScalingGroups>
  </DescribeAccountLimitsResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeAccountLimitsResponse>
```

## See Also
<a name="API_DescribeAccountLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeAccountLimits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeAccountLimits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeAccountLimits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeAccountLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeAccountLimits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeAccountLimits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeAccountLimits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeAccountLimits)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeAccountLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeAccountLimits)
