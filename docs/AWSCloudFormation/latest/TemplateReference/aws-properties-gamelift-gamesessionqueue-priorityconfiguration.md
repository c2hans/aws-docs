---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-gamesessionqueue-priorityconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::GameSessionQueue PriorityConfiguration
<a name="aws-properties-gamelift-gamesessionqueue-priorityconfiguration"></a>

Custom prioritization settings for use by a game session queue when placing new game sessions with available game servers. When defined, this configuration replaces the default FleetIQ prioritization process, which is as follows:
+ If player latency data is included in a game session request, destinations and locations are prioritized first based on lowest average latency (1), then on lowest hosting cost (2), then on destination list order (3), and finally on location (alphabetical) (4). This approach ensures that the queue's top priority is to place game sessions where average player latency is lowest, and--if latency is the same--where the hosting cost is less, etc.
+ If player latency data is not included, destinations and locations are prioritized first on destination list order (1), and then on location (alphabetical) (2). This approach ensures that the queue's top priority is to place game sessions on the first destination fleet listed. If that fleet has multiple locations, the game session is placed on the first location (when listed alphabetically).

Changing the priority order will affect how game sessions are placed.

## Syntax
<a name="aws-properties-gamelift-gamesessionqueue-priorityconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-gamesessionqueue-priorityconfiguration-syntax.json"></a>

```
{
  "[LocationOrder](#cfn-gamelift-gamesessionqueue-priorityconfiguration-locationorder)" : {{[ String, ... ]}},
  "[PriorityOrder](#cfn-gamelift-gamesessionqueue-priorityconfiguration-priorityorder)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-gamelift-gamesessionqueue-priorityconfiguration-syntax.yaml"></a>

```
  [LocationOrder](#cfn-gamelift-gamesessionqueue-priorityconfiguration-locationorder): {{
    - String}}
  [PriorityOrder](#cfn-gamelift-gamesessionqueue-priorityconfiguration-priorityorder): {{
    - String}}
```

## Properties
<a name="aws-properties-gamelift-gamesessionqueue-priorityconfiguration-properties"></a>

`LocationOrder`  <a name="cfn-gamelift-gamesessionqueue-priorityconfiguration-locationorder"></a>
The prioritization order to use for fleet locations, when the `PriorityOrder` property includes `LOCATION`. Locations can include AWS Region codes (such as `us-west-2`), local zones, and custom locations (for Anywhere fleets). Each location must be listed only once. For details, see [Amazon GameLift Servers service locations.](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html)
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `64 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PriorityOrder`  <a name="cfn-gamelift-gamesessionqueue-priorityconfiguration-priorityorder"></a>
A custom sequence to use when prioritizing where to place new game sessions. Each priority type is listed once.
+ `LATENCY` -- Amazon GameLift Servers prioritizes locations where the average player latency is lowest. Player latency data is provided in each game session placement request.
+ `COST` -- Amazon GameLift Servers prioritizes queue destinations with the lowest current hosting costs. Cost is evaluated based on the destination's location, instance type, and fleet type (Spot or On-Demand).
+ `DESTINATION` -- Amazon GameLift Servers prioritizes based on the list order of destinations in the queue configuration.
+ `LOCATION` -- Amazon GameLift Servers prioritizes based on the provided order of locations, as defined in `LocationOrder`.
*Required*: No
*Type*: Array of String
*Allowed values*: `LATENCY | COST | DESTINATION | LOCATION`
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
