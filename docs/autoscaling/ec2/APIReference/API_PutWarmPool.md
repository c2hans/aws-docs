---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutWarmPool.html
---

# PutWarmPool
<a name="API_PutWarmPool"></a>

Creates or updates a warm pool for the specified Auto Scaling group. A warm pool is a pool of pre-initialized EC2 instances that sits alongside the Auto Scaling group. Whenever your application needs to scale out, the Auto Scaling group can draw on the warm pool to meet its new desired capacity.

This operation must be called from the Region in which the Auto Scaling group was created.

You can view the instances in the warm pool using the [DescribeWarmPool](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeWarmPool.html) API call. If you are no longer using a warm pool, you can delete it by calling the [DeleteWarmPool](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteWarmPool.html) API.

For more information, see [Warm pools for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Request Parameters
<a name="API_PutWarmPool_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** InstanceReusePolicy **
Indicates whether instances in the Auto Scaling group can be returned to the warm pool on scale in. The default is to terminate instances in the Auto Scaling group when the group scales in.
Type: [InstanceReusePolicy](API_InstanceReusePolicy.md) object
Required: No

 ** MaxGroupPreparedCapacity **
Specifies the maximum number of instances that are allowed to be in the warm pool or in any state except `Terminated` for the Auto Scaling group. This is an optional property. Specify it only if you do not want the warm pool size to be determined by the difference between the group's maximum capacity and its desired capacity.
If a value for `MaxGroupPreparedCapacity` is not specified, Amazon EC2 Auto Scaling launches and maintains the difference between the group's maximum capacity and its desired capacity. If you specify a value for `MaxGroupPreparedCapacity`, Amazon EC2 Auto Scaling uses the difference between the `MaxGroupPreparedCapacity` and the desired capacity instead.
The size of the warm pool is dynamic. Only when `MaxGroupPreparedCapacity` and `MinSize` are set to the same value does the warm pool have an absolute size.
If the desired capacity of the Auto Scaling group is higher than the `MaxGroupPreparedCapacity`, the capacity of the warm pool is 0, unless you specify a value for `MinSize`. To remove a value that you previously set, include the property but specify -1 for the value.
Type: Integer
Valid Range: Minimum value of -1.
Required: No

 ** MinSize **
Specifies the minimum number of instances to maintain in the warm pool. This helps you to ensure that there is always a certain number of warmed instances available to handle traffic spikes. Defaults to 0 if not specified.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PoolState **
Sets the instance state to transition to after the lifecycle actions are complete. Default is `Stopped`.
Type: String
Valid Values: `Stopped | Running | Hibernated`
Required: No

## Errors
<a name="API_PutWarmPool_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InstanceRefreshInProgress **
The request failed because an active instance refresh already exists for the specified Auto Scaling group.
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
<a name="API_PutWarmPool_Examples"></a>

### Example
<a name="API_PutWarmPool_Example_1"></a>

This example illustrates one usage of PutWarmPool.

#### Sample Request
<a name="API_PutWarmPool_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=PutWarmPool
&AutoScalingGroupName=my-asg
&MinSize=30
&PoolState=Hibernated
&InstanceReusePolicy.ReuseOnScaleIn=true
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_PutWarmPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/PutWarmPool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/PutWarmPool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/PutWarmPool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/PutWarmPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/PutWarmPool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/PutWarmPool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/PutWarmPool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/PutWarmPool)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/PutWarmPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/PutWarmPool)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
