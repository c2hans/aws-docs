---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-imageconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function ImageConfig
<a name="aws-properties-lambda-function-imageconfig"></a>

Configuration values that override the container image Dockerfile settings. For more information, see [Container image settings](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-parms).

## Syntax
<a name="aws-properties-lambda-function-imageconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-imageconfig-syntax.json"></a>

```
{
  "[Command](#cfn-lambda-function-imageconfig-command)" : {{[ String, ... ]}},
  "[EntryPoint](#cfn-lambda-function-imageconfig-entrypoint)" : {{[ String, ... ]}},
  "[WorkingDirectory](#cfn-lambda-function-imageconfig-workingdirectory)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-function-imageconfig-syntax.yaml"></a>

```
  [Command](#cfn-lambda-function-imageconfig-command): {{
    - String}}
  [EntryPoint](#cfn-lambda-function-imageconfig-entrypoint): {{
    - String}}
  [WorkingDirectory](#cfn-lambda-function-imageconfig-workingdirectory): {{String}}
```

## Properties
<a name="aws-properties-lambda-function-imageconfig-properties"></a>

`Command`  <a name="cfn-lambda-function-imageconfig-command"></a>
Specifies parameters that you want to pass in with ENTRYPOINT. You can specify a maximum of 1,500 parameters in the list.
*Required*: No
*Type*: Array of String
*Maximum*: `1500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EntryPoint`  <a name="cfn-lambda-function-imageconfig-entrypoint"></a>
Specifies the entry point to their application, which is typically the location of the runtime executable. You can specify a maximum of 1,500 string entries in the list.
*Required*: No
*Type*: Array of String
*Maximum*: `1500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkingDirectory`  <a name="cfn-lambda-function-imageconfig-workingdirectory"></a>
Specifies the working directory. The length of the directory string cannot exceed 1,000 characters.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
