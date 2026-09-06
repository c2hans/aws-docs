---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/cloudformation-template.html
---

# Create a AWS CloudFormation template using the AWS Toolkit for Visual Studio Code
<a name="cloudformation-template"></a>

The AWS Toolkit for Visual Studio Code can assist you in writing AWS CloudFormation and SAM templates.

## Prerequisites
<a name="cloudformation-template-prereq"></a>

### Toolkit for VS Code and credential prerequisites
<a name="w2aac17c25b9b7b3"></a>
+ Before you can access the CloudFormation service from the Toolkit for VS Code, you need to meet the requirements outlined in the the userguide [Installing the Toolkit for VS Code](setup-toolkit.md#setup-prereq).
+ The credentials you created in [Authentication and access](establish-credentials.md) must include appropriate read/write access to the AWS CloudFormation service.
**Note**
If the **CloudFormation** service displays an **Error loading CloudFormation resources** message, check the permissions you've attached to those credentials. Also note that Changes made to permissions may take a few minutes to update in the **AWS Explorer**.

### CloudFormation template prerequisites
<a name="w2aac17c25b9b7b5"></a>
+ Install and enable the [Redhat Developer YAML VS Code](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) extension.
+ You need to be connected to the internet when using the Redhat Developer YAML VS Code extension because it's used to download and cache JSON schemas on your machine.

## Writing a CloudFormation template with YAML Schema Support
<a name="tamplate-schema"></a>

The toolkit uses YAML language support and JSON schemas to streamline the process of writing CloudFormation and SAM templates. Features like syntax validation and autocompletion not only make the process faster, but also help improve the quality of your template. When selecting a schema for your template, the following are recommended best practices.

**CloudFormation template**
+ File has a .yaml or .yml extension.
+ The file has a top-level `AWSTemplateFormatVersion` or **Resources** node.

**SAM Template**
+ All of the criteria already described for CloudFormation
+ The file has a top-level **Transform** node, containing a value that begins with `AWS::Serverless`.

The schema will be applied upon file modification. For example, a SAM Template schema will be applied after adding a serverless transform to a CloudFormation template and saving the file.

### Syntax Validation
<a name="w2aac17c25b9c11c11"></a>

The YAML extension will automatically apply type validation to your template. This highlights entries with invalid types for a given property. If you hover over a highlighted entry, the extensions displays corrective actions.

### Autocompletion
<a name="w2aac17c25b9c11c13"></a>

When adding new fields, enumerated values, or other [resource types](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html#resources-section-structure-resource-fields), you can initiate the YAML extension's autocompletion feature by typing **Ctrl \+ space**.
