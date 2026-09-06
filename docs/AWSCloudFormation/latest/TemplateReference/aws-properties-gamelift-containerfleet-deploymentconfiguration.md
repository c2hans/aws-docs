---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containerfleet-deploymentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerFleet DeploymentConfiguration
<a name="aws-properties-gamelift-containerfleet-deploymentconfiguration"></a>

Set of rules for processing a deployment for a container fleet update.

## Syntax
<a name="aws-properties-gamelift-containerfleet-deploymentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containerfleet-deploymentconfiguration-syntax.json"></a>

```
{
  "[ImpairmentStrategy](#cfn-gamelift-containerfleet-deploymentconfiguration-impairmentstrategy)" : {{String}},
  "[MinimumHealthyPercentage](#cfn-gamelift-containerfleet-deploymentconfiguration-minimumhealthypercentage)" : {{Integer}},
  "[ProtectionStrategy](#cfn-gamelift-containerfleet-deploymentconfiguration-protectionstrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-containerfleet-deploymentconfiguration-syntax.yaml"></a>

```
  [ImpairmentStrategy](#cfn-gamelift-containerfleet-deploymentconfiguration-impairmentstrategy): {{String}}
  [MinimumHealthyPercentage](#cfn-gamelift-containerfleet-deploymentconfiguration-minimumhealthypercentage): {{Integer}}
  [ProtectionStrategy](#cfn-gamelift-containerfleet-deploymentconfiguration-protectionstrategy): {{String}}
```

## Properties
<a name="aws-properties-gamelift-containerfleet-deploymentconfiguration-properties"></a>

`ImpairmentStrategy`  <a name="cfn-gamelift-containerfleet-deploymentconfiguration-impairmentstrategy"></a>
Determines what actions to take if a deployment fails. If the fleet is multi-location, this strategy applies across all fleet locations. With a rollback strategy, updated fleet instances are rolled back to the last successful deployment. Alternatively, you can maintain a few impaired containers for the purpose of debugging, while all other tasks return to the last successful deployment.
*Required*: No
*Type*: String
*Allowed values*: `MAINTAIN | ROLLBACK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumHealthyPercentage`  <a name="cfn-gamelift-containerfleet-deploymentconfiguration-minimumhealthypercentage"></a>
Sets a minimum level of healthy tasks to maintain during deployment activity.
*Required*: No
*Type*: Integer
*Minimum*: `30`
*Maximum*: `75`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtectionStrategy`  <a name="cfn-gamelift-containerfleet-deploymentconfiguration-protectionstrategy"></a>
Determines how fleet deployment activity affects active game sessions on the fleet. With protection, a deployment honors game session protection, and delays actions that would interrupt a protected active game session until the game session ends. Without protection, deployment activity can shut down all running tasks, including active game sessions, regardless of game session protection.
*Required*: No
*Type*: String
*Allowed values*: `WITH_PROTECTION | IGNORE_PROTECTION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
