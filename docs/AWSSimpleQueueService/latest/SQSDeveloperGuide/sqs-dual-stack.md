---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dual-stack.html
---

# Connect to Amazon SQS using Dual-stack (IPv4 and IPv6) endpoints
<a name="sqs-dual-stack"></a>

 Dual-stack endpoints support both IPv4 and IPv6 traffic. When you make a request to a dual-stack endpoint, the endpoint URL resolves to an IPv4 or an IPv6 address. For more information on dual-stack and FIPS endpoints, see the [SDK Reference guide](https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html).

 Amazon SQS supports Regional dual-stack endpoints, which means that you must specify the AWS Region as part of the endpoint name. Dual-stack endpoint names use the following naming convention: `sqs.{{Region}}.amazonaws.com`. For example, the dual-stack endpoint name for the `eu-west-1` Region is `sqs.{{eu-west-1}}.amazonaws.com`.

For the full list of Amazon SQS endpoints, see the [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/sqs-service.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
