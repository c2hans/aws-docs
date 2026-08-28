---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/performance-at-scale.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Performance at scale
<a name="performance-at-scale"></a>

 Code pulled in as a container image from [Amazon Elastic Container Registry ](https://aws.amazon.com/ecr/) (Amazon ECR), or from a zip file uploaded to Amazon S3, runs in an isolated environment managed by AWS. You do not have to scale your Lambda functions—each time an event notification is received by your function, AWS Lambda locates available capacity within its compute fleet and runs your code with runtime, memory, disk, and timeout configurations that you define. With this pattern, AWS can start as many copies of your function as needed.

 A Lambda-based logic tier is always right sized for your customer needs. The ability to quickly absorb surges in traffic through managed scaling and concurrent code initiation, combined with Lambda pay-per-use pricing, enables you to always meet customer requests while simultaneously not paying for idle compute capacity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
