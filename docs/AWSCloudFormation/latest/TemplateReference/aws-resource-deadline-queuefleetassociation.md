---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-deadline-queuefleetassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::QueueFleetAssociation
<a name="aws-resource-deadline-queuefleetassociation"></a>

Creates an association between a queue and a fleet.

## Syntax
<a name="aws-resource-deadline-queuefleetassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-deadline-queuefleetassociation-syntax.json"></a>

```
{
  "Type" : "AWS::Deadline::QueueFleetAssociation",
  "Properties" : {
      "[FarmId](#cfn-deadline-queuefleetassociation-farmid)" : {{String}},
      "[FleetId](#cfn-deadline-queuefleetassociation-fleetid)" : {{String}},
      "[QueueId](#cfn-deadline-queuefleetassociation-queueid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-deadline-queuefleetassociation-syntax.yaml"></a>

```
Type: AWS::Deadline::QueueFleetAssociation
Properties:
  [FarmId](#cfn-deadline-queuefleetassociation-farmid): {{String}}
  [FleetId](#cfn-deadline-queuefleetassociation-fleetid): {{String}}
  [QueueId](#cfn-deadline-queuefleetassociation-queueid): {{String}}
```

## Properties
<a name="aws-resource-deadline-queuefleetassociation-properties"></a>

`FarmId`  <a name="cfn-deadline-queuefleetassociation-farmid"></a>
The identifier of the farm that contains the queue and the fleet.
*Required*: Yes
*Type*: String
*Pattern*: `^farm-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FleetId`  <a name="cfn-deadline-queuefleetassociation-fleetid"></a>
The fleet ID.
*Required*: Yes
*Type*: String
*Pattern*: `^fleet-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QueueId`  <a name="cfn-deadline-queuefleetassociation-queueid"></a>
The queue ID.
*Required*: Yes
*Type*: String
*Pattern*: `^queue-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-deadline-queuefleetassociation-return-values"></a>

### Ref
<a name="aws-resource-deadline-queuefleetassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the queue fleet associations.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).
