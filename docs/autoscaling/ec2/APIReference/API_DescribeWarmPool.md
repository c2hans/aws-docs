---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeWarmPool.html
---

# DescribeWarmPool
<a name="API_DescribeWarmPool"></a>

Gets information about a warm pool and its instances.

For more information, see [Warm pools for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Request Parameters
<a name="API_DescribeWarmPool_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** MaxRecords **
The maximum number of instances to return with this call. The maximum value is `50`.
Type: Integer
Required: No

 ** NextToken **
The token for the next set of instances to return. (You received this token from a previous call.)
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## Response Elements
<a name="API_DescribeWarmPool_ResponseElements"></a>

The following elements are returned by the service.

 **Instances.member.N**
The instances that are currently in the warm pool.
Type: Array of [Instance](API_Instance.md) objects

 ** NextToken **
This string indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the `NextToken` value when requesting the next set of items. This value is null when there are no more items to return.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

 ** WarmPoolConfiguration **
The warm pool configuration details.
Type: [WarmPoolConfiguration](API_WarmPoolConfiguration.md) object

## Errors
<a name="API_DescribeWarmPool_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextToken **
The `NextToken` value is not valid.
 ** message **

HTTP Status Code: 400

 ** LimitExceeded **
You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see [DescribeAccountLimits](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html).
 ** message **

HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_DescribeWarmPool_Examples"></a>

### Example
<a name="API_DescribeWarmPool_Example_1"></a>

This example illustrates one usage of DescribeWarmPool.

#### Sample Request
<a name="API_DescribeWarmPool_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DescribeWarmPool
&AutoScalingGroupName=my-asg
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeWarmPool_Example_1_Response"></a>

```
<DescribeWarmPoolResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DescribeWarmPoolResult>
    <WarmPoolConfiguration>
      <MinSize>30</MinSize>
      <MaxGroupPreparedCapacity>0</MaxGroupPreparedCapacity>
      <PoolState>Hibernated</PoolState>
    </WarmPoolConfiguration>
    <Instances />
  </DescribeWarmPoolResult>
  <ResponseMetadata>
    <RequestId>9351b5ea-b4c0-4a88-b873-c51e4EXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeWarmPoolResponse>
```

## See Also
<a name="API_DescribeWarmPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeWarmPool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeWarmPool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeWarmPool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeWarmPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeWarmPool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeWarmPool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeWarmPool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeWarmPool)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeWarmPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeWarmPool)
