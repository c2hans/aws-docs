---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-tasktemplate-field.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::TaskTemplate Field
<a name="aws-properties-connect-tasktemplate-field"></a>

Describes a single task template field.

## Syntax
<a name="aws-properties-connect-tasktemplate-field-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-tasktemplate-field-syntax.json"></a>

```
{
  "[Description](#cfn-connect-tasktemplate-field-description)" : {{String}},
  "[Id](#cfn-connect-tasktemplate-field-id)" : {{FieldIdentifier}},
  "[SingleSelectOptions](#cfn-connect-tasktemplate-field-singleselectoptions)" : {{[ String, ... ]}},
  "[Type](#cfn-connect-tasktemplate-field-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-tasktemplate-field-syntax.yaml"></a>

```
  [Description](#cfn-connect-tasktemplate-field-description): {{String}}
  [Id](#cfn-connect-tasktemplate-field-id): {{
    FieldIdentifier}}
  [SingleSelectOptions](#cfn-connect-tasktemplate-field-singleselectoptions): {{
    - String}}
  [Type](#cfn-connect-tasktemplate-field-type): {{String}}
```

## Properties
<a name="aws-properties-connect-tasktemplate-field-properties"></a>

`Description`  <a name="cfn-connect-tasktemplate-field-description"></a>
The description of the field.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-connect-tasktemplate-field-id"></a>
The unique identifier for the field.
*Required*: Yes
*Type*: [FieldIdentifier](aws-properties-connect-tasktemplate-fieldidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SingleSelectOptions`  <a name="cfn-connect-tasktemplate-field-singleselectoptions"></a>
A list of options for a single select field.
*Required*: No
*Type*: Array of String
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-connect-tasktemplate-field-type"></a>
Indicates the type of field. Following are the valid field types: `NAME``DESCRIPTION` \| `SCHEDULED_TIME` \| `QUICK_CONNECT` \| `URL` \| `NUMBER` \| `TEXT` \| `TEXT_AREA` \| `DATE_TIME` \| `BOOLEAN` \| `SINGLE_SELECT` \| `EMAIL`
*Required*: Yes
*Type*: String
*Allowed values*: `NAME | DESCRIPTION | SCHEDULED_TIME | QUICK_CONNECT | URL | NUMBER | TEXT | TEXT_AREA | DATE_TIME | BOOLEAN | SINGLE_SELECT | EMAIL | EXPIRY_DURATION | SELF_ASSIGN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
