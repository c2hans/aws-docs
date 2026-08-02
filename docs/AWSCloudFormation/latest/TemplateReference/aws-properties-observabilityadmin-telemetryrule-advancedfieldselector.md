---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-telemetryrule-advancedfieldselector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::TelemetryRule AdvancedFieldSelector
<a name="aws-properties-observabilityadmin-telemetryrule-advancedfieldselector"></a>

 Defines criteria for selecting resources based on field values.

## Syntax
<a name="aws-properties-observabilityadmin-telemetryrule-advancedfieldselector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-telemetryrule-advancedfieldselector-syntax.json"></a>

```
{
  "[EndsWith](#cfn-observabilityadmin-telemetryrule-advancedfieldselector-endswith)" : {{[ String, ... ]}},
  "[Equals](#cfn-observabilityadmin-telemetryrule-advancedfieldselector-equals)" : {{[ String, ... ]}},
  "[Field](#cfn-observabilityadmin-telemetryrule-advancedfieldselector-field)" : {{String}},
  "[NotEndsWith](#cfn-observabilityadmin-telemetryrule-advancedfieldselector-notendswith)" : {{[ String, ... ]}},
  "[NotEquals](#cfn-observabilityadmin-telemetryrule-advancedfieldselector-notequals)" : {{[ String, ... ]}},
  "[NotStartsWith](#cfn-observabilityadmin-telemetryrule-advancedfieldselector-notstartswith)" : {{[ String, ... ]}},
  "[StartsWith](#cfn-observabilityadmin-telemetryrule-advancedfieldselector-startswith)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-telemetryrule-advancedfieldselector-syntax.yaml"></a>

```
  [EndsWith](#cfn-observabilityadmin-telemetryrule-advancedfieldselector-endswith): {{
    - String}}
  [Equals](#cfn-observabilityadmin-telemetryrule-advancedfieldselector-equals): {{
    - String}}
  [Field](#cfn-observabilityadmin-telemetryrule-advancedfieldselector-field): {{String}}
  [NotEndsWith](#cfn-observabilityadmin-telemetryrule-advancedfieldselector-notendswith): {{
    - String}}
  [NotEquals](#cfn-observabilityadmin-telemetryrule-advancedfieldselector-notequals): {{
    - String}}
  [NotStartsWith](#cfn-observabilityadmin-telemetryrule-advancedfieldselector-notstartswith): {{
    - String}}
  [StartsWith](#cfn-observabilityadmin-telemetryrule-advancedfieldselector-startswith): {{
    - String}}
```

## Properties
<a name="aws-properties-observabilityadmin-telemetryrule-advancedfieldselector-properties"></a>

`EndsWith`  <a name="cfn-observabilityadmin-telemetryrule-advancedfieldselector-endswith"></a>
 Matches if the field value ends with the specified value.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Equals`  <a name="cfn-observabilityadmin-telemetryrule-advancedfieldselector-equals"></a>
 Matches if the field value equals the specified value.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Field`  <a name="cfn-observabilityadmin-telemetryrule-advancedfieldselector-field"></a>
 The name of the field to use for selection.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotEndsWith`  <a name="cfn-observabilityadmin-telemetryrule-advancedfieldselector-notendswith"></a>
 Matches if the field value does not end with the specified value.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotEquals`  <a name="cfn-observabilityadmin-telemetryrule-advancedfieldselector-notequals"></a>
 Matches if the field value does not equal the specified value.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotStartsWith`  <a name="cfn-observabilityadmin-telemetryrule-advancedfieldselector-notstartswith"></a>
 Matches if the field value does not start with the specified value.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartsWith`  <a name="cfn-observabilityadmin-telemetryrule-advancedfieldselector-startswith"></a>
 Matches if the field value starts with the specified value.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
