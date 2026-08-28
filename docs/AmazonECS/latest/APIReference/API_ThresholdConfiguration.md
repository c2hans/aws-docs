---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ThresholdConfiguration.html
---

# ThresholdConfiguration
<a name="API_ThresholdConfiguration"></a>

Defines the failure threshold that the deployment circuit breaker uses to monitor a deployment. The `type` and `value` together determine the number of task failures that are tolerated before the circuit breaker triggers.

By default, the threshold configuration uses a `type` of `BOUNDED_PERCENT` with a `value` of `50`.

## Contents
<a name="API_ThresholdConfiguration_Contents"></a>

 ** type **   <a name="ECS-Type-ThresholdConfiguration-type"></a>
Determines how Amazon ECS uses `value` to calculate the failure threshold. For the percentage types (`BOUNDED_PERCENT` and `UNBOUNDED_PERCENT`), Amazon ECS multiplies `value` by the latest service desired count. For `COUNT`, Amazon ECS uses `value` directly as the threshold. The default is `BOUNDED_PERCENT`.
Type: String
Valid Values: `COUNT | BOUNDED_PERCENT | UNBOUNDED_PERCENT`
Required: Yes

 ** value **   <a name="ECS-Type-ThresholdConfiguration-value"></a>
Specifies the integer that Amazon ECS uses to calculate the failure threshold. When `type` is `COUNT`, this value is the failure threshold itself. When `type` is a percentage type, Amazon ECS multiplies this value by the latest service desired count to produce the failure threshold. The default is `50`.
Type: Integer
Required: Yes

## See Also
<a name="API_ThresholdConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ThresholdConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ThresholdConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ThresholdConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
