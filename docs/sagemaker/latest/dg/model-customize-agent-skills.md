---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-agent-skills.html
---

# Model customization agent skills
<a name="model-customize-agent-skills"></a>

To accelerate model customization workflows, you can use a comprehensive set of Amazon SageMaker AI agent Skills designed to work with AI coding assistants that support skills, such as Kiro and Claude Code. These Skills direct coding assistants, in an IDE or at command line, to orchestrate model customization tasks, such as use case specification and planning, dataset transformation, customization technique selection, fine-tuning, model evaluation, and model deployment with options for Amazon SageMaker AI and Amazon Bedrock, according to Amazon SageMaker AI best practices. You can describe your use case and preferred workflow in natural language to your coding assistant which, guided by Amazon SageMaker AI skills, outputs code constructs that handle the invocation and orchestration of Amazon SageMaker AI APIs and MCP tools.

Amazon SageMaker AI skills are distributed as an open-source agent plugin through the AWS Agent Plugins GitHub repository, maintained by AWSLabs. By adhering to the standard SKILL.md format defined by the Agent Skills open standard, these skills remain portable across any compatible coding environment.

## Getting started
<a name="agent-skills-getting-started"></a>

Access the Amazon SageMaker AI agent skills through the [AWSLabs Agent Plugins repository](https://github.com/awslabs/agent-plugins) on the GitHub website. In Claude Code or Cursor install the `sagemaker-ai` plugin. For coding assistants that don't support agent plugins directly (for example, Kiro CLI or IDE as of Mar 2026), install the MCP server and Skills separately as detailed in the [sagemaker-ai plugin README](https://github.com/awslabs/agent-plugins/tree/main/plugins/sagemaker-ai) on the GitHub website.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
