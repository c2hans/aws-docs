---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-exclusions.html
---

# Exclusions
<a name="deployment-guardrails-exclusions"></a>

When doing a blue/green or rolling deployment, your new endpoint configuration must have the same variant name as the old endpoint configuration. There are also feature-based exclusions that make your endpoint incompatible with deployment guardrails at this time. If your endpoint uses any of the following features, you cannot use deployment guardrails on your endpoint, and your endpoint will fall back to using a blue/green deployment with all at once traffic shifting and no final baking period:
+ Marketplace containers
+ Endpoints that use Inf1 (Inferentia-based) instances

If you're doing a rolling deployment, there are additional feature-based exclusions:
+ Serverless inference endpoints
+ Multi-variant inference endpoints

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
