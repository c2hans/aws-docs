---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_ProcessType.html
---

# ProcessType
<a name="API_ProcessType"></a>

Describes a process type.

For more information, see [Types of processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html#process-types) in the *Amazon EC2 Auto Scaling User Guide*.

## Contents
<a name="API_ProcessType_Contents"></a>

 ** ProcessName **
One of the following processes:
+  `Launch`
+  `Terminate`
+  `AddToLoadBalancer`
+  `AlarmNotification`
+  `AZRebalance`
+  `HealthCheck`
+  `InstanceRefresh`
+  `ReplaceUnhealthy`
+  `ScheduledActions`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

## See Also
<a name="API_ProcessType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/ProcessType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/ProcessType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/ProcessType)
