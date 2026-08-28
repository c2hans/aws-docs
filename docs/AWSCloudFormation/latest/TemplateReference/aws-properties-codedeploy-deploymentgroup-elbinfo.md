---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-elbinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentGroup ELBInfo
<a name="aws-properties-codedeploy-deploymentgroup-elbinfo"></a>

The `ELBInfo` property type specifies information about the Elastic Load Balancing load balancer used for an CodeDeploy deployment group.

If you specify the `ELBInfo` property, the `DeploymentStyle.DeploymentOption` property must be set to `WITH_TRAFFIC_CONTROL` for AWS CodeDeploy to route your traffic using the specified load balancers.

`ELBInfo` is a property of the [AWS CodeDeploy DeploymentGroup LoadBalancerInfo ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html) property type.

## Syntax
<a name="aws-properties-codedeploy-deploymentgroup-elbinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentgroup-elbinfo-syntax.json"></a>

```
{
  "[Name](#cfn-codedeploy-deploymentgroup-elbinfo-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentgroup-elbinfo-syntax.yaml"></a>

```
  [Name](#cfn-codedeploy-deploymentgroup-elbinfo-name): {{String}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentgroup-elbinfo-properties"></a>

`Name`  <a name="cfn-codedeploy-deploymentgroup-elbinfo-name"></a>
For blue/green deployments, the name of the load balancer that is used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.
CloudFormation supports blue/green deployments on AWS Lambda compute platforms only.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
