---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_mitigate_interaction_failure_limit_retries.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL05-BP03 Control and limit retry calls
<a name="rel_mitigate_interaction_failure_limit_retries"></a>

 Use exponential backoff to retry after progressively longer intervals. Introduce jitter to randomize those retry intervals, and limit the maximum number of retries.

 Typical components in a distributed software system include servers, load balancers, databases, and DNS servers. In operation, and subject to failures, any of these can start generating errors. The default technique for dealing with errors is to implement retries on the client side. This technique increases the reliability and availability of the application. However, at scale—and if clients attempt to retry the failed operation as soon as an error occurs—the network can quickly become saturated with new and retried requests, each competing for network bandwidth. This can result in a *retry storm,* which will reduce availability of the service. This pattern might continue until a full system failure occurs.

 To avoid such scenarios, backoff algorithms such as the common *exponential backoff* should be used. Exponential backoff algorithms gradually decrease the rate at which retries are performed, thus avoiding network congestion.

 Many SDKs and software libraries, including those from AWS, implement a version of these algorithms. However, **never assume a backoff algorithm exists—always test and verify this to be the case.**

 Simple backoff alone is not enough because in distributed systems all clients may backoff simultaneously, creating clusters of retry calls. Marc Brooker in his blog post [Exponential Backoff and Jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-italics%0djitter/), explains how to modify the wait() function in the exponential backoff to prevent clusters of retry calls. The solution is to add *jitter* in the wait() function. To avoid retrying for too long, implementations should cap the backoff to a maximum value.

 Finally, it’s important to configure a *maximum number of retries* or elapsed time, after which retrying will simply fail. AWS SDKs implement this by default, and it can be configured. For services lower in the stack, a maximum retry limit of zero or one can limit risk yet still be effective as retries are delegated to services higher in the stack.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Control and limit retry calls. Use exponential backoff to retry after progressively longer intervals. Introduce jitter to randomize those retry intervals, and limit the maximum number of retries.
  +  [Error Retries and Exponential Backoff in AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html)
    + Amazon SDKs implement retries and exponential backoff by default. Implement similar logic in your dependency layer when calling your own dependent services. Decide what the timeouts are and when to stop retrying based on your use case.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon API Gateway: Throttle API Requests for Better Throughput](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)
+  [Error Retries and Exponential Backoff in AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html)
+  [The Amazon Builders' Library: Avoiding fallback in distributed systems](https://aws.amazon.com/builders-library/avoiding-fallback-in-distributed-systems)
+  [The Amazon Builders' Library: Avoiding insurmountable queue backlogs](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs)
+  [The Amazon Builders' Library: Caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/)
+  [The Amazon Builders' Library: Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)

 **Related videos:**
+  [Retry, backoff, and jitter: AWS re:Invent 2019: Introducing The Amazon Builders’ Library (DOP328)](https://youtu.be/sKRdemSirDM?t=1884)
