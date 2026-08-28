---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel_mitigate_interaction_failure_stateless.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL05-BP06 Make services stateless where possible
<a name="rel_mitigate_interaction_failure_stateless"></a>

 Services should either not require state, or should offload state such that between different client requests, there is no dependence on locally stored data on disk and in memory. This allows servers to be replaced at will without causing an availability impact. Amazon ElastiCache or Amazon DynamoDB are good destinations for offloaded state.

![In this stateless web application, session state is offloaded to Amazon ElastiCache.](http://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/images/stateless-webapp.png)

 When users or services interact with an application, they often perform a series of interactions that form a session. A session is unique data for users that persists between requests while they use the application. A stateless application is an application that does not need knowledge of previous interactions and does not store session information.

 Once designed to be stateless, you can then use serverless compute services, such as AWS Lambda or AWS Fargate.

 In addition to server replacement, another benefit of stateless applications is that they can scale horizontally because any of the available compute resources (such as EC2 instances and AWS Lambda functions) can service any request.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Make your applications stateless. Stateless applications allow horizontal scaling and are tolerant to the failure of an individual node.
  +  Remove state that could actually be stored in request parameters.
  +  After examining whether the state is required, move any state tracking to a resilient multi-zone cache or data store like Amazon ElastiCache, Amazon RDS, Amazon DynamoDB, or a third-party distributed data solution. Store a state that could not be moved to resilient data stores.
    +  Some data (like cookies) can be passed in headers or query parameters.
    +  Refactor to remove state that can be quickly passed in requests.
    +  Some data may not actually be needed per request and can be retrieved on demand.
    +  Remove data that can be asynchronously retrieved.
    +  Decide on a data store that meets the requirements for a required state.
    +  Consider a NoSQL database for non-relational data.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [The Amazon Builders' Library: Avoiding fallback in distributed systems](https://aws.amazon.com/builders-library/avoiding-fallback-in-distributed-systems)
+  [The Amazon Builders' Library: Avoiding insurmountable queue backlogs](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs)
+  [The Amazon Builders' Library: Caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
