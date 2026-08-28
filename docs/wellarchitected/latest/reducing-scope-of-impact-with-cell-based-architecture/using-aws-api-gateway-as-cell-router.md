---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/using-aws-api-gateway-as-cell-router.html
---

# Using Amazon API Gateway as cell router
<a name="using-aws-api-gateway-as-cell-router"></a>

 [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) is an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale. It's a serverless regional service and has a good fit to be your cell router. It has native integration with many AWS services, caching support, throttling, rate limit, canary deployments, usage plan configuration and many other features. [DynamoDB](https://docs.aws.amazon.com/dynamodb/index.html) is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability com latency single digit in milliseconds and with an SLA of 99.99% and 99.999% with global tables enabled.

![Diagram showing the use of Amazon API Gateway](http://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/images/api-gateway.png)

 DynamoDB also features the [Amazon DynamoDB Accelerator (DAX)](https://aws.amazon.com/dynamodb/dax/?ref=wellarchitected) is a fully managed, highly available in-memory cache for Amazon DynamoDB that delivers up to a 10X performance improvement from milliseconds to microseconds, even at millions of requests per second.

 DynamoDB is a powerful serverless and regional NoSQL database, but according to your workload needs, any database can be used in this model of cell router architecture.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
