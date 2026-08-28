---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-tasktemplate-invisiblefieldinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::TaskTemplate InvisibleFieldInfo
<a name="aws-properties-connect-tasktemplate-invisiblefieldinfo"></a>

A field that is invisible to an agent.

## Syntax
<a name="aws-properties-connect-tasktemplate-invisiblefieldinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-tasktemplate-invisiblefieldinfo-syntax.json"></a>

```
{
  "[Id](#cfn-connect-tasktemplate-invisiblefieldinfo-id)" : {{FieldIdentifier}}
}
```

### YAML
<a name="aws-properties-connect-tasktemplate-invisiblefieldinfo-syntax.yaml"></a>

```
  [Id](#cfn-connect-tasktemplate-invisiblefieldinfo-id): {{
    FieldIdentifier}}
```

## Properties
<a name="aws-properties-connect-tasktemplate-invisiblefieldinfo-properties"></a>

`Id`  <a name="cfn-connect-tasktemplate-invisiblefieldinfo-id"></a>
Identifier of the invisible field.
*Required*: Yes
*Type*: [FieldIdentifier](aws-properties-connect-tasktemplate-fieldidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
