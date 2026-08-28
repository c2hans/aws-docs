---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/selection.html
---

# Selection
<a name="selection"></a>

| PER 1: How have you optimized the performance of your serverless application? |
| --- |
|   |

 Run performance tests on your serverless application using steady and burst rates. Using the result, try tuning capacity units and the provisioning model, and load test after changes to help you select the best configuration:
+  **[Amazon API Gateway](amazon-api-gateway.md):** Use Edge endpoints for geographically dispersed customers. Use Regional for regional customers and when using other AWS services within the same Region.
+  **[AWS Lambda](aws-lambda.md):** Test different memory settings since CPU, network, and storage IOPS are allocated proportionally. Optimize static initialization and consider provisioned concurrency.
+  **[AWS Step Functions](aws-step-functions.md)**: Test Standard and Express Workflows, consider the per second rates for both execution start rate and state transition rate.
+  **Amazon DynamoDB:** Use on-demand for unpredictable application traffic, otherwise provisioned mode for consistent traffic.
+  **Amazon Kinesis:** Use enhanced-fan-out for dedicated input/output channels per consumer in multiple consumer scenarios. Use an extended batch window for low volume transactions with Lambda.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
