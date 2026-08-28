---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-parameterdetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent ParameterDetail
<a name="aws-properties-bedrock-agent-parameterdetail"></a>

 Contains details about a parameter in a function for an action group.

## Syntax
<a name="aws-properties-bedrock-agent-parameterdetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-parameterdetail-syntax.json"></a>

```
{
  "[Description](#cfn-bedrock-agent-parameterdetail-description)" : {{String}},
  "[Required](#cfn-bedrock-agent-parameterdetail-required)" : {{Boolean}},
  "[Type](#cfn-bedrock-agent-parameterdetail-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-parameterdetail-syntax.yaml"></a>

```
  [Description](#cfn-bedrock-agent-parameterdetail-description): {{String}}
  [Required](#cfn-bedrock-agent-parameterdetail-required): {{Boolean}}
  [Type](#cfn-bedrock-agent-parameterdetail-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-agent-parameterdetail-properties"></a>

`Description`  <a name="cfn-bedrock-agent-parameterdetail-description"></a>
 A description of the parameter. Helps the foundation model determine how to elicit the parameters from the user.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Required`  <a name="cfn-bedrock-agent-parameterdetail-required"></a>
 Whether the parameter is required for the agent to complete the function for action group invocation.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-agent-parameterdetail-type"></a>
 The data type of the parameter.
*Required*: Yes
*Type*: String
*Allowed values*: `string | number | integer | boolean | array`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
