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
