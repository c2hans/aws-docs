---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-tasktemplate-defaultfieldvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::TaskTemplate DefaultFieldValue
<a name="aws-properties-connect-tasktemplate-defaultfieldvalue"></a>

Describes a default field and its corresponding value.

## Syntax
<a name="aws-properties-connect-tasktemplate-defaultfieldvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-tasktemplate-defaultfieldvalue-syntax.json"></a>

```
{
  "[DefaultValue](#cfn-connect-tasktemplate-defaultfieldvalue-defaultvalue)" : {{String}},
  "[Id](#cfn-connect-tasktemplate-defaultfieldvalue-id)" : {{FieldIdentifier}}
}
```

### YAML
<a name="aws-properties-connect-tasktemplate-defaultfieldvalue-syntax.yaml"></a>

```
  [DefaultValue](#cfn-connect-tasktemplate-defaultfieldvalue-defaultvalue): {{String}}
  [Id](#cfn-connect-tasktemplate-defaultfieldvalue-id): {{
    FieldIdentifier}}
```

## Properties
<a name="aws-properties-connect-tasktemplate-defaultfieldvalue-properties"></a>

`DefaultValue`  <a name="cfn-connect-tasktemplate-defaultfieldvalue-defaultvalue"></a>
Default value for the field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-connect-tasktemplate-defaultfieldvalue-id"></a>
Identifier of a field.
*Required*: Yes
*Type*: [FieldIdentifier](aws-properties-connect-tasktemplate-fieldidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
