---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentGroup DeploymentStyle
<a name="aws-properties-codedeploy-deploymentgroup-deploymentstyle"></a>

Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.

## Syntax
<a name="aws-properties-codedeploy-deploymentgroup-deploymentstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentgroup-deploymentstyle-syntax.json"></a>

```
{
  "[DeploymentOption](#cfn-codedeploy-deploymentgroup-deploymentstyle-deploymentoption)" : {{String}},
  "[DeploymentType](#cfn-codedeploy-deploymentgroup-deploymentstyle-deploymenttype)" : {{String}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentgroup-deploymentstyle-syntax.yaml"></a>

```
  [DeploymentOption](#cfn-codedeploy-deploymentgroup-deploymentstyle-deploymentoption): {{String}}
  [DeploymentType](#cfn-codedeploy-deploymentgroup-deploymentstyle-deploymenttype): {{String}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentgroup-deploymentstyle-properties"></a>

`DeploymentOption`  <a name="cfn-codedeploy-deploymentgroup-deploymentstyle-deploymentoption"></a>
Indicates whether to route deployment traffic behind a load balancer.
 An Amazon EC2Application Load Balancer or Network Load Balancer is required for an Amazon ECS deployment.
*Required*: No
*Type*: String
*Allowed values*: `WITH_TRAFFIC_CONTROL | WITHOUT_TRAFFIC_CONTROL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeploymentType`  <a name="cfn-codedeploy-deploymentgroup-deploymentstyle-deploymenttype"></a>
Indicates whether to run an in-place or blue/green deployment.
*Required*: No
*Type*: String
*Allowed values*: `IN_PLACE | BLUE_GREEN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-codedeploy-deploymentgroup-deploymentstyle--seealso"></a>
+ [EC2TagFilter](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_EC2TagFilter.html) in the *AWS CodeDeploy API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
