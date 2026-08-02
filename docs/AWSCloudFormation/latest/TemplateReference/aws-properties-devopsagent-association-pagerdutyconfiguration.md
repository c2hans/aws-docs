---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-pagerdutyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association PagerDutyConfiguration
<a name="aws-properties-devopsagent-association-pagerdutyconfiguration"></a>

<a name="aws-properties-devopsagent-association-pagerdutyconfiguration-description"></a>The `PagerDutyConfiguration` property type specifies Property description not available. for an [AWS::DevOpsAgent::Association](aws-resource-devopsagent-association.md).

## Syntax
<a name="aws-properties-devopsagent-association-pagerdutyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-pagerdutyconfiguration-syntax.json"></a>

```
{
  "[CustomerEmail](#cfn-devopsagent-association-pagerdutyconfiguration-customeremail)" : {{String}},
  "[EnableWebhookUpdates](#cfn-devopsagent-association-pagerdutyconfiguration-enablewebhookupdates)" : {{Boolean}},
  "[Services](#cfn-devopsagent-association-pagerdutyconfiguration-services)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-pagerdutyconfiguration-syntax.yaml"></a>

```
  [CustomerEmail](#cfn-devopsagent-association-pagerdutyconfiguration-customeremail): {{String}}
  [EnableWebhookUpdates](#cfn-devopsagent-association-pagerdutyconfiguration-enablewebhookupdates): {{Boolean}}
  [Services](#cfn-devopsagent-association-pagerdutyconfiguration-services): {{
    - String}}
```

## Properties
<a name="aws-properties-devopsagent-association-pagerdutyconfiguration-properties"></a>

`CustomerEmail`  <a name="cfn-devopsagent-association-pagerdutyconfiguration-customeremail"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableWebhookUpdates`  <a name="cfn-devopsagent-association-pagerdutyconfiguration-enablewebhookupdates"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Services`  <a name="cfn-devopsagent-association-pagerdutyconfiguration-services"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
