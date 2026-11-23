---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-healthchecksource-subnetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::HealthCheckSource SubnetConfiguration

A complex type that identifies one subnet for a health check source and the security groups that Route 53 associates with the network interfaces that it creates in that subnet.

## Syntax
<a name="aws-properties-route53-healthchecksource-subnetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53-healthchecksource-subnetconfiguration-syntax.json"></a>

```json
{
  "[AvailabilityZoneId](#cfn-route53-healthchecksource-subnetconfiguration-availabilityzoneid)" : {{String}},
  "[SecurityGroupIdList](#cfn-route53-healthchecksource-subnetconfiguration-securitygroupidlist)" : {{[ String, ... ]}},
  "[SubnetId](#cfn-route53-healthchecksource-subnetconfiguration-subnetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53-healthchecksource-subnetconfiguration-syntax.yaml"></a>

```yaml
  [AvailabilityZoneId](#cfn-route53-healthchecksource-subnetconfiguration-availabilityzoneid): {{String}}
  [SecurityGroupIdList](#cfn-route53-healthchecksource-subnetconfiguration-securitygroupidlist): {{
    - String}}
  [SubnetId](#cfn-route53-healthchecksource-subnetconfiguration-subnetid): {{String}}
```

## Properties
<a name="aws-properties-route53-healthchecksource-subnetconfiguration-properties"></a>

`AvailabilityZoneId`  <a name="cfn-route53-healthchecksource-subnetconfiguration-availabilityzoneid"></a>
The ID of the Availability Zone that contains the subnet, for example `use1-az1`. Specify the Availability Zone ID, not the Availability Zone name.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIdList`  <a name="cfn-route53-healthchecksource-subnetconfiguration-securitygroupidlist"></a>
The IDs of the security groups in the same virtual private cloud (VPC) to associate with the network interfaces that Route 53 creates in this subnet. The security groups must allow outbound traffic to the endpoints that the health checks monitor.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `64 | 10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetId`  <a name="cfn-route53-healthchecksource-subnetconfiguration-subnetid"></a>
The ID of the subnet that Route 53 uses to send health check requests.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-route53-healthchecksource-subnetconfiguration--seealso"></a>
+ [SubnetConfiguration](https://docs.aws.amazon.com/Route53/latest/APIReference/API_SubnetConfiguration.html) in the *Amazon Route 53 API Reference*
