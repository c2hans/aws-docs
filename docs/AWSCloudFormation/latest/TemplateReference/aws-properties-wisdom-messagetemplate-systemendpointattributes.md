---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-messagetemplate-systemendpointattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplate SystemEndpointAttributes
<a name="aws-properties-wisdom-messagetemplate-systemendpointattributes"></a>

The system endpoint attributes that are used with the message template.

## Syntax
<a name="aws-properties-wisdom-messagetemplate-systemendpointattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-messagetemplate-systemendpointattributes-syntax.json"></a>

```
{
  "[Address](#cfn-wisdom-messagetemplate-systemendpointattributes-address)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-messagetemplate-systemendpointattributes-syntax.yaml"></a>

```
  [Address](#cfn-wisdom-messagetemplate-systemendpointattributes-address): {{String}}
```

## Properties
<a name="aws-properties-wisdom-messagetemplate-systemendpointattributes-properties"></a>

`Address`  <a name="cfn-wisdom-messagetemplate-systemendpointattributes-address"></a>
The customer's phone number if used with `customerEndpoint`, or the number the customer dialed to call your contact center if used with `systemEndpoint`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
