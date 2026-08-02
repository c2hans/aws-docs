---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/cicd-and-automation.html
---

# CI/CD and automation for serverless AI
<a name="cicd-and-automation"></a>

In traditional software development, continuous integration and deployment (CI/CD) enables teams to test and release changes rapidly and safely. In serverless AI systems, CI/CD becomes even more critical because of the ephemeral, event-driven nature of services and the volatile behavior of AI models and prompts.

From infrastructure (for example, AWS Lambda, Amazon API Gateway, and Amazon Bedrock agents) to logic (for example, prompts, RAG flows, and agent tool configurations), everything must be versioned and tested. Then these components should be deployed consistently across environments.

Without implementing CI/CD practices, organizations face the following risks:
+ Human error increases because of manual AWS Identity and Access Management (IAM) or prompt changes.
+ Model and infrastructure drift occurs across development/test/production environments.
+ Testing bottlenecks slow innovation.
+ Unvalidated updates create a risk of downtime or behavior changes.

## CI/CD capabilities in serverless AI
<a name="ci-cd-capabilities-in-serverless-ai.72316321-862f-5a7c-acda-a03b33bc4648"></a>

CI/CD provides the following capabilities and their associated benefits in serverless AI:
+ **Safe prompt and agent versioning** – Prompts and agent configuration changes pass through review, test, and approval processes.
+ **Infrastructure reproducibility** – Infrastructure as code (IaC) using AWS Cloud Development Kit (AWS CDK) or AWS CloudFormation helps to ensure that environments are identical across stages.
+ **Integrated testing** – Run prompt tests, schema validation, and security checks before deployment.
+ **Automated deployment approvals** – Use guardrails for production promotion, including manual review and automated metrics.
+ **Rollback and audit** – Tagged versions allow rapid rollback and compliance traceability.
+ **Frequent low–risk updates** – Enables fast iteration cycles for large language model (LLM) applications and prompt tuning.

## Typical CI/CD workflow for serverless AI projects
<a name="typical-ci-cd-workflow-for-serverless-ai-projects.10fab3b1-f3f8-5390-8d2f-0e12ba9526fa"></a>

