---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_NotScaledReason.html
---

# NotScaledReason
<a name="API_NotScaledReason"></a>

Describes the reason for an activity that isn't scaled (*not scaled activity*), in machine-readable format. For help interpreting the not scaled reason details, see [Scaling activities for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scaling-activities.html) in the *Application Auto Scaling User Guide*.

## Contents
<a name="API_NotScaledReason_Contents"></a>

 ** Code **   <a name="autoscaling-Type-NotScaledReason-Code"></a>
A code that represents the reason for not scaling.
Valid values:
+ AutoScalingAnticipatedFlapping
+ TargetServicePutResourceAsUnscalable
+ AlreadyAtMaxCapacity
+ AlreadyAtMinCapacity
+ AlreadyAtDesiredCapacity
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** CurrentCapacity **   <a name="autoscaling-Type-NotScaledReason-CurrentCapacity"></a>
The current capacity.
Type: Integer
Required: No

 ** MaxCapacity **   <a name="autoscaling-Type-NotScaledReason-MaxCapacity"></a>
The maximum capacity.
Type: Integer
Required: No

 ** MinCapacity **   <a name="autoscaling-Type-NotScaledReason-MinCapacity"></a>
The minimum capacity.
Type: Integer
Required: No

## See Also
<a name="API_NotScaledReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/NotScaledReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/NotScaledReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/NotScaledReason)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
