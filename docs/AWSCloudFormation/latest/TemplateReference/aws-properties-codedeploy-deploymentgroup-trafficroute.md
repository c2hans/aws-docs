---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-trafficroute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentGroup TrafficRoute
<a name="aws-properties-codedeploy-deploymentgroup-trafficroute"></a>

 Information about a listener. The listener contains the path used to route traffic that is received from the load balancer to a target group.

## Syntax
<a name="aws-properties-codedeploy-deploymentgroup-trafficroute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentgroup-trafficroute-syntax.json"></a>

```
{
  "[ListenerArns](#cfn-codedeploy-deploymentgroup-trafficroute-listenerarns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentgroup-trafficroute-syntax.yaml"></a>

```
  [ListenerArns](#cfn-codedeploy-deploymentgroup-trafficroute-listenerarns): {{
    - String}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentgroup-trafficroute-properties"></a>

`ListenerArns`  <a name="cfn-codedeploy-deploymentgroup-trafficroute-listenerarns"></a>
 The Amazon Resource Name (ARN) of one listener. The listener identifies the route between a target group and a load balancer. This is an array of strings with a maximum size of one.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
