---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-capacityprovider-capacityreservationtarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CapacityProvider CapacityReservationTarget
<a name="aws-properties-bedrockagentcore-capacityprovider-capacityreservationtarget"></a>

<a name="aws-properties-bedrockagentcore-capacityprovider-capacityreservationtarget-description"></a>The `CapacityReservationTarget` property type specifies Property description not available. for an [AWS::BedrockAgentCore::CapacityProvider](aws-resource-bedrockagentcore-capacityprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-capacityprovider-capacityreservationtarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-capacityprovider-capacityreservationtarget-syntax.json"></a>

```
{
  "[CapacityReservationId](#cfn-bedrockagentcore-capacityprovider-capacityreservationtarget-capacityreservationid)" : {{String}},
  "[CapacityReservationResourceGroupArn](#cfn-bedrockagentcore-capacityprovider-capacityreservationtarget-capacityreservationresourcegrouparn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-capacityprovider-capacityreservationtarget-syntax.yaml"></a>

```
  [CapacityReservationId](#cfn-bedrockagentcore-capacityprovider-capacityreservationtarget-capacityreservationid): {{String}}
  [CapacityReservationResourceGroupArn](#cfn-bedrockagentcore-capacityprovider-capacityreservationtarget-capacityreservationresourcegrouparn): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-capacityprovider-capacityreservationtarget-properties"></a>

`CapacityReservationId`  <a name="cfn-bedrockagentcore-capacityprovider-capacityreservationtarget-capacityreservationid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^cr-[0-9a-z]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CapacityReservationResourceGroupArn`  <a name="cfn-bedrockagentcore-capacityprovider-capacityreservationtarget-capacityreservationresourcegrouparn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:resource-groups:[a-z0-9-]+:[0-9]{12}:group/[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
