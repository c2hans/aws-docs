---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-ephemeralstorage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function EphemeralStorage
<a name="aws-properties-lambda-function-ephemeralstorage"></a>

The size of the function's `/tmp` directory in MB. The default value is 512, but it can be any whole number between 512 and 10,240 MB.

## Syntax
<a name="aws-properties-lambda-function-ephemeralstorage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-ephemeralstorage-syntax.json"></a>

```
{
  "[Size](#cfn-lambda-function-ephemeralstorage-size)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-function-ephemeralstorage-syntax.yaml"></a>

```
  [Size](#cfn-lambda-function-ephemeralstorage-size): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-function-ephemeralstorage-properties"></a>

`Size`  <a name="cfn-lambda-function-ephemeralstorage-size"></a>
The size of the function's `/tmp` directory.
*Required*: Yes
*Type*: Integer
*Minimum*: `512`
*Maximum*: `10240`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
