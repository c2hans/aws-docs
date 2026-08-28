---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceDeploymentCircuitBreaker.html
---

# ServiceDeploymentCircuitBreaker
<a name="API_ServiceDeploymentCircuitBreaker"></a>

Information about the circuit breaker used to determine when a service deployment has failed.

The deployment circuit breaker is the rolling update mechanism that determines if the tasks reach a steady state. The deployment circuit breaker has an option that will automatically roll back a failed deployment to the last cpompleted service revision. For more information, see [How the Amazon ECS deployment circuit breaker detects failures](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-circuit-breaker.html) in the* Amazon ECS Developer Guide*.

## Contents
<a name="API_ServiceDeploymentCircuitBreaker_Contents"></a>

 ** failureCount **   <a name="ECS-Type-ServiceDeploymentCircuitBreaker-failureCount"></a>
The number of times the circuit breaker detected a service deploymeny failure.
Type: Integer
Required: No

 ** status **   <a name="ECS-Type-ServiceDeploymentCircuitBreaker-status"></a>
The circuit breaker status. Amazon ECS is not using the circuit breaker for service deployment failures when the status is `DISABLED`.
Type: String
Valid Values: `TRIGGERED | MONITORING | MONITORING_COMPLETE | DISABLED`
Required: No

 ** threshold **   <a name="ECS-Type-ServiceDeploymentCircuitBreaker-threshold"></a>
The threshhold which determines that the service deployment failed.
The deployment circuit breaker calculates the threshold value, and then uses the value to determine when to move the deployment to a FAILED state. The deployment circuit breaker has a minimum threshold of 3 and a maximum threshold of 200. and uses the values in the following formula to determine the deployment failure.
 `0.5 * desired task count`
Type: Integer
Required: No

## See Also
<a name="API_ServiceDeploymentCircuitBreaker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceDeploymentCircuitBreaker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceDeploymentCircuitBreaker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceDeploymentCircuitBreaker)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
