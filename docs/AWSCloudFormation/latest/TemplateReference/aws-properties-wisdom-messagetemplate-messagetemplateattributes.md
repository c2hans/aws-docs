---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-messagetemplate-messagetemplateattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplate MessageTemplateAttributes
<a name="aws-properties-wisdom-messagetemplate-messagetemplateattributes"></a>

The attributes that are used with the message template.

## Syntax
<a name="aws-properties-wisdom-messagetemplate-messagetemplateattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-messagetemplate-messagetemplateattributes-syntax.json"></a>

```
{
  "[AgentAttributes](#cfn-wisdom-messagetemplate-messagetemplateattributes-agentattributes)" : {{AgentAttributes}},
  "[CustomAttributes](#cfn-wisdom-messagetemplate-messagetemplateattributes-customattributes)" : {{{{{Key}}: {{Value}}, ...}}},
  "[CustomerProfileAttributes](#cfn-wisdom-messagetemplate-messagetemplateattributes-customerprofileattributes)" : {{CustomerProfileAttributes}},
  "[SystemAttributes](#cfn-wisdom-messagetemplate-messagetemplateattributes-systemattributes)" : {{SystemAttributes}}
}
```

### YAML
<a name="aws-properties-wisdom-messagetemplate-messagetemplateattributes-syntax.yaml"></a>

```
  [AgentAttributes](#cfn-wisdom-messagetemplate-messagetemplateattributes-agentattributes): {{
    AgentAttributes}}
  [CustomAttributes](#cfn-wisdom-messagetemplate-messagetemplateattributes-customattributes): {{
    {{Key}}: {{Value}}}}
  [CustomerProfileAttributes](#cfn-wisdom-messagetemplate-messagetemplateattributes-customerprofileattributes): {{
    CustomerProfileAttributes}}
  [SystemAttributes](#cfn-wisdom-messagetemplate-messagetemplateattributes-systemattributes): {{
    SystemAttributes}}
```

## Properties
<a name="aws-properties-wisdom-messagetemplate-messagetemplateattributes-properties"></a>

`AgentAttributes`  <a name="cfn-wisdom-messagetemplate-messagetemplateattributes-agentattributes"></a>
The agent attributes that are used with the message template.
*Required*: No
*Type*: [AgentAttributes](aws-properties-wisdom-messagetemplate-agentattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomAttributes`  <a name="cfn-wisdom-messagetemplate-messagetemplateattributes-customattributes"></a>
The custom attributes that are used with the message template.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomerProfileAttributes`  <a name="cfn-wisdom-messagetemplate-messagetemplateattributes-customerprofileattributes"></a>
The customer profile attributes that are used with the message template.
*Required*: No
*Type*: [CustomerProfileAttributes](aws-properties-wisdom-messagetemplate-customerprofileattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SystemAttributes`  <a name="cfn-wisdom-messagetemplate-messagetemplateattributes-systemattributes"></a>
The system attributes that are used with the message template.
*Required*: No
*Type*: [SystemAttributes](aws-properties-wisdom-messagetemplate-systemattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
