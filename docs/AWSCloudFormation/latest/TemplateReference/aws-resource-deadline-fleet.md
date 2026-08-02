---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-deadline-fleet.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet
<a name="aws-resource-deadline-fleet"></a>

Creates a fleet. Fleets gather information relating to compute, or capacity, for renders within your farms. You can choose to manage your own capacity or opt to have fleets fully managed by Deadline Cloud.

## Syntax
<a name="aws-resource-deadline-fleet-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-deadline-fleet-syntax.json"></a>

```
{
  "Type" : "AWS::Deadline::Fleet",
  "Properties" : {
      "[Configuration](#cfn-deadline-fleet-configuration)" : {{FleetConfiguration}},
      "[Description](#cfn-deadline-fleet-description)" : {{String}},
      "[DisplayName](#cfn-deadline-fleet-displayname)" : {{String}},
      "[FarmId](#cfn-deadline-fleet-farmid)" : {{String}},
      "[HostConfiguration](#cfn-deadline-fleet-hostconfiguration)" : {{HostConfiguration}},
      "[MaxWorkerCount](#cfn-deadline-fleet-maxworkercount)" : {{Integer}},
      "[MinWorkerCount](#cfn-deadline-fleet-minworkercount)" : {{Integer}},
      "[RoleArn](#cfn-deadline-fleet-rolearn)" : {{String}},
      "[Tags](#cfn-deadline-fleet-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-deadline-fleet-syntax.yaml"></a>

```
Type: AWS::Deadline::Fleet
Properties:
  [Configuration](#cfn-deadline-fleet-configuration): {{
    FleetConfiguration}}
  [Description](#cfn-deadline-fleet-description): {{String}}
  [DisplayName](#cfn-deadline-fleet-displayname): {{String}}
  [FarmId](#cfn-deadline-fleet-farmid): {{String}}
  [HostConfiguration](#cfn-deadline-fleet-hostconfiguration): {{
    HostConfiguration}}
  [MaxWorkerCount](#cfn-deadline-fleet-maxworkercount): {{Integer}}
  [MinWorkerCount](#cfn-deadline-fleet-minworkercount): {{Integer}}
  [RoleArn](#cfn-deadline-fleet-rolearn): {{String}}
  [Tags](#cfn-deadline-fleet-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-deadline-fleet-properties"></a>

`Configuration`  <a name="cfn-deadline-fleet-configuration"></a>
The configuration details for the fleet.
*Required*: Yes
*Type*: [FleetConfiguration](aws-properties-deadline-fleet-fleetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-deadline-fleet-description"></a>
A description that helps identify what the fleet is used for.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-deadline-fleet-displayname"></a>
The display name of the fleet summary to update.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FarmId`  <a name="cfn-deadline-fleet-farmid"></a>
The farm ID.
*Required*: Yes
*Type*: String
*Pattern*: `^farm-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HostConfiguration`  <a name="cfn-deadline-fleet-hostconfiguration"></a>
Provides a script that runs as a worker is starting up that you can use to provide additional configuration for workers in your fleet.
To remove a script from a fleet, use the [UpdateFleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateFleet.html) operation with the `hostConfiguration``scriptBody` parameter set to an empty string ("").
*Required*: No
*Type*: [HostConfiguration](aws-properties-deadline-fleet-hostconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxWorkerCount`  <a name="cfn-deadline-fleet-maxworkercount"></a>
The maximum number of workers specified in the fleet.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinWorkerCount`  <a name="cfn-deadline-fleet-minworkercount"></a>
The minimum number of workers in the fleet.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-deadline-fleet-rolearn"></a>
The IAM role that workers in the fleet use when processing jobs.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):iam::\d{12}:role(/[!-.0-~]+)*/[\w+=,.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-deadline-fleet-tags"></a>
The tags to add to your fleet. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.
*Required*: No
*Type*: Array of [Tag](aws-properties-deadline-fleet-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-deadline-fleet-return-values"></a>

### Ref
<a name="aws-resource-deadline-fleet-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the fleet.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-deadline-fleet-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-deadline-fleet-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) assigned to the fleet.

`FleetId`  <a name="FleetId-fn::getatt"></a>
The fleet ID.

`Status`  <a name="Status-fn::getatt"></a>
The status of the fleet.

`StatusMessage`  <a name="StatusMessage-fn::getatt"></a>
A message that communicates a suspended status of the fleet.

`WorkerCount`  <a name="WorkerCount-fn::getatt"></a>
The number of workers in the fleet summary.
