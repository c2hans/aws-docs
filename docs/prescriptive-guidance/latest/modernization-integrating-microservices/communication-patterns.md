---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/communication-patterns.html
---

# Communication patterns
<a name="communication-patterns"></a>

In a microservices architecture, communication occurs in two main patterns: *synchronous* and *asynchronous*. In synchronous communication, the caller waits for a response before proceeding, similar to a real-time HTTP REST API call. Asynchronous communication follows a message-based pattern where the caller continues processing without waiting for a response, such as when using message queues. The following sections examine each pattern's implementation, benefits, and use cases in detail.
+ [Synchronous communication](synchronous.md)
+ [Asynchronous communication](asynchronous.md)
