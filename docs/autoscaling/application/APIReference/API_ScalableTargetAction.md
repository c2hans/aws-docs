---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_ScalableTargetAction.html
---

# ScalableTargetAction
<a name="API_ScalableTargetAction"></a>

Represents the minimum and maximum capacity for a scheduled action.

## Contents
<a name="API_ScalableTargetAction_Contents"></a>

 ** MaxCapacity **   <a name="autoscaling-Type-ScalableTargetAction-MaxCapacity"></a>
The maximum capacity.
Although you can specify a large maximum capacity, note that service quotas may impose lower limits. Each service has its own default quotas for the maximum capacity of the resource. If you want to specify a higher limit, you can request an increase. For more information, consult the documentation for that service. For information about the default quotas for each service, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) in the *Amazon Web Services General Reference*.
Type: Integer
Required: No

 ** MinCapacity **   <a name="autoscaling-Type-ScalableTargetAction-MinCapacity"></a>
The minimum capacity.
When the scheduled action runs, the resource will have at least this much capacity, but it might have more depending on other settings, such as the target utilization level of a target tracking scaling policy.
For certain resources, the minimum value allowed is 0. For more information, see [RegisterScalableTarget](API_RegisterScalableTarget.md).
Type: Integer
Required: No

## See Also
<a name="API_ScalableTargetAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/ScalableTargetAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/ScalableTargetAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/ScalableTargetAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
