---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-predefinedattribute-values.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::PredefinedAttribute Values
<a name="aws-properties-connect-predefinedattribute-values"></a>

The values of a predefined attribute.

## Syntax
<a name="aws-properties-connect-predefinedattribute-values-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-predefinedattribute-values-syntax.json"></a>

```
{
  "[StringList](#cfn-connect-predefinedattribute-values-stringlist)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-predefinedattribute-values-syntax.yaml"></a>

```
  [StringList](#cfn-connect-predefinedattribute-values-stringlist): {{
    - String}}
```

## Properties
<a name="aws-properties-connect-predefinedattribute-values-properties"></a>

`StringList`  <a name="cfn-connect-predefinedattribute-values-stringlist"></a>
Predefined attribute values of type string list.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
