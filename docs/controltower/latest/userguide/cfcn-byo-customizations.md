---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/cfcn-byo-customizations.html
---

# Build your own customizations
<a name="cfcn-byo-customizations"></a>

To build your own customizations, you can modify the CfCT `manifest.yaml` file by adding or updating service control policies (SCPs), resource control policies (RCPs), and CloudFormation resources. For resources that must be deployed, you can add or remove accounts and OUs. You can add or modify the templates in the package folders, create your own folders, and reference the templates or folders in the `manifest.yaml` file.

This section explains the two main parts of building your own customizations:
+ how to set up your own configuration package for service control policies
+ how to set up your own configuration package for AWS CloudFormation stack sets

**JSON schema for the customization package**
The JSON schema for the customization package for CfCT is located in the [source code repository on GitHub](https://github.com/aws-solutions/aws-control-tower-customizations). You can use the schema with many of your favorite development tools, and you may find it helpful for reducing errors when you build your own CfCT `manifest.yaml` file.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
