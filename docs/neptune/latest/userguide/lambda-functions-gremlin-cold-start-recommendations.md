---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/lambda-functions-gremlin-cold-start-recommendations.html
---

# Factors that may slow down cold starts of Neptune Gremlin Lambda functions
<a name="lambda-functions-gremlin-cold-start-recommendations"></a>

The first time an AWS Lambda function is invoked is referred to as a cold start. There are several factors that can increase the latency of a cold start:
+ **Be sure to assign enough memory to your Lambda function.**   –   Compilation during a cold start can be significantly slower for a Lambda function than it would be on EC2 because AWS Lambda allocates CPU cycles [linearly in proportion to the memory](https://docs.aws.amazon.com/lambda/latest/dg/configuration-console.html) that you assign to the function. With 1,769 MB of memory, a function receives the equivalent of one full vCPU (one vCPU-second of credits per second). The impact of not assigning enough memory to receive adequate CPU cycles is particularly pronounced for large Lambda functions written in Java.
+ **Be aware that [enabling IAM database authentication](iam-auth-enable.md) may slow down a cold start**   –   AWS Identity and Access Management (IAM) database authentication can also slow down cold starts, particularly if the Lambda function has to generate a new signing key. This latency only affects the cold start and not subsequent requests, because once IAM DB auth has established the connection credentials, Neptune only periodically validates that they are still valid.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
