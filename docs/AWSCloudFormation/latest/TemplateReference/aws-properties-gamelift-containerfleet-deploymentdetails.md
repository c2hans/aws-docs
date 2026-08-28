---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containerfleet-deploymentdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerFleet DeploymentDetails
<a name="aws-properties-gamelift-containerfleet-deploymentdetails"></a>

Information about the most recent deployment for the container fleet.

## Syntax
<a name="aws-properties-gamelift-containerfleet-deploymentdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containerfleet-deploymentdetails-syntax.json"></a>

```
{
  "[LatestDeploymentId](#cfn-gamelift-containerfleet-deploymentdetails-latestdeploymentid)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-containerfleet-deploymentdetails-syntax.yaml"></a>

```
  [LatestDeploymentId](#cfn-gamelift-containerfleet-deploymentdetails-latestdeploymentid): {{String}}
```

## Properties
<a name="aws-properties-gamelift-containerfleet-deploymentdetails-properties"></a>

`LatestDeploymentId`  <a name="cfn-gamelift-containerfleet-deploymentdetails-latestdeploymentid"></a>
A unique identifier for a fleet deployment.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-]+$|^$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
