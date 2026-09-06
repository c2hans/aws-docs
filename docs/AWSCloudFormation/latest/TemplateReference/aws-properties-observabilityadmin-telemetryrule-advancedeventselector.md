---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-telemetryrule-advancedeventselector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryRule AdvancedEventSelector
<a name="aws-properties-observabilityadmin-telemetryrule-advancedeventselector"></a>

Advanced event selectors let you create fine-grained selectors for management, data, and network activity events.

## Syntax
<a name="aws-properties-observabilityadmin-telemetryrule-advancedeventselector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-telemetryrule-advancedeventselector-syntax.json"></a>

```
{
  "[FieldSelectors](#cfn-observabilityadmin-telemetryrule-advancedeventselector-fieldselectors)" : {{[ AdvancedFieldSelector, ... ]}},
  "[Name](#cfn-observabilityadmin-telemetryrule-advancedeventselector-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-telemetryrule-advancedeventselector-syntax.yaml"></a>

```
  [FieldSelectors](#cfn-observabilityadmin-telemetryrule-advancedeventselector-fieldselectors): {{
    - AdvancedFieldSelector}}
  [Name](#cfn-observabilityadmin-telemetryrule-advancedeventselector-name): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-telemetryrule-advancedeventselector-properties"></a>

`FieldSelectors`  <a name="cfn-observabilityadmin-telemetryrule-advancedeventselector-fieldselectors"></a>
Contains all selector statements in an advanced event selector.
*Required*: Yes
*Type*: Array of [AdvancedFieldSelector](aws-properties-observabilityadmin-telemetryrule-advancedfieldselector.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-observabilityadmin-telemetryrule-advancedeventselector-name"></a>
An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
