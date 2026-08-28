---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedAutoScaling.html
---

# ManagedAutoScaling
<a name="API_ManagedAutoScaling"></a>

The auto scaling configuration created by Amazon ECS for an Express service.

## Contents
<a name="API_ManagedAutoScaling_Contents"></a>

 ** applicationAutoScalingPolicies **   <a name="ECS-Type-ManagedAutoScaling-applicationAutoScalingPolicies"></a>
The policy used for auto scaling.
Type: Array of [ManagedApplicationAutoScalingPolicy](API_ManagedApplicationAutoScalingPolicy.md) objects
Required: No

 ** scalableTarget **   <a name="ECS-Type-ManagedAutoScaling-scalableTarget"></a>
Represents a scalable target.
Type: [ManagedScalableTarget](API_ManagedScalableTarget.md) object
Required: No

## See Also
<a name="API_ManagedAutoScaling_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedAutoScaling)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedAutoScaling)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedAutoScaling)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
