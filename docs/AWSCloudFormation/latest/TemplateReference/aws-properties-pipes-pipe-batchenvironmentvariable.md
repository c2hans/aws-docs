---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-batchenvironmentvariable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe BatchEnvironmentVariable
<a name="aws-properties-pipes-pipe-batchenvironmentvariable"></a>

The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition.

**Note**
Environment variables cannot start with "` AWS Batch `". This naming convention is reserved for variables that AWS Batch sets.

## Syntax
<a name="aws-properties-pipes-pipe-batchenvironmentvariable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-batchenvironmentvariable-syntax.json"></a>

```
{
  "[Name](#cfn-pipes-pipe-batchenvironmentvariable-name)" : {{String}},
  "[Value](#cfn-pipes-pipe-batchenvironmentvariable-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-batchenvironmentvariable-syntax.yaml"></a>

```
  [Name](#cfn-pipes-pipe-batchenvironmentvariable-name): {{String}}
  [Value](#cfn-pipes-pipe-batchenvironmentvariable-value): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-batchenvironmentvariable-properties"></a>

`Name`  <a name="cfn-pipes-pipe-batchenvironmentvariable-name"></a>
The name of the key-value pair. For environment variables, this is the name of the environment variable.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-pipes-pipe-batchenvironmentvariable-value"></a>
The value of the key-value pair. For environment variables, this is the value of the environment variable.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
