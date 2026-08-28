---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml-workflow-framework.html
---

# OpenSearch Service flow framework templates
<a name="ml-workflow-framework"></a>

Amazon OpenSearch Service flow framework templates allow you to automate complex OpenSearch Service setup and preprocessing tasks by providing templates for common use cases. For example, you can use flow framework templates to automate machine learning setup tasks. Amazon OpenSearch Service flow framework templates provide a compact description of the setup process in a JSON or YAML document. These templates describe automated workflow configurations for conversational chat or query generation, AI connectors, tools, agents, and other components that prepare OpenSearch Service for backend use for generative models.

Amazon OpenSearch Service flow framework templates can be customized to meet your specific needs. To see an example of a custom flow framework template, see [flow-framework](https://github.com/opensearch-project/flow-framework/blob/main/sample-templates/deploy-bedrock-claude-model.json). For OpenSearch Service provided templates, see [workflow-templates](https://opensearch.org/docs/2.13/automating-configurations/workflow-templates/). For comprehensive documentation, including detailed steps, an API reference, and a reference of all available settings, see [automating configuration](https://github.com/opensearch-project/flow-framework/blob/main/sample-templates/deploy-bedrock-claude-model.json) in the open source OpenSearch documentation.

**Note**
Flow-framework does not support backend role filtering for OpenSearch Service 2.17.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
