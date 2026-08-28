---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/communication-patterns.html
---

# Communication patterns
<a name="communication-patterns"></a>

In a microservices architecture, communication occurs in two main patterns: *synchronous* and *asynchronous*. In synchronous communication, the caller waits for a response before proceeding, similar to a real-time HTTP REST API call. Asynchronous communication follows a message-based pattern where the caller continues processing without waiting for a response, such as when using message queues. The following sections examine each pattern's implementation, benefits, and use cases in detail.
+ [Synchronous communication](synchronous.md)
+ [Asynchronous communication](asynchronous.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
