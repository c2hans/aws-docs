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
