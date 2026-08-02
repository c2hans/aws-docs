---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connection-physicalconnectionrequirements.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Connection PhysicalConnectionRequirements
<a name="aws-properties-glue-connection-physicalconnectionrequirements"></a>

The OAuth client app in GetConnection response.

## Syntax
<a name="aws-properties-glue-connection-physicalconnectionrequirements-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connection-physicalconnectionrequirements-syntax.json"></a>

```
{
  "[AvailabilityZone](#cfn-glue-connection-physicalconnectionrequirements-availabilityzone)" : {{String}},
  "[SecurityGroupIdList](#cfn-glue-connection-physicalconnectionrequirements-securitygroupidlist)" : {{[ String, ... ]}},
  "[SubnetId](#cfn-glue-connection-physicalconnectionrequirements-subnetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-connection-physicalconnectionrequirements-syntax.yaml"></a>

```
  [AvailabilityZone](#cfn-glue-connection-physicalconnectionrequirements-availabilityzone): {{String}}
  [SecurityGroupIdList](#cfn-glue-connection-physicalconnectionrequirements-securitygroupidlist): {{
    - String}}
  [SubnetId](#cfn-glue-connection-physicalconnectionrequirements-subnetid): {{String}}
```

## Properties
<a name="aws-properties-glue-connection-physicalconnectionrequirements-properties"></a>

`AvailabilityZone`  <a name="cfn-glue-connection-physicalconnectionrequirements-availabilityzone"></a>
The connection's Availability Zone.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIdList`  <a name="cfn-glue-connection-physicalconnectionrequirements-securitygroupidlist"></a>
The security group ID list used by the connection.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-glue-connection-physicalconnectionrequirements-subnetid"></a>
The subnet ID used by the connection.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
