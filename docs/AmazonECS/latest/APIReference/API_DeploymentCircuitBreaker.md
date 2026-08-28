---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeploymentCircuitBreaker.html
---

# DeploymentCircuitBreaker
<a name="API_DeploymentCircuitBreaker"></a>

**Note**
The deployment circuit breaker can only be used for services using the rolling update (`ECS`) deployment type.

The **deployment circuit breaker** determines whether a service deployment will fail if the service can't reach a steady state. If it is turned on, a service deployment will transition to a failed state and stop launching new tasks. You can also configure Amazon ECS to roll back your service to the last completed deployment after a failure. For more information, see [Rolling update](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html) in the *Amazon Elastic Container Service Developer Guide*.

For more information about API failure reasons, see [API failure reasons](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html) in the *Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_DeploymentCircuitBreaker_Contents"></a>

 ** enable **   <a name="ECS-Type-DeploymentCircuitBreaker-enable"></a>
Determines whether to use the deployment circuit breaker logic for the service.
Type: Boolean
Required: Yes

 ** rollback **   <a name="ECS-Type-DeploymentCircuitBreaker-rollback"></a>
Determines whether to configure Amazon ECS to roll back the service if a service deployment fails. If rollback is on, when a service deployment fails, the service is rolled back to the last deployment that completed successfully.
Type: Boolean
Required: Yes

 ** resetOnHealthyTask **   <a name="ECS-Type-DeploymentCircuitBreaker-resetOnHealthyTask"></a>
Specifies whether the deployment circuit breaker resets its failure count when a task reaches a healthy state. When set to `true`, a task that reaches a healthy state resets the failure count to `0`. When set to `false`, Amazon ECS does not reset the failure count. The default is `true`.
Type: Boolean
Required: No

 ** thresholdConfiguration **   <a name="ECS-Type-DeploymentCircuitBreaker-thresholdConfiguration"></a>
The threshold configuration that controls when the deployment circuit breaker triggers. The `type` and `value` together determine how many task failures are tolerated before the circuit breaker activates.
Type: [ThresholdConfiguration](API_ThresholdConfiguration.md) object
Required: No

## See Also
<a name="API_DeploymentCircuitBreaker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DeploymentCircuitBreaker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DeploymentCircuitBreaker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DeploymentCircuitBreaker)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
