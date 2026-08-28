---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containerfleet-gamesessioncreationlimitpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerFleet GameSessionCreationLimitPolicy
<a name="aws-properties-gamelift-containerfleet-gamesessioncreationlimitpolicy"></a>

A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control players' ability to consume available resources.

The policy is evaluated when a player tries to create a new game session. On receiving a `CreateGameSession` request, Amazon GameLift Servers checks that the player (identified by `CreatorId`) has created fewer than game session limit in the specified time period.

## Syntax
<a name="aws-properties-gamelift-containerfleet-gamesessioncreationlimitpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containerfleet-gamesessioncreationlimitpolicy-syntax.json"></a>

```
{
  "[NewGameSessionsPerCreator](#cfn-gamelift-containerfleet-gamesessioncreationlimitpolicy-newgamesessionspercreator)" : {{Integer}},
  "[PolicyPeriodInMinutes](#cfn-gamelift-containerfleet-gamesessioncreationlimitpolicy-policyperiodinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-gamelift-containerfleet-gamesessioncreationlimitpolicy-syntax.yaml"></a>

```
  [NewGameSessionsPerCreator](#cfn-gamelift-containerfleet-gamesessioncreationlimitpolicy-newgamesessionspercreator): {{Integer}}
  [PolicyPeriodInMinutes](#cfn-gamelift-containerfleet-gamesessioncreationlimitpolicy-policyperiodinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-gamelift-containerfleet-gamesessioncreationlimitpolicy-properties"></a>

`NewGameSessionsPerCreator`  <a name="cfn-gamelift-containerfleet-gamesessioncreationlimitpolicy-newgamesessionspercreator"></a>
A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control players' ability to consume available resources.
The policy evaluates when a player tries to create a new game session. On receiving a `CreateGameSession` request, Amazon GameLift Servers checks that the player (identified by `CreatorId`) has created fewer than game session limit in the specified time period.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyPeriodInMinutes`  <a name="cfn-gamelift-containerfleet-gamesessioncreationlimitpolicy-policyperiodinminutes"></a>
The time span used in evaluating the resource creation limit policy.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
