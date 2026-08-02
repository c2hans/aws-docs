---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_mitigate_interaction_failure_graceful_degradation.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL05-BP01 Implement graceful degradation to transform applicable hard dependencies into soft dependencies
<a name="rel_mitigate_interaction_failure_graceful_degradation"></a>

 When a component's dependencies are unhealthy, the component itself can still function, although in a degraded manner. For example, when a dependency call fails, failover to a predetermined static response.

 Consider a service B that is called by service A and in turn calls service C.

![Diagram showing Service C fails when called from service B. Service B returns a degraded response to service A](http://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/images/graceful-degradation.png)

 When service B calls service C, it received an error or timeout from it. Service B, lacking a response from service C (and the data it contains) instead returns what it can. This can be the last cached good value, or service B can substitute a pre-determined static response for what it would have received from service C. It can then return a degraded response to its caller, service A. Without this static response, the failure in service C would cascade through service B to service A, resulting in a loss of availability.

 As per the multiplicative factor in the availability equation for hard dependencies (see [https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/availability.html#dbedbedda68f9a15ACLX122](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/availability.html#dbedbedda68f9a15ACLX122)), any drop in the availability of C seriously impacts effective availability of B. By returning the static response, service B mitigates the failure in C and, although degraded, makes service C’s availability look like 100% availability (assuming it reliably returns the static response under error conditions). Note that the static response is a simple alternative to returning an error, and is not an attempt to re-compute the response using different means. Such attempts at a completely different mechanism to try to achieve the same result are called fallback behavior, and are an anti-pattern to be avoided.

 Another example of graceful degradation is the *circuit breaker pattern*. Retry strategies should be used when the failure is transient. When this is not the case, and the operation is likely to fail, the circuit breaker pattern prevents the client from performing a request that is likely to fail. When requests are being processed normally, the circuit breaker is closed and requests flow through. When the remote system begins returning errors or exhibits high latency, the circuit breaker opens and the dependency is ignored or results are replaced with more simply obtained but less comprehensive responses (which might simply be a response cache). Periodically, the system attempts to call the dependency to determine if it has recovered. When that occurs, the circuit breaker is closed.

![Diagram showing circuit breaker in open and closed states.](http://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/images/circuit-breaker.png)

 In addition to the closed and open states shown in the diagram, after a configurable period of time in the open state, the circuit breaker can transition to half-open. In this state, it periodically attempts to call the service at a much lower rate than normal. This probe is used to check the health of the service. After a number of successes in half-open state, the circuit breaker transitions to closed, and normal requests resume.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Implement graceful degradation to transform applicable hard dependencies into soft dependencies. When a component's dependencies are unhealthy, the component itself can still function, although in a degraded manner. For example, when a dependency call fails, failover to a predetermined static response.
  +  By returning a static response, your workload mitigates failures that occur in its dependencies.
    +  [Well-Architected lab: Level 300: Implementing Health Checks and Managing Dependencies to Improve Reliability](https://wellarchitectedlabs.com/Reliability/300_Health_Checks_and_Dependencies/README.html)
  +  Detect when the retry operation is likely to fail, and prevent your client from making failed calls with the circuit breaker pattern.
    +  [CircuitBreaker](https://martinfowler.com/bliki/CircuitBreaker.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon API Gateway: Throttle API Requests for Better Throughput](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)
+  [CircuitBreaker (summarizes Circuit Breaker from “Release It\!” book)](https://martinfowler.com/bliki/CircuitBreaker.html)
+  [Error Retries and Exponential Backoff in AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html)
+  [Michael Nygard “Release It\! Design and Deploy Production-Ready Software”](https://pragprog.com/titles/mnee2/release-it-second-edition/)
+  [The Amazon Builders' Library: Avoiding fallback in distributed systems](https://aws.amazon.com/builders-library/avoiding-fallback-in-distributed-systems)
+  [The Amazon Builders' Library: Avoiding insurmountable queue backlogs](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs)
+  [The Amazon Builders' Library: Caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/)
+  [The Amazon Builders' Library: Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)

 **Related videos:**
+  [Retry, backoff, and jitter: AWS re:Invent 2019: Introducing The Amazon Builders’ Library (DOP328)](https://youtu.be/sKRdemSirDM?t=1884)

 **Related examples:**
+  [Well-Architected lab: Level 300: Implementing Health Checks and Managing Dependencies to Improve Reliability](https://wellarchitectedlabs.com/Reliability/300_Health_Checks_and_Dependencies/README.html)
