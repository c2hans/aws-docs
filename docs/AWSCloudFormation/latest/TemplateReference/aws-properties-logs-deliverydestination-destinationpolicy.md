---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-deliverydestination-destinationpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::DeliveryDestination DestinationPolicy
<a name="aws-properties-logs-deliverydestination-destinationpolicy"></a>

An IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account.

## Syntax
<a name="aws-properties-logs-deliverydestination-destinationpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-deliverydestination-destinationpolicy-syntax.json"></a>

```
{
  "[DeliveryDestinationName](#cfn-logs-deliverydestination-destinationpolicy-deliverydestinationname)" : {{String}},
  "[DeliveryDestinationPolicy](#cfn-logs-deliverydestination-destinationpolicy-deliverydestinationpolicy)" : {{Json}}
}
```

### YAML
<a name="aws-properties-logs-deliverydestination-destinationpolicy-syntax.yaml"></a>

```
  [DeliveryDestinationName](#cfn-logs-deliverydestination-destinationpolicy-deliverydestinationname): {{String}}
  [DeliveryDestinationPolicy](#cfn-logs-deliverydestination-destinationpolicy-deliverydestinationpolicy): {{Json}}
```

## Properties
<a name="aws-properties-logs-deliverydestination-destinationpolicy-properties"></a>

`DeliveryDestinationName`  <a name="cfn-logs-deliverydestination-destinationpolicy-deliverydestinationname"></a>
A name for an existing destination.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeliveryDestinationPolicy`  <a name="cfn-logs-deliverydestination-destinationpolicy-deliverydestinationpolicy"></a>
Creates or updates an access policy associated with an existing destination. An access policy is an [IAM policy document](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies_overview.html) that is used to authorize claims to register a subscription filter against a given destination.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
