---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-consentportal-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::ConsentPortal Tag
<a name="aws-properties-bedrockagentcore-consentportal-tag"></a>

<a name="aws-properties-bedrockagentcore-consentportal-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::BedrockAgentCore::ConsentPortal](aws-resource-bedrockagentcore-consentportal.md).

## Syntax
<a name="aws-properties-bedrockagentcore-consentportal-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-consentportal-tag-syntax.json"></a>

```
{
  "[Key](#cfn-bedrockagentcore-consentportal-tag-key)" : {{String}},
  "[Value](#cfn-bedrockagentcore-consentportal-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-consentportal-tag-syntax.yaml"></a>

```
  [Key](#cfn-bedrockagentcore-consentportal-tag-key): {{String}}
  [Value](#cfn-bedrockagentcore-consentportal-tag-value): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-consentportal-tag-properties"></a>

`Key`  <a name="cfn-bedrockagentcore-consentportal-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-bedrockagentcore-consentportal-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
