---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingInstances.html
---

# DescribeAutoScalingInstances
<a name="API_DescribeAutoScalingInstances"></a>

Gets information about the Auto Scaling instances in the account and Region.

## Request Parameters
<a name="API_DescribeAutoScalingInstances_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **InstanceIds.member.N**
The IDs of the instances. If you omit this property, all Auto Scaling instances are described. If you specify an ID that does not exist, it is ignored with no error.
Array Members: Maximum number of 50 items.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** MaxRecords **
The maximum number of items to return with this call. The default value is `50` and the maximum value is `50`.
Type: Integer
Required: No

 ** NextToken **
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## Response Elements
<a name="API_DescribeAutoScalingInstances_ResponseElements"></a>

The following elements are returned by the service.

 **AutoScalingInstances.member.N**
The instances.
Type: Array of [AutoScalingInstanceDetails](API_AutoScalingInstanceDetails.md) objects

 ** NextToken **
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the `NextToken` value when requesting the next set of items. This value is null when there are no more items to return.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

## Errors
<a name="API_DescribeAutoScalingInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextToken **
The `NextToken` value is not valid.
 ** message **

HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_DescribeAutoScalingInstances_Examples"></a>

### Example
<a name="API_DescribeAutoScalingInstances_Example_1"></a>

This example illustrates one usage of DescribeAutoScalingInstances.

#### Sample Request
<a name="API_DescribeAutoScalingInstances_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DescribeAutoScalingInstances
&InstanceIds.member.1=i-1234567890abcdef0
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeAutoScalingInstances_Example_1_Response"></a>

```
<DescribeAutoScalingInstancesResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DescribeAutoScalingInstancesResult>
    <AutoScalingInstances>
      <member>
        <ProtectedFromScaleIn>false</ProtectedFromScaleIn>
        <AvailabilityZone>us-east-1b</AvailabilityZone>
        <LaunchConfigurationName>my-lc</LaunchConfigurationName>
        <LaunchTemplate />
        <InstanceId>i-1234567890abcdef0</InstanceId>
        <InstanceType>t3.micro</InstanceType>
        <AutoScalingGroupName>my-asg</AutoScalingGroupName>
        <HealthStatus>HEALTHY</HealthStatus>
        <LifecycleState>InService</LifecycleState>
        <WeightedCapacity />
      </member>
    </AutoScalingInstances>
  </DescribeAutoScalingInstancesResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeAutoScalingInstancesResponse>
```

## See Also
<a name="API_DescribeAutoScalingInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeAutoScalingInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeAutoScalingInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeAutoScalingInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeAutoScalingInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeAutoScalingInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeAutoScalingInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeAutoScalingInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeAutoScalingInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeAutoScalingInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeAutoScalingInstances)
