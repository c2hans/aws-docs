---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-healthchecksource-healthchecksourceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::HealthCheckSource HealthCheckSourceConfig

<a name="aws-properties-route53-healthchecksource-healthchecksourceconfig-description"></a>The `HealthCheckSourceConfig` property type specifies Property description not available. for an [AWS::Route53::HealthCheckSource](aws-resource-route53-healthchecksource.md).

## Syntax
<a name="aws-properties-route53-healthchecksource-healthchecksourceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53-healthchecksource-healthchecksourceconfig-syntax.json"></a>

```
{
  "[SubnetConfigurationList](#cfn-route53-healthchecksource-healthchecksourceconfig-subnetconfigurationlist)" : {{[ SubnetConfiguration, ... ]}},
  "[VpcId](#cfn-route53-healthchecksource-healthchecksourceconfig-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53-healthchecksource-healthchecksourceconfig-syntax.yaml"></a>

```
  [SubnetConfigurationList](#cfn-route53-healthchecksource-healthchecksourceconfig-subnetconfigurationlist): {{
    - SubnetConfiguration}}
  [VpcId](#cfn-route53-healthchecksource-healthchecksourceconfig-vpcid): {{String}}
```

## Properties
<a name="aws-properties-route53-healthchecksource-healthchecksourceconfig-properties"></a>

`SubnetConfigurationList`  <a name="cfn-route53-healthchecksource-healthchecksourceconfig-subnetconfigurationlist"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [SubnetConfiguration](aws-properties-route53-healthchecksource-subnetconfiguration.md)
*Minimum*: `2`
*Maximum*: `3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-route53-healthchecksource-healthchecksourceconfig-vpcid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
