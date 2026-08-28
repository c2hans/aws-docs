---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshooting-discovery.html
---

# Troubleshooting dependency discovery
<a name="next-gen-troubleshooting-discovery"></a>

If dependency discovery is not returning expected results, review the following common issues:
+ **Discovery not returning expected dependencies for EC2 instances** – Verify the dependency uses DNS resolution (not a direct IP), confirm that the compute resources are in a VPC with a Route 53 resolver, and check that the dependency was called within the 35-day lookback window.
+ **Discovery not returning expected dependencies for ECS Fargate** – Verify that Service topology includes the VPC for the ECS Fargate Service.
+ **Discovery not returning expected dependencies for Lambda functions** – Verify that the Lambda functions are VPC-connected, and that Service topology includes the VPC.
+ **Unexpected cross-region dependencies** – Cross-region dependencies are flagged automatically in the console. Common causes include hardcoded regional endpoints in application code, AWS SDK clients configured for a specific region, and third-party services routing to non-local endpoints.
+ **Dependencies appearing for the wrong service** – This typically occurs with shared VPCs or Amazon EKS clusters. Verify that compute resource attribution is correctly mapping resources to services.

For additional troubleshooting guidance, see [Troubleshooting Next generation Resilience Hub](next-gen-troubleshooting.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
