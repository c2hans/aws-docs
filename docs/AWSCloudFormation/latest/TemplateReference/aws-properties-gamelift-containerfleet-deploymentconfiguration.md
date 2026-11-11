---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containerfleet-deploymentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerFleet DeploymentConfiguration
<a name="aws-properties-gamelift-containerfleet-deploymentconfiguration"></a>

Set of rules for processing a deployment for a container fleet update. For how Amazon GameLift Servers validates and rolls out a deployment, see [Container fleet deployments](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/containers-deployment-validation.html).

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
Determines what actions to take if a deployment fails validation. If the fleet is multi-location, this strategy applies across all fleet locations.
+ `ROLLBACK` -- Returns all of the fleet's containers to the last successful deployment.
+ `MAINTAIN` -- Keeps the containers that failed validation in place so that you can inspect them, and returns all other containers to the last successful deployment. Use this option when you're deploying a container image that you want to be able to debug on failure.
Default value: `MAINTAIN`
*Required*: No
*Type*: String
*Allowed values*: `MAINTAIN | ROLLBACK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumHealthyPercentage`  <a name="cfn-gamelift-containerfleet-deploymentconfiguration-minimumhealthypercentage"></a>
Sets the minimum percentage of the fleet's game server container groups to keep healthy during deployment activity. A low value favors deployment speed; a high value favors game server availability. For example, if the fleet runs 20 game server container groups and this value is 75, Amazon GameLift Servers keeps at least 15 of them healthy, so it replaces no more than 5 at a time.
Default value: 75
*Required*: No
*Type*: Integer
*Minimum*: `30`
*Maximum*: `75`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtectionStrategy`  <a name="cfn-gamelift-containerfleet-deploymentconfiguration-protectionstrategy"></a>
Determines how fleet deployment activity affects active game sessions on the fleet. A protected game session can't be terminated while it's active; a fleet sets the default protection for its new game sessions with `NewGameSessionProtectionPolicy`.
+ `WITH_PROTECTION` -- The deployment honors game session protection, and delays actions that would interrupt a protected active game session until the game session ends.
+ `IGNORE_PROTECTION` -- The deployment replaces containers regardless of game session activity, including active game sessions. This option is useful during development and testing.
This setting also affects how long deployment validation can take. When the fleet's `NewGameSessionProtectionPolicy` is `FullProtection` and the deployment uses `WITH_PROTECTION`, validation waits for protected game sessions to end.
Default value: `WITH_PROTECTION`
*Required*: No
*Type*: String
*Allowed values*: `WITH_PROTECTION | IGNORE_PROTECTION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
