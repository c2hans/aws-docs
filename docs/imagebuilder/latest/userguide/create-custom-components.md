---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-custom-components.html
---

# Develop custom components for your Image Builder image
<a name="create-custom-components"></a>

You can create your own components to customize your Image Builder images according to your exact specifications. Use the following steps to develop custom components for your Image Builder image or container recipes.

1. If you want to develop your component document and validate it locally, you can install the AWS Task Orchestrator and Executor (AWSTOE) application and set it up on your local machine. For more information, see [Manual set up to develop custom components with AWSTOE](toe-get-started.md).

1. Create a component document that uses the AWSTOE component document framework. For more information about the document framework, see [Use the AWSTOE component document framework for custom components](toe-use-documents.md).

1. Specify your component document when you create a custom component. For more information, see [Create a custom component with Image Builder](create-component.md).

**Topics**
+ [Create a YAML component document for custom components in Image Builder](create-component-yaml.md)
+ [Create a custom component with Image Builder](create-component.md)

**Note**
To avoid unexpected charges, make sure to clean up resources and pipelines that you created from the examples in this guide. For more information about deleting resources in Image Builder, see [Delete outdated or unused Image Builder resources](delete-resources.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
