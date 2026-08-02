---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/synchronous.html
---

# Synchronous communication
<a name="synchronous"></a>

In synchronous communication, a client initiates a request to a service, as the following diagram illustrates. Examples include a request to fetch information, such as an `HTTP GET` request, or a request to mutate data, such as an `HTTP PUT` request. In either case, the client waits for the server to respond before it proceeds. Synchronous calls are familiar to most developers, are easy to implement and troubleshoot, and, in many cases, are the widely accepted standard for communication.

![Synchronous communication between clients and microservices, or between microservices.](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/images/guide-img/89e63ee3-ec0f-41b0-920f-39a1fbded9a6/images/ae8ad062-7419-4142-9aee-1d8601e4964e.png)

Benefits of synchronous communication include:
+ **Predictable flow control** – Deterministic execution and clear request-response cycles that are easier to understand compared with asynchronous communication.
+ **Strong consistency** – Immediate confirmation of data changes and state updates.
+ **Simple error handling** – Direct propagation of errors and exceptions.
+ **Easy debugging** – Straightforward request tracing and monitoring.
+ **Protocol support** – Well-established protocols such as HTTP and REST, which make implementation straightforward.

Synchronous communication has some drawbacks:
+ **Tight coupling** – Direct dependency of services on each other's availability.
+ **Network impact** – Increased network load because of constant open connections.
+ **Resource utilization** – Higher memory usage from maintaining connection states.
+ **Cascading failures** – Ability for issues in one service to quickly propagate through the system.
