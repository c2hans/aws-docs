---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-telemetryrule-labelnamecondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryRule LabelNameCondition
<a name="aws-properties-observabilityadmin-telemetryrule-labelnamecondition"></a>

 Condition that matches based on WAF rule labels, with label names limited to 1024 characters.

## Syntax
<a name="aws-properties-observabilityadmin-telemetryrule-labelnamecondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-telemetryrule-labelnamecondition-syntax.json"></a>

```
{
  "[LabelName](#cfn-observabilityadmin-telemetryrule-labelnamecondition-labelname)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-telemetryrule-labelnamecondition-syntax.yaml"></a>

```
  [LabelName](#cfn-observabilityadmin-telemetryrule-labelnamecondition-labelname): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-telemetryrule-labelnamecondition-properties"></a>

`LabelName`  <a name="cfn-observabilityadmin-telemetryrule-labelnamecondition-labelname"></a>
 The label name to match, supporting alphanumeric characters, underscores, hyphens, and colons.
*Required*: No
*Type*: String
*Pattern*: `^[0-9A-Za-z_\-:]+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
