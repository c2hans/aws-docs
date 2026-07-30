---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-greenfleetprovisioningoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentGroup GreenFleetProvisioningOption
<a name="aws-properties-codedeploy-deploymentgroup-greenfleetprovisioningoption"></a>

Information about the instances that belong to the replacement environment in a blue/green deployment.

## Syntax
<a name="aws-properties-codedeploy-deploymentgroup-greenfleetprovisioningoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentgroup-greenfleetprovisioningoption-syntax.json"></a>

```
{
  "[Action](#cfn-codedeploy-deploymentgroup-greenfleetprovisioningoption-action)" : {{String}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentgroup-greenfleetprovisioningoption-syntax.yaml"></a>

```
  [Action](#cfn-codedeploy-deploymentgroup-greenfleetprovisioningoption-action): {{String}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentgroup-greenfleetprovisioningoption-properties"></a>

`Action`  <a name="cfn-codedeploy-deploymentgroup-greenfleetprovisioningoption-action"></a>
The method used to add instances to a replacement environment.
+ `DISCOVER_EXISTING`: Use instances that already exist or will be created manually.
+ `COPY_AUTO_SCALING_GROUP`: Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group.
*Required*: No
*Type*: String
*Allowed values*: `DISCOVER_EXISTING | COPY_AUTO_SCALING_GROUP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
