---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentconfig-timebasedlinear.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentConfig TimeBasedLinear
<a name="aws-properties-codedeploy-deploymentconfig-timebasedlinear"></a>

A configuration that shifts traffic from one version of a Lambda function or ECS task set to another in equal increments, with an equal number of minutes between each increment. The original and target Lambda function versions or ECS task sets are specified in the deployment's AppSpec file.

## Syntax
<a name="aws-properties-codedeploy-deploymentconfig-timebasedlinear-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentconfig-timebasedlinear-syntax.json"></a>

```
{
  "[LinearInterval](#cfn-codedeploy-deploymentconfig-timebasedlinear-linearinterval)" : {{Integer}},
  "[LinearPercentage](#cfn-codedeploy-deploymentconfig-timebasedlinear-linearpercentage)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentconfig-timebasedlinear-syntax.yaml"></a>

```
  [LinearInterval](#cfn-codedeploy-deploymentconfig-timebasedlinear-linearinterval): {{Integer}}
  [LinearPercentage](#cfn-codedeploy-deploymentconfig-timebasedlinear-linearpercentage): {{Integer}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentconfig-timebasedlinear-properties"></a>

`LinearInterval`  <a name="cfn-codedeploy-deploymentconfig-timebasedlinear-linearinterval"></a>
The number of minutes between each incremental traffic shift of a `TimeBasedLinear` deployment.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LinearPercentage`  <a name="cfn-codedeploy-deploymentconfig-timebasedlinear-linearpercentage"></a>
The percentage of traffic that is shifted at the start of each increment of a `TimeBasedLinear` deployment.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
