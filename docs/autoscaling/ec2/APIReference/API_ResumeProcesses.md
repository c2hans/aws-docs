---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_ResumeProcesses.html
---

# ResumeProcesses
<a name="API_ResumeProcesses"></a>

Resumes the specified suspended auto scaling processes, or all suspended process, for the specified Auto Scaling group.

For more information, see [Suspend and resume Amazon EC2 Auto Scaling processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Request Parameters
<a name="API_ResumeProcesses_RequestParameters"></a>

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
<a name="API_ResumeProcesses_Errors"></a>

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
<a name="API_ResumeProcesses_Examples"></a>

### Example
<a name="API_ResumeProcesses_Example_1"></a>

This example illustrates one usage of ResumeProcesses.

#### Sample Request
<a name="API_ResumeProcesses_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=ResumeProcesses
&AutoScalingGroupName=my-asg
&ScalingProcesses.member.1=AlarmNotification
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_ResumeProcesses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/ResumeProcesses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/ResumeProcesses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/ResumeProcesses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/ResumeProcesses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/ResumeProcesses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/ResumeProcesses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/ResumeProcesses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/ResumeProcesses)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/ResumeProcesses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/ResumeProcesses)
