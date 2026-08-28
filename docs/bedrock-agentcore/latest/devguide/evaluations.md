---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html
---

# Evaluate agent performance with Amazon Bedrock AgentCore Evaluations
<a name="evaluations"></a>

Amazon Bedrock AgentCore Evaluations provides automated assessment tools to measure how well your agent or tools perform specific tasks, handle edge cases, and maintain consistency across different inputs and contexts. The service enables data-driven optimization and ensures your agents meet quality standards before and after deployment.

AgentCore Evaluations integrates with popular agent frameworks including **Strands** and **LangGraph** with **OpenTelemetry** and **OpenInference** instrumentation libraries. Under the hood, traces from these agents are converted to a unified format and scored using LLM-as-a-Judge techniques for both built-in and custom evaluators.

Each evaluator has a unique Amazon Resource Name (ARN) and resource policy attached to it. Evaluator ARNs follow these formats:

```
arn:aws:bedrock-agentcore:::evaluator/Builtin.Helpfulness (for built-in evaluators)
```

```
arn:aws:bedrock-agentcore:region:account:evaluator/my-evaluator-id (for custom evaluators)
```

Built-in evaluators are public and accessible to all users. Custom evaluation resources are private and can only be accessed by users who are explicitly granted access. To grant access, you can use IAM resource-based policies for evaluators and evaluation configurations, and IAM identity-based policies for users and roles.

By default, you can create up to 1,000 evaluation configurations per AWS Region in an AWS account. The service supports up to 1 million input and output tokens per minute per account for large regions.

**Topics**
+ [How it works](how-it-works-evaluations.md)
+ [Telemetry setup and delivery](supported-frameworks-telemetry.md)
+ [Supported agent frameworks](supported-frameworks.md)
+ [Built-in evaluators](built-in-evaluators-overview.md)
+ [Third-party evaluators](third-party-evaluators.md)
+ [Custom evaluators](custom-evaluators.md)
+ [Online evaluation](online-evaluations.md)
+ [On-demand evaluation](on-demand-evaluations.md)
+ [Batch evaluation](batch-evaluations.md)
+ [Dataset evaluation](dataset-evaluations.md)
+ [Simulation](simulation.md)
+ [Diagnose AgentCore Evaluation issues with an AI coding assistant](diagnose-evaluation-issues.md)
+ [Encryption at rest for AgentCore Evaluations](evaluations-encryption.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
