---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentConfig MinimumHealthyHosts
<a name="aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts"></a>

`MinimumHealthyHosts` is a property of the [DeploymentConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html) resource that defines how many instances must remain healthy during an AWS CodeDeploy deployment.

## Syntax
<a name="aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts-syntax.json"></a>

```
{
  "[Type](#cfn-codedeploy-deploymentconfig-minimumhealthyhosts-type)" : {{String}},
  "[Value](#cfn-codedeploy-deploymentconfig-minimumhealthyhosts-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts-syntax.yaml"></a>

```
  [Type](#cfn-codedeploy-deploymentconfig-minimumhealthyhosts-type): {{String}}
  [Value](#cfn-codedeploy-deploymentconfig-minimumhealthyhosts-value): {{Integer}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts-properties"></a>

`Type`  <a name="cfn-codedeploy-deploymentconfig-minimumhealthyhosts-type"></a>
The minimum healthy instance type:
+ HOST\_COUNT: The minimum number of healthy instance as an absolute value.
+ FLEET\_PERCENT: The minimum number of healthy instance as a percentage of the total number of instance in the deployment.
In an example of nine instance, if a HOST\_COUNT of six is specified, deploy to up to three instances at a time. The deployment is successful if six or more instances are deployed to successfully. Otherwise, the deployment fails. If a FLEET\_PERCENT of 40 is specified, deploy to up to five instance at a time. The deployment is successful if four or more instance are deployed to successfully. Otherwise, the deployment fails.
In a call to `GetDeploymentConfig`, CodeDeployDefault.OneAtATime returns a minimum healthy instance type of MOST\_CONCURRENCY and a value of 1. This means a deployment to only one instance at a time. (You cannot set the type to MOST\_CONCURRENCY, only to HOST\_COUNT or FLEET\_PERCENT.) In addition, with CodeDeployDefault.OneAtATime, AWS CodeDeploy attempts to ensure that all instances but one are kept in a healthy state during the deployment. Although this allows one instance at a time to be taken offline for a new deployment, it also means that if the deployment to the last instance fails, the overall deployment is still successful.
For more information, see [AWS CodeDeploy Instance Health](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html) in the *AWS CodeDeploy User Guide*.
*Required*: Yes
*Type*: String
*Allowed values*: `HOST_COUNT | FLEET_PERCENT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-codedeploy-deploymentconfig-minimumhealthyhosts-value"></a>
The minimum healthy instance value.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
