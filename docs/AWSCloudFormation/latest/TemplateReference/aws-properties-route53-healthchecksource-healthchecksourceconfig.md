---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-healthchecksource-healthchecksourceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::HealthCheckSource HealthCheckSourceConfig

A complex type that contains the virtual private cloud (VPC), subnets, and security groups for a health check source. You can't change these values after you create the source.

## Syntax
<a name="aws-properties-route53-healthchecksource-healthchecksourceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53-healthchecksource-healthchecksourceconfig-syntax.json"></a>

```json
{
  "[SubnetConfigurationList](#cfn-route53-healthchecksource-healthchecksourceconfig-subnetconfigurationlist)" : {{[ SubnetConfiguration, ... ]}},
  "[VpcId](#cfn-route53-healthchecksource-healthchecksourceconfig-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53-healthchecksource-healthchecksourceconfig-syntax.yaml"></a>

```yaml
  [SubnetConfigurationList](#cfn-route53-healthchecksource-healthchecksourceconfig-subnetconfigurationlist): {{
    - SubnetConfiguration}}
  [VpcId](#cfn-route53-healthchecksource-healthchecksourceconfig-vpcid): {{String}}
```

## Properties
<a name="aws-properties-route53-healthchecksource-healthchecksourceconfig-properties"></a>

`SubnetConfigurationList`  <a name="cfn-route53-healthchecksource-healthchecksourceconfig-subnetconfigurationlist"></a>
A complex type that contains two or three `SubnetConfiguration` elements, one in each Availability Zone that Route 53 uses for private endpoint health checks in the AWS Region. The Availability Zones must be distinct. Route 53 creates network interfaces in each subnet and sends health check requests from all of them.
*Required*: Yes
*Type*: Array of [SubnetConfiguration](aws-properties-route53-healthchecksource-subnetconfiguration.md)
*Minimum*: `2`
*Maximum*: `3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-route53-healthchecksource-healthchecksourceconfig-vpcid"></a>
The ID of the virtual private cloud (VPC) that contains the subnets for the health check source. All subnets in `SubnetConfigurationList` must belong to this VPC.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-route53-healthchecksource-healthchecksourceconfig--seealso"></a>
+ [HealthCheckSourceConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckSourceConfig.html) in the *Amazon Route 53 API Reference*
