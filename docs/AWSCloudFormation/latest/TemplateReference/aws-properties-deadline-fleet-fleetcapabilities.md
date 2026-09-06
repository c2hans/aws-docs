---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-fleetcapabilities.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet FleetCapabilities
<a name="aws-properties-deadline-fleet-fleetcapabilities"></a>

The amounts and attributes of fleets.

## Syntax
<a name="aws-properties-deadline-fleet-fleetcapabilities-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-fleetcapabilities-syntax.json"></a>

```
{
  "[Amounts](#cfn-deadline-fleet-fleetcapabilities-amounts)" : {{[ FleetAmountCapability, ... ]}},
  "[Attributes](#cfn-deadline-fleet-fleetcapabilities-attributes)" : {{[ FleetAttributeCapability, ... ]}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-fleetcapabilities-syntax.yaml"></a>

```
  [Amounts](#cfn-deadline-fleet-fleetcapabilities-amounts): {{
    - FleetAmountCapability}}
  [Attributes](#cfn-deadline-fleet-fleetcapabilities-attributes): {{
    - FleetAttributeCapability}}
```

## Properties
<a name="aws-properties-deadline-fleet-fleetcapabilities-properties"></a>

`Amounts`  <a name="cfn-deadline-fleet-fleetcapabilities-amounts"></a>
Amount capabilities of the fleet.
*Required*: No
*Type*: Array of [FleetAmountCapability](aws-properties-deadline-fleet-fleetamountcapability.md)
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Attributes`  <a name="cfn-deadline-fleet-fleetcapabilities-attributes"></a>
Attribute capabilities of the fleet.
*Required*: No
*Type*: Array of [FleetAttributeCapability](aws-properties-deadline-fleet-fleetattributecapability.md)
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
