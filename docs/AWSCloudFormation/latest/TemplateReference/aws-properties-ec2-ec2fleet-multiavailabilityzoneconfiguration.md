---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-multiavailabilityzoneconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet MultiAvailabilityZoneConfiguration
<a name="aws-properties-ec2-ec2fleet-multiavailabilityzoneconfiguration"></a>

<a name="aws-properties-ec2-ec2fleet-multiavailabilityzoneconfiguration-description"></a>The `MultiAvailabilityZoneConfiguration` property type specifies Property description not available. for an [AWS::EC2::EC2Fleet](aws-resource-ec2-ec2fleet.md).

## Syntax
<a name="aws-properties-ec2-ec2fleet-multiavailabilityzoneconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-multiavailabilityzoneconfiguration-syntax.json"></a>

```
{
  "[ConfigurationType](#cfn-ec2-ec2fleet-multiavailabilityzoneconfiguration-configurationtype)" : {{String}},
  "[StandbyAvailabilityZones](#cfn-ec2-ec2fleet-multiavailabilityzoneconfiguration-standbyavailabilityzones)" : {{[ StandbyAvailabilityZone, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-multiavailabilityzoneconfiguration-syntax.yaml"></a>

```
  [ConfigurationType](#cfn-ec2-ec2fleet-multiavailabilityzoneconfiguration-configurationtype): {{String}}
  [StandbyAvailabilityZones](#cfn-ec2-ec2fleet-multiavailabilityzoneconfiguration-standbyavailabilityzones): {{
    - StandbyAvailabilityZone}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-multiavailabilityzoneconfiguration-properties"></a>

`ConfigurationType`  <a name="cfn-ec2-ec2fleet-multiavailabilityzoneconfiguration-configurationtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StandbyAvailabilityZones`  <a name="cfn-ec2-ec2fleet-multiavailabilityzoneconfiguration-standbyavailabilityzones"></a>
Property description not available.
*Required*: No
*Type*: Array of [StandbyAvailabilityZone](aws-properties-ec2-ec2fleet-standbyavailabilityzone.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
