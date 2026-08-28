---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-capacityprovider-capacityreservationspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CapacityProvider CapacityReservationSpecification
<a name="aws-properties-bedrockagentcore-capacityprovider-capacityreservationspecification"></a>

<a name="aws-properties-bedrockagentcore-capacityprovider-capacityreservationspecification-description"></a>The `CapacityReservationSpecification` property type specifies Property description not available. for an [AWS::BedrockAgentCore::CapacityProvider](aws-resource-bedrockagentcore-capacityprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-capacityprovider-capacityreservationspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-capacityprovider-capacityreservationspecification-syntax.json"></a>

```
{
  "[CapacityReservationPreference](#cfn-bedrockagentcore-capacityprovider-capacityreservationspecification-capacityreservationpreference)" : {{String}},
  "[CapacityReservationTarget](#cfn-bedrockagentcore-capacityprovider-capacityreservationspecification-capacityreservationtarget)" : {{CapacityReservationTarget}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-capacityprovider-capacityreservationspecification-syntax.yaml"></a>

```
  [CapacityReservationPreference](#cfn-bedrockagentcore-capacityprovider-capacityreservationspecification-capacityreservationpreference): {{String}}
  [CapacityReservationTarget](#cfn-bedrockagentcore-capacityprovider-capacityreservationspecification-capacityreservationtarget): {{
    CapacityReservationTarget}}
```

## Properties
<a name="aws-properties-bedrockagentcore-capacityprovider-capacityreservationspecification-properties"></a>

`CapacityReservationPreference`  <a name="cfn-bedrockagentcore-capacityprovider-capacityreservationspecification-capacityreservationpreference"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `capacity-reservations-only | open | none`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CapacityReservationTarget`  <a name="cfn-bedrockagentcore-capacityprovider-capacityreservationspecification-capacityreservationtarget"></a>
Property description not available.
*Required*: No
*Type*: [CapacityReservationTarget](aws-properties-bedrockagentcore-capacityprovider-capacityreservationtarget.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
