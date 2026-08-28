---
source_url: https://docs.aws.amazon.com/guidance/latest/automotive-data-platform-on-aws/pm-plan.html
---

# Plan your deployment
<a name="pm-plan"></a>

This section provides deployment options, cost estimates, and resource requirements for implementing Predictive Maintenance in your AWS environment.

## Cost Breakdown
<a name="cost-breakdown"></a>

 **Monthly costs** (us-east-1 region, 10K-50K vehicles):

| Service | Usage | Monthly Cost | Notes |
| --- | --- | --- | --- |
| Amazon SageMaker Training | ml.m5.xlarge, 4 hours/week | $50 | Weekly model training |
| Amazon SageMaker Inference | ml.m5.large, 2 instances | $200 | Daily batch transform jobs |
| AWS Lambda | 5M invocations | $10 | Query, processing, alerts |
| Amazon DynamoDB | 1M reads, 100K writes | $5 | Alert storage |
| Amazon SNS | 10K notifications | $0.50 | Email and SMS alerts |
| Amazon API Gateway | 1M requests | $3.50 | Alerts API |
| AWS Step Functions | 10K executions | $2.50 | ML and filtering pipelines |
| CloudWatch Logs | 20 GB/month | $10 | Logging and monitoring |
|  **Total (10K vehicles)**  |  |  **\~$355**  | Scales with fleet size |
|  **Total (50K vehicles)**  |  |  **\~$650**  | Higher Glue and SageMaker costs |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for an Automotive Data Platform on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
