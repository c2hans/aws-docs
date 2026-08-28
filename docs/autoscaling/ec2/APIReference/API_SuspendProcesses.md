---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SuspendProcesses.html
---

# SuspendProcesses
<a name="API_SuspendProcesses"></a>

Suspends the specified auto scaling processes, or all processes, for the specified Auto Scaling group.

If you suspend either the `Launch` or `Terminate` process types, it can prevent other process types from functioning properly. For more information, see [Suspend and resume Amazon EC2 Auto Scaling processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html) in the *Amazon EC2 Auto Scaling User Guide*.

To resume processes that have been suspended, call the [ResumeProcesses](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_ResumeProcesses.html) API.

## Request Parameters
<a name="API_SuspendProcesses_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 **ScalingProcesses.member.N**
One or more of the following processes:
+  `Launch`
+  `Terminate`
+  `AddToLoadBalancer`
+  `AlarmNotification`
+  `AZRebalance`
+  `HealthCheck`
+  `InstanceRefresh`
+  `ReplaceUnhealthy`
+  `ScheduledActions`
If you omit this property, all processes are specified.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## Errors
<a name="API_SuspendProcesses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

 ** ResourceInUse **
The operation can't be performed because the resource is in use.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_SuspendProcesses_Examples"></a>

### Example
<a name="API_SuspendProcesses_Example_1"></a>

This example illustrates one usage of SuspendProcesses.

#### Sample Request
<a name="API_SuspendProcesses_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=SuspendProcesses
&AutoScalingGroupName=my-asg
&ScalingProcesses.member.1=AlarmNotification
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_SuspendProcesses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/SuspendProcesses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/SuspendProcesses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/SuspendProcesses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/SuspendProcesses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/SuspendProcesses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/SuspendProcesses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/SuspendProcesses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/SuspendProcesses)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/SuspendProcesses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/SuspendProcesses)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
