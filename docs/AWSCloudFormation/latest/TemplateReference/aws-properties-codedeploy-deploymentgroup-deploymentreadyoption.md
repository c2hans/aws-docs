---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-deploymentreadyoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentGroup DeploymentReadyOption
<a name="aws-properties-codedeploy-deploymentgroup-deploymentreadyoption"></a>

Information about how traffic is rerouted to instances in a replacement environment in a blue/green deployment.

## Syntax
<a name="aws-properties-codedeploy-deploymentgroup-deploymentreadyoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentgroup-deploymentreadyoption-syntax.json"></a>

```
{
  "[ActionOnTimeout](#cfn-codedeploy-deploymentgroup-deploymentreadyoption-actionontimeout)" : {{String}},
  "[WaitTimeInMinutes](#cfn-codedeploy-deploymentgroup-deploymentreadyoption-waittimeinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentgroup-deploymentreadyoption-syntax.yaml"></a>

```
  [ActionOnTimeout](#cfn-codedeploy-deploymentgroup-deploymentreadyoption-actionontimeout): {{String}}
  [WaitTimeInMinutes](#cfn-codedeploy-deploymentgroup-deploymentreadyoption-waittimeinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentgroup-deploymentreadyoption-properties"></a>

`ActionOnTimeout`  <a name="cfn-codedeploy-deploymentgroup-deploymentreadyoption-actionontimeout"></a>
Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.
+ CONTINUE\_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
+ STOP\_DEPLOYMENT: Do not register new instances with a load balancer unless traffic rerouting is started using [ContinueDeployment ](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ContinueDeployment.html). If traffic rerouting is not started before the end of the specified wait period, the deployment status is changed to Stopped.
*Required*: No
*Type*: String
*Allowed values*: `CONTINUE_DEPLOYMENT | STOP_DEPLOYMENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WaitTimeInMinutes`  <a name="cfn-codedeploy-deploymentgroup-deploymentreadyoption-waittimeinminutes"></a>
The number of minutes to wait before the status of a blue/green deployment is changed to Stopped if rerouting is not started manually. Applies only to the `STOP_DEPLOYMENT` option for `actionOnTimeout`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
