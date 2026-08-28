---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-numbervalidation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory NumberValidation
<a name="aws-properties-bedrockagentcore-memory-numbervalidation"></a>

Validation for NUMBER fields.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-numbervalidation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-numbervalidation-syntax.json"></a>

```
{
  "[MaxValue](#cfn-bedrockagentcore-memory-numbervalidation-maxvalue)" : {{Number}},
  "[MinValue](#cfn-bedrockagentcore-memory-numbervalidation-minvalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-numbervalidation-syntax.yaml"></a>

```
  [MaxValue](#cfn-bedrockagentcore-memory-numbervalidation-maxvalue): {{Number}}
  [MinValue](#cfn-bedrockagentcore-memory-numbervalidation-minvalue): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-numbervalidation-properties"></a>

`MaxValue`  <a name="cfn-bedrockagentcore-memory-numbervalidation-maxvalue"></a>
Maximum allowed value.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinValue`  <a name="cfn-bedrockagentcore-memory-numbervalidation-minvalue"></a>
Minimum allowed value.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
