---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::NotebookInstanceLifecycleConfig NotebookInstanceLifecycleHook
<a name="aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook"></a>

Specifies the notebook instance lifecycle configuration script. Each lifecycle configuration script has a limit of 16384 characters.

## Syntax
<a name="aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook-syntax.json"></a>

```
{
  "[Content](#cfn-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook-content)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook-syntax.yaml"></a>

```
  [Content](#cfn-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook-content): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook-properties"></a>

`Content`  <a name="cfn-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook-content"></a>
A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
*Required*: No
*Type*: String
*Pattern*: `[\S\s]+`
*Minimum*: `1`
*Maximum*: `16384`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
