---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-gamesessionqueue-gamesessionqueuedestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::GameSessionQueue GameSessionQueueDestination
<a name="aws-properties-gamelift-gamesessionqueue-gamesessionqueuedestination"></a>

A fleet or alias designated in a game session queue. Queues fulfill requests for new game sessions by placing a new game session on any of the queue's destinations.

## Syntax
<a name="aws-properties-gamelift-gamesessionqueue-gamesessionqueuedestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-gamesessionqueue-gamesessionqueuedestination-syntax.json"></a>

```
{
  "[DestinationArn](#cfn-gamelift-gamesessionqueue-gamesessionqueuedestination-destinationarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-gamesessionqueue-gamesessionqueuedestination-syntax.yaml"></a>

```
  [DestinationArn](#cfn-gamelift-gamesessionqueue-gamesessionqueuedestination-destinationarn): {{String}}
```

## Properties
<a name="aws-properties-gamelift-gamesessionqueue-gamesessionqueuedestination-properties"></a>

`DestinationArn`  <a name="cfn-gamelift-gamesessionqueue-gamesessionqueuedestination-destinationarn"></a>
The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9:/-]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
