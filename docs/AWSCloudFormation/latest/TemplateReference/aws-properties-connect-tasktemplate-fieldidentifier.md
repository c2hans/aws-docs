---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-tasktemplate-fieldidentifier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::TaskTemplate FieldIdentifier
<a name="aws-properties-connect-tasktemplate-fieldidentifier"></a>

The identifier of the task template field.

## Syntax
<a name="aws-properties-connect-tasktemplate-fieldidentifier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-tasktemplate-fieldidentifier-syntax.json"></a>

```
{
  "[Name](#cfn-connect-tasktemplate-fieldidentifier-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-tasktemplate-fieldidentifier-syntax.yaml"></a>

```
  [Name](#cfn-connect-tasktemplate-fieldidentifier-name): {{String}}
```

## Properties
<a name="aws-properties-connect-tasktemplate-fieldidentifier-properties"></a>

`Name`  <a name="cfn-connect-tasktemplate-fieldidentifier-name"></a>
The name of the task template field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
