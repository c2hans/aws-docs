---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-functionschema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent FunctionSchema
<a name="aws-properties-bedrock-agent-functionschema"></a>

 Contains details about the function schema for the action group or the JSON or YAML-formatted payload defining the schema.

## Syntax
<a name="aws-properties-bedrock-agent-functionschema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-functionschema-syntax.json"></a>

```
{
  "[Functions](#cfn-bedrock-agent-functionschema-functions)" : {{[ Function, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-functionschema-syntax.yaml"></a>

```
  [Functions](#cfn-bedrock-agent-functionschema-functions): {{
    - Function}}
```

## Properties
<a name="aws-properties-bedrock-agent-functionschema-properties"></a>

`Functions`  <a name="cfn-bedrock-agent-functionschema-functions"></a>
 A list of functions that each define an action in the action group.
*Required*: Yes
*Type*: Array of [Function](aws-properties-bedrock-agent-function.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
