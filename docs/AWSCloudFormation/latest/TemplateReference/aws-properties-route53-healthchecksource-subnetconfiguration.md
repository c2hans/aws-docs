---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-healthchecksource-subnetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::HealthCheckSource SubnetConfiguration

<a name="aws-properties-route53-healthchecksource-subnetconfiguration-description"></a>The `SubnetConfiguration` property type specifies Property description not available. for an [AWS::Route53::HealthCheckSource](aws-resource-route53-healthchecksource.md).

## Syntax
<a name="aws-properties-route53-healthchecksource-subnetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53-healthchecksource-subnetconfiguration-syntax.json"></a>

```
{
  "[AvailabilityZoneId](#cfn-route53-healthchecksource-subnetconfiguration-availabilityzoneid)" : {{String}},
  "[SecurityGroupIdList](#cfn-route53-healthchecksource-subnetconfiguration-securitygroupidlist)" : {{[ String, ... ]}},
  "[SubnetId](#cfn-route53-healthchecksource-subnetconfiguration-subnetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53-healthchecksource-subnetconfiguration-syntax.yaml"></a>

```
  [AvailabilityZoneId](#cfn-route53-healthchecksource-subnetconfiguration-availabilityzoneid): {{String}}
  [SecurityGroupIdList](#cfn-route53-healthchecksource-subnetconfiguration-securitygroupidlist): {{
    - String}}
  [SubnetId](#cfn-route53-healthchecksource-subnetconfiguration-subnetid): {{String}}
```

## Properties
<a name="aws-properties-route53-healthchecksource-subnetconfiguration-properties"></a>

`AvailabilityZoneId`  <a name="cfn-route53-healthchecksource-subnetconfiguration-availabilityzoneid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIdList`  <a name="cfn-route53-healthchecksource-subnetconfiguration-securitygroupidlist"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `64 | 10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetId`  <a name="cfn-route53-healthchecksource-subnetconfiguration-subnetid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
