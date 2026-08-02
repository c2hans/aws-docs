---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachTrafficSources.html
---

# DetachTrafficSources
<a name="API_DetachTrafficSources"></a>

Detaches one or more traffic sources from the specified Auto Scaling group.

When you detach a traffic source, it enters the `Removing` state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the traffic source using the [DescribeTrafficSources](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTrafficSources.html) API call. The instances continue to run.

## Request Parameters
<a name="API_DetachTrafficSources_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 **TrafficSources.member.N**
The unique identifiers of one or more traffic sources. You can specify up to 10 traffic sources.
Type: Array of [TrafficSourceIdentifier](API_TrafficSourceIdentifier.md) objects
Required: Yes

## Errors
<a name="API_DetachTrafficSources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_DetachTrafficSources_Examples"></a>

### Example
<a name="API_DetachTrafficSources_Example_1"></a>

This example detaches the Classic Load Balancer named `my-classic-load-balancer` from the Auto Scaling group named `my-asg`.

#### Sample Request
<a name="API_DetachTrafficSources_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DetachTrafficSources
&AutoScalingGroupName=my-asg
&TrafficSources.member.1.Identifier=my-classic-load-balancer
&TrafficSources.member.1.Type=elb
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_DetachTrafficSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DetachTrafficSources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DetachTrafficSources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DetachTrafficSources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DetachTrafficSources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DetachTrafficSources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DetachTrafficSources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DetachTrafficSources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DetachTrafficSources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DetachTrafficSources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DetachTrafficSources)
