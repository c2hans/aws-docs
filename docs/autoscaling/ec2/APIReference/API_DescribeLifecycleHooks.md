---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLifecycleHooks.html
---

# DescribeLifecycleHooks
<a name="API_DescribeLifecycleHooks"></a>

Gets information about the lifecycle hooks for the specified Auto Scaling group.

## Request Parameters
<a name="API_DescribeLifecycleHooks_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 **LifecycleHookNames.member.N**
The names of one or more lifecycle hooks. If you omit this property, all lifecycle hooks are described.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9\-_\/]+`
Required: No

## Response Elements
<a name="API_DescribeLifecycleHooks_ResponseElements"></a>

The following element is returned by the service.

 **LifecycleHooks.member.N**
The lifecycle hooks for the specified group.
Type: Array of [LifecycleHook](API_LifecycleHook.md) objects

## Errors
<a name="API_DescribeLifecycleHooks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_DescribeLifecycleHooks_Examples"></a>

### Example
<a name="API_DescribeLifecycleHooks_Example_1"></a>

This example illustrates one usage of DescribeLifecycleHooks.

#### Sample Request
<a name="API_DescribeLifecycleHooks_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DescribeLifecycleHooks
&AutoScalingGroupName=my-asg
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeLifecycleHooks_Example_1_Response"></a>

```
<DescribeLifecycleHooksResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DescribeLifecycleHooksResult>
    <LifecycleHooks>
      <member>
        <AutoScalingGroupName>my-asg</AutoScalingGroupName>
        <RoleARN>arn:aws:iam::1234567890:role/my-auto-scaling-role</RoleARN>
        <LifecycleTransition>autoscaling:EC2_INSTANCE_LAUNCHING</LifecycleTransition>
        <GlobalTimeout>172800</GlobalTimeout>
        <LifecycleHookName>my-launch-hook</LifecycleHookName>
        <HeartbeatTimeout>3600</HeartbeatTimeout>
        <DefaultResult>ABANDON</DefaultResult>
        <NotificationTargetARN>arn:aws:sqs:us-east-1:123456789012:my-queue</NotificationTargetARN>
      </member>
    </LifecycleHooks>
  </DescribeLifecycleHooksResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeLifecycleHooksResponse>
```

## See Also
<a name="API_DescribeLifecycleHooks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeLifecycleHooks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeLifecycleHooks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeLifecycleHooks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeLifecycleHooks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeLifecycleHooks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeLifecycleHooks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeLifecycleHooks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeLifecycleHooks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeLifecycleHooks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeLifecycleHooks)
