---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentconfig-minimumhealthyhostsperzone.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentConfig MinimumHealthyHostsPerZone
<a name="aws-properties-codedeploy-deploymentconfig-minimumhealthyhostsperzone"></a>

Information about the minimum number of healthy instances per Availability Zone.

## Syntax
<a name="aws-properties-codedeploy-deploymentconfig-minimumhealthyhostsperzone-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentconfig-minimumhealthyhostsperzone-syntax.json"></a>

```
{
  "[Type](#cfn-codedeploy-deploymentconfig-minimumhealthyhostsperzone-type)" : {{String}},
  "[Value](#cfn-codedeploy-deploymentconfig-minimumhealthyhostsperzone-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentconfig-minimumhealthyhostsperzone-syntax.yaml"></a>

```
  [Type](#cfn-codedeploy-deploymentconfig-minimumhealthyhostsperzone-type): {{String}}
  [Value](#cfn-codedeploy-deploymentconfig-minimumhealthyhostsperzone-value): {{Integer}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentconfig-minimumhealthyhostsperzone-properties"></a>

`Type`  <a name="cfn-codedeploy-deploymentconfig-minimumhealthyhostsperzone-type"></a>
The `type` associated with the `MinimumHealthyHostsPerZone` option.
*Required*: Yes
*Type*: String
*Allowed values*: `HOST_COUNT | FLEET_PERCENT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-codedeploy-deploymentconfig-minimumhealthyhostsperzone-value"></a>
The `value` associated with the `MinimumHealthyHostsPerZone` option.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
