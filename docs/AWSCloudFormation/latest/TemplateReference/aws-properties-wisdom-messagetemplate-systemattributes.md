---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-messagetemplate-systemattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplate SystemAttributes
<a name="aws-properties-wisdom-messagetemplate-systemattributes"></a>

The system attributes that are used with the message template.

## Syntax
<a name="aws-properties-wisdom-messagetemplate-systemattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-messagetemplate-systemattributes-syntax.json"></a>

```
{
  "[CustomerEndpoint](#cfn-wisdom-messagetemplate-systemattributes-customerendpoint)" : {{SystemEndpointAttributes}},
  "[Name](#cfn-wisdom-messagetemplate-systemattributes-name)" : {{String}},
  "[SystemEndpoint](#cfn-wisdom-messagetemplate-systemattributes-systemendpoint)" : {{SystemEndpointAttributes}}
}
```

### YAML
<a name="aws-properties-wisdom-messagetemplate-systemattributes-syntax.yaml"></a>

```
  [CustomerEndpoint](#cfn-wisdom-messagetemplate-systemattributes-customerendpoint): {{
    SystemEndpointAttributes}}
  [Name](#cfn-wisdom-messagetemplate-systemattributes-name): {{String}}
  [SystemEndpoint](#cfn-wisdom-messagetemplate-systemattributes-systemendpoint): {{
    SystemEndpointAttributes}}
```

## Properties
<a name="aws-properties-wisdom-messagetemplate-systemattributes-properties"></a>

`CustomerEndpoint`  <a name="cfn-wisdom-messagetemplate-systemattributes-customerendpoint"></a>
The CustomerEndpoint attribute.
*Required*: No
*Type*: [SystemEndpointAttributes](aws-properties-wisdom-messagetemplate-systemendpointattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-wisdom-messagetemplate-systemattributes-name"></a>
The name of the task.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SystemEndpoint`  <a name="cfn-wisdom-messagetemplate-systemattributes-systemendpoint"></a>
The SystemEndpoint attribute.
*Required*: No
*Type*: [SystemEndpointAttributes](aws-properties-wisdom-messagetemplate-systemendpointattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
