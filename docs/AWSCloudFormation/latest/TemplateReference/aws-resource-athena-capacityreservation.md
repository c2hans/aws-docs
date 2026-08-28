---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-athena-capacityreservation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::CapacityReservation
<a name="aws-resource-athena-capacityreservation"></a>

Specifies a capacity reservation with the provided name and number of requested data processing units.

## Syntax
<a name="aws-resource-athena-capacityreservation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-athena-capacityreservation-syntax.json"></a>

```
{
  "Type" : "AWS::Athena::CapacityReservation",
  "Properties" : {
      "[CapacityAssignmentConfiguration](#cfn-athena-capacityreservation-capacityassignmentconfiguration)" : {{CapacityAssignmentConfiguration}},
      "[Name](#cfn-athena-capacityreservation-name)" : {{String}},
      "[Tags](#cfn-athena-capacityreservation-tags)" : {{[ Tag, ... ]}},
      "[TargetDpus](#cfn-athena-capacityreservation-targetdpus)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-athena-capacityreservation-syntax.yaml"></a>

```
Type: AWS::Athena::CapacityReservation
Properties:
  [CapacityAssignmentConfiguration](#cfn-athena-capacityreservation-capacityassignmentconfiguration): {{
    CapacityAssignmentConfiguration}}
  [Name](#cfn-athena-capacityreservation-name): {{String}}
  [Tags](#cfn-athena-capacityreservation-tags): {{
    - Tag}}
  [TargetDpus](#cfn-athena-capacityreservation-targetdpus): {{Integer}}
```

## Properties
<a name="aws-resource-athena-capacityreservation-properties"></a>

`CapacityAssignmentConfiguration`  <a name="cfn-athena-capacityreservation-capacityassignmentconfiguration"></a>
Assigns Athena workgroups (and hence their queries) to capacity reservations. A capacity reservation can have only one capacity assignment configuration, but the capacity assignment configuration can be made up of multiple individual assignments. Each assignment specifies how Athena queries can consume capacity from the capacity reservation that their workgroup is mapped to.
*Required*: No
*Type*: [CapacityAssignmentConfiguration](aws-properties-athena-capacityreservation-capacityassignmentconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-athena-capacityreservation-name"></a>
The name of the capacity reservation.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9._-]{1,128}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-athena-capacityreservation-tags"></a>
An array of key-value pairs to apply to the capacity reservation.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-athena-capacityreservation-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetDpus`  <a name="cfn-athena-capacityreservation-targetdpus"></a>
The number of data processing units requested.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-athena-capacityreservation-return-values"></a>

### Ref
<a name="aws-resource-athena-capacityreservation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the capacity reservation.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-athena-capacityreservation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-athena-capacityreservation-return-values-fn--getatt-fn--getatt"></a>

`AllocatedDpus`  <a name="AllocatedDpus-fn::getatt"></a>
The number of data processing units currently allocated.

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the capacity reservation.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time in UTC epoch millis when the capacity reservation was created.

`LastSuccessfulAllocationTime`  <a name="LastSuccessfulAllocationTime-fn::getatt"></a>
The time of the most recent capacity allocation that succeeded.

`Status`  <a name="Status-fn::getatt"></a>
The status of the capacity reservation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
