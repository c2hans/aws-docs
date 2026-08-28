---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/using-configuration-files.html
---

# Using configuration files
<a name="using-configuration-files"></a>

Landing Zone Accelerator on AWS includes seven configuration files that you can use to customize the solution. Six of the files are mandatory. The `customizations-config.yaml` file is for optional extensions of the core solution. The solution orchestrates the creation of resources and configurations based on the input from the configuration files. Resources are generated using AWS CDK constructs defined in the solution’s source code.

Having your configuration in a Git-compatible repository introduces the following benefits:
+ You can use version control for your configuration like you would for source code. You can introduce feature branching and other commonly-used strategies to ensure changes to the environment meet your standards.
+ You can audit the change history of the configuration files.
+ The files serve as declarative manifests for your environment’s configuration. The `AWSAccelerator-Pipeline` sources changes to the main branch of the repository and orchestrates your defined configuration properties with CodeBuild projects and the AWS CDK toolkit. Users who make edits to these configuration files aren’t required to know how to write code.
+ Because the repository is hosted in CodeCommit, you can use IAM to define which users and roles can view or make changes to the repository. You can use this strategy as a gate to allow members in your organization to make changes to the environment.

## Configuration file descriptions
<a name="configuration-file-descriptions"></a>
+  **accounts-config.yaml** - Used to manage all of the AWS accounts within the AWS Organization. Adding a new account to this configuration file invokes the account creation process from Landing Zone Accelerator on AWS.
+  **customizations-config.yaml (optional)** - Used to manage configuration of custom applications, third-party firewall appliances, and CloudFormation stacks.
+  **global-config.yaml** - Used to manage all of the global properties that can be inherited across the AWS Organization.
+  **iam-config.yaml** - Used to manage all of the IAM resources across the AWS Organization.
+  **network-config.yaml** - Used to manage and implement network resources to establish a WAN/LAN architecture to support cloud operations and application workloads in AWS.
+  **organization-config.yaml** - Used to manage all of the organization units in the AWS Organization.
+  **replacements-config.yaml (optional)** - Used to manage all of the replacement values across the configuration files, see [Parameter Store reference variable](working-with-solution-specific-variables.md#parameter-store-reference-variable) for more details.
+  **security-config.yaml -** Used to manage configuration of AWS security services.

## Using JSON schema
<a name="using-json-schema"></a>

Landing Zone Accelerator on AWS fully supports JSON Schema, empowering you with enhanced configuration validation and auto-completion directly in your IDE.
+  **Validation**: Configuration files are validated in real-time as you type, reducing syntax errors and improving your feedback loop. If any of your configuration files contain an error that does not align with the Landing Zone Accelerator on AWS schema, you will know immediately before pushing your config to your git-compatible repository.
+  **Auto-Completion**: As you type, you will receive suggestions for configurations straight from the schema, making it easier and faster to edit Landing Zone Accelerator on AWS configuration files.
+  **Discoverability**: By exploring each Landing Zone Accelerator on AWS configuration file using the schema, you can discover what options are available to you without ever leaving the IDE. For example, you can highlight any of the Landing Zone Accelerator on AWS configuration entries to view a description of it. You can also, initiate a suggestion (Ctrl/Cmd\+Space in VSCode) anywhere in the Landing Zone Accelerator on AWS configuration code to show available options to you.

This feature is designed to enhance the experience of working with the Landing Zone Accelerator on AWS configuration files and is immediately available. To take advantage of this, open the Landing Zone Accelerator on AWS configuration files in an editor that supports JSON schema.

The following are examples of validated IDEs:
+ VSCode: requires YAML extension
+ IntelliJ

## Configuration file API reference
<a name="configuration-file-api-reference"></a>

A full reference for this solution’s configuration API is available in the [Services, Features, and Configuration References section](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/user-guide/config/) of the solution’s [GitHub Pages website](https://awslabs.github.io/landing-zone-accelerator-on-aws/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
