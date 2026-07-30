---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-physicalconnectionrequirements.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection PhysicalConnectionRequirements
<a name="aws-properties-datazone-connection-physicalconnectionrequirements"></a>

Physical connection requirements of a connection.

## Syntax
<a name="aws-properties-datazone-connection-physicalconnectionrequirements-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-physicalconnectionrequirements-syntax.json"></a>

```
{
  "[AvailabilityZone](#cfn-datazone-connection-physicalconnectionrequirements-availabilityzone)" : {{String}},
  "[SecurityGroupIdList](#cfn-datazone-connection-physicalconnectionrequirements-securitygroupidlist)" : {{[ String, ... ]}},
  "[SubnetId](#cfn-datazone-connection-physicalconnectionrequirements-subnetid)" : {{String}},
  "[SubnetIdList](#cfn-datazone-connection-physicalconnectionrequirements-subnetidlist)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-datazone-connection-physicalconnectionrequirements-syntax.yaml"></a>

```
  [AvailabilityZone](#cfn-datazone-connection-physicalconnectionrequirements-availabilityzone): {{String}}
  [SecurityGroupIdList](#cfn-datazone-connection-physicalconnectionrequirements-securitygroupidlist): {{
    - String}}
  [SubnetId](#cfn-datazone-connection-physicalconnectionrequirements-subnetid): {{String}}
  [SubnetIdList](#cfn-datazone-connection-physicalconnectionrequirements-subnetidlist): {{
    - String}}
```

## Properties
<a name="aws-properties-datazone-connection-physicalconnectionrequirements-properties"></a>

`AvailabilityZone`  <a name="cfn-datazone-connection-physicalconnectionrequirements-availabilityzone"></a>
The availability zone of the physical connection requirements of a connection.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIdList`  <a name="cfn-datazone-connection-physicalconnectionrequirements-securitygroupidlist"></a>
The group ID list of the physical connection requirements of a connection.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `255 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-datazone-connection-physicalconnectionrequirements-subnetid"></a>
The subnet ID of the physical connection requirements of a connection.
*Required*: No
*Type*: String
*Pattern*: `^subnet-[a-z0-9]+$`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIdList`  <a name="cfn-datazone-connection-physicalconnectionrequirements-subnetidlist"></a>
The subnet ID list of the physical connection requirements of a connection.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `32 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