A comprehensive CI/CD pipeline for serverless AI projects involves multiple stages. The following list outlines each stage of a typical CI/CD workflow, including associated actions and example tooling:
+ **Code and prompt commit** – Developer pushes updated Lambda function, AWS CDK code, or prompt text to Git by using tools like GitHub or GitLab.
+ **Build and lint** – Validate syntax, prompt format, and schema alignment by using tools such as [ESLint](https://eslint.org/) for JavaScript, [Black](https://pypi.org/project/black/) for Python, [yamllint](https://yamllint.readthedocs.io/en/stable/), and custom prompt validators.
+ **Unit tests and prompt regression** – Run local logic and unit tests and golden prompt-response tests by using [pytest](https://docs.pytest.org/en/stable/), [promptfoo](https://www.promptfoo.dev/docs/intro/), and custom fixtures.
+ **IaC validation** – Synthesize and validate AWS CDK and CloudFormationtemplates by using `cdk synth` and `cfn–lint`.
+ **Integration test** – Deploy to staging and invoke full workflow (for example, Amazon S3 upload to Amazon Bedrock agent) by using AWS CodeBuild and mocked agents.
+ **Manual or auto approval** – Review model cost impact and approval checklist (for example, prompt change) by using AWS CodePipeline or GitHub Actions gates.
+ **Deploy to production** – Promote stacks, update Amazon Bedrock agent configs, and publish prompts by using AWS CodeDeploy, AWS CDK, and the AWS SAM command line interface (CLI).
+ **Post–deployment smoke test** – Validate production agent outputs, log capture, and rollback readiness by using Amazon CloudWatch Synthetics and test Lambda.
+ **Monitor and observe** – Auto-create dashboards, cost alerts, and token usage monitors by using CloudWatch, Amazon Bedrock token logs (through CloudWatch), and AWS X-Ray.

## CI/CD for prompts and Amazon Bedrock agents
<a name="ci-cd-for-prompts-and-9999999999999999br--agents.d573e453-90ea-56f9-99c6-5211eb70e279"></a>

Prompt and Amazon Bedrock agent configurations require special handling in the CI/CD process:
+ Treat prompts as versioned assets in source control (for example, `/prompts/v1/agent-support-en.yaml`).
+ Include prompts in automated golden test cases.
+ Deploy Amazon Bedrock agent configurations (including tools, instructions, and knowledge base URIs) by using IaC templates.
+ Deploy Amazon Bedrock agent updates only when:
  + Prompt regression tests pass.
  + Tool permissions match IAM templates.
  + Confidence thresholds or validation Lambda results meet acceptable criteria.

This approach prevents silent prompt degradation and ensures repeatable generative AI behavior in production.

## Integrating AgentCore with CI/CD pipelines
<a name="integrating-9999999999999999brac--with-ci-cd-pipelines.d7a9155c-f73e-5a3c-b350-2bbf06d0a8ee"></a>

Amazon Bedrock AgentCore extends traditional CI/CD automation by introducing a managed runtime and memory fabric for agent deployment, testing, and evolution. Current serverless pipelines automate the packaging and deployment of agent code (for example, through AWS CodePipeline, AWS CodeBuild, or the AWS CDK), However, AgentCoreintegrates directly into this process to manage agent state, memory, and tool connectors as part of the deployment lifecycle.

Key integration points of AgentCore with CI/CD pipelines are the following:
+ R**untime registration and versioning** – Each deployed agent can be registered with AgentCore Runtime, which handles scaling, routing, and lifecycle orchestration. This approach replaces the need for maintaining custom registries or service discovery logic in CI/CD workflows.
+ **Memory snapshots and promotion** – During automated testing, AgentCore can persist agent memory snapshots, including learned context or state, and promote them alongside code artifacts through the pipeline. This capability enables *context continuity* between development, staging, and production environments.
+ **Tools configuration management** – Using AgentCore Gateway tools, teams can define integration points with other AWS services (for example, DynamoDB, Amazon S3, Amazon Bedrock FMs, or EventBridge) declaratively within the same pipeline. This configuration management capability helps provide consistent and auditable access configuration.
+ **Observability hooks for validation** – AgentCore exposes built-in telemetry for agent execution, enabling CI/CD pipelines to automatically validate performance, reasoning quality, and compliance metrics before deployment.

A CodePipeline deployment might consist of the following steps:

1. Build new agent code using AWS CodeBuild.

1. Deploy the agent to AgentCore Runtime for execution.

1. Run automated integration tests that use AgentCore Memory to persist and compare state across runs.

1. Promote successful builds to production while updating AgentCore registries for discovery and orchestration.

## AWS services for CI/CD tooling
<a name="9999999999999999aws-services--for-ci-cd-tooling.313e5cfe-d88a-5686-b99f-79b49bbbf272"></a>

The following AWS services support CI/CD implementation for serverless AI:
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) provides end-to-end pipeline capabilities for code, prompts, and infrastructure.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) runs tests, linting, and validation.
+ [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) and [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), as well as HashiCorp [Terraform ](https://www.terraform.io/docs)(a third-party tool), define infrastructure, agents, permissions, and workflows.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) stores versioned prompt files and agent templates.
+ [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) API and CLI register prompts and agent definitions dynamically.
+ [CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) performs post-deployment probes and confidence validation.
+ [Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html) and [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) trigger CI/CD from monitored events such as drift and deployment failure.

## Summary of CI/CD and automation
<a name="summary-of-ci-cd-and-automation.4e69f361-3985-5a37-b69d-7bdd14090f75"></a>

CI/CD is not just a best practice—it is a necessity for scaling safe and reliable AI systems. With prompt sensitivity, tool autonomy, and infrastructure complexity, automation provides several important benefits:
+ Faster innovation cycles with reduced risk
+ Governable and auditable updates
+ Stable environments across teams and regions
+ Integrated testing for both logic and language

With Amazon Bedrock AgentCore integrated into CI/CD pipelines, agent deployment evolves from code delivery to continuous capability delivery. Reasoning, memory, and state become first-class deployable assets in modern serverless AI systems.

By applying DevOps principles to AI-native architectures, enterprises can bring AI to production responsibly, at speed and at scale.
