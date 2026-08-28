---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/asynchronous.html
---

# Asynchronous communication
<a name="asynchronous"></a>

Conversely, in asynchronous communication, the client issues a request to a service but doesn't receive an immediate response. In this case, the client usually receives only an acknowledgement that the request was accepted.

Benefits of asynchronous communication include:
+ **Event-driven architecture support** – Natural fit for event-sourcing and command query responsibility segregation (CQRS) patterns.
+ **Better resource management** – Ability of services to process requests based on their capacity.
+ **Improved fault isolation** – Decoupling of services, which prevents cascade failures.
+ **Peak load handling** – Better handling of traffic spikes through message queuing.

Drawbacks include complexity. For example:
+ If the client requires the result of the asynchronous operation, implementing a mechanism to fetch or receive that result requires more effort.
+ It can be more difficult to troubleshoot asynchronous operations, because troubleshooting requires examining logs across multiple systems.
+ It can be more difficult to test asynchronous operations, because testing requires coordination among multiple systems and services.

Approaches to asynchronous communication include fire and forget, claim check, callback, and bidirectional communication.

## Fire and forget
<a name="fire-forget"></a>

In the fire and forget pattern, a client issues a request to the server and synchronously receives an acknowledgement indicating that the server has received the message and will process it. However, the actual processing has not yet occurred, and the client has no visibility into when or how it will be done. The following diagram illustrates this pattern.

![The fire and forget pattern in asynchronous communication.](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/images/guide-img/89e63ee3-ec0f-41b0-920f-39a1fbded9a6/images/e204b84e-d819-4993-8494-aa580294f9c9.png)

In this case, the service **should not** send the acknowledgement until the object is durably persisted. This persistence could be implemented as a database write operation or by putting an item in a queue.

Additional considerations:
+ Implement idempotency to handle duplicate messages. That is, each message should be processed only once.
+ Consider [dead-letter queues](https://aws.amazon.com/what-is/dead-letter-queue/) for failed processing.
+ Monitor message processing success rates.

## Claim check
<a name="claim-check"></a>

If a client needs the result of a service call, you can build the service to issue a *claim check* when it receives a request. The following diagram illustrates this pattern. The claim check is implemented as an identifier that the service returns in its acknowledgement. The client can use this identifier later to check on the status of the request and to retrieve the result when the request is complete.

![The claim check pattern in asynchronous communication.](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/images/guide-img/89e63ee3-ec0f-41b0-920f-39a1fbded9a6/images/b03a28e9-cb79-46f2-9336-8bd2ee636744.png)

Clients must implement a mechanism to poll for results. This could be automated (for example, a check can be performed every *n* minutes) or implemented manually, where the check is performed in response to another event or user action. Services that implement the claim check pattern should be explicit about the length of time a claim check is valid.

Best practices:
+ Implement exponential backoff for polling.
+ Set an appropriate time to live (TTL) for claim checks.
+ Provide status endpoints for progress tracking.

## Callback
<a name="callback"></a>

In the callback pattern, a client issues a request to a service and provides a location for the service to contact when the processing is complete. The client does not wait for a result, and processing continues The service is responsible for contacting the location when processing is complete and providing the outcome. Common types of locations for responses are REST APIs or queues. The following diagram illustrates the callback pattern.

![The callback pattern in asynchronous communication.](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/images/guide-img/89e63ee3-ec0f-41b0-920f-39a1fbded9a6/images/15745c28-dda9-442d-8f97-3547ccc68482.png)

Implementation:
+ Implement retry mechanisms for failed callbacks.
+ Secure the callback location as you would other services.
+ Handle callback timeouts.

## Bidirectional communication
<a name="bidirectional"></a>

To implement bidirectional communication, you must create a stateful connection between a client and a service, which enables both the client and the service to send and process messages. This is illustrated in the following diagram. Although the communication is asynchronous, the service must be able to support an open connection for each client.

![The bidirectional communication pattern in asynchronous communication.](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/images/guide-img/89e63ee3-ec0f-41b0-920f-39a1fbded9a6/images/b090fd11-3fcb-43ae-97dd-d846b0c8fa68.png)

Implementation considerations:
+ Message ordering
  + Sequence numbers
  + Partition strategies
  + Message ordering
+ State management
  + Event sourcing patterns
  + State reconciliation
  + Consistency models
+ Error handling
  + [Dead letter queues](https://aws.amazon.com/what-is/dead-letter-queue/)
  + Retry policies
  + [Circuit breakers](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html)
  + Fallback strategies
+ Monitoring and observability
  + Correlation IDs
  + Message tracking
  + Performance metrics
  + System health indicators

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
