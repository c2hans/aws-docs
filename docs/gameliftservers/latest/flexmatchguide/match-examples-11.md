---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-examples-11.html
---

# Example: Create a rule that uses a player's block list
<a name="match-examples-11"></a>

This example illustrates a rule set that lets players avoid being matched with certain other players. Players can create a block list, which the matchmaker evaluates during player selection for a match. For more guidance on adding a block list or avoid list feature, see [AWS for Games Blog](https://aws.amazon.com/blogs/gametech/category/game-development/amazon-gamelift/).

This example sets out the following instructions:
+ Create two teams of exactly five players.
+ Pass in a player's block list, which is a list of player IDs (up to 100).
+ Compare all players against each player's block list and reject a proposed match if any blocked player IDs are found.

Notes on using this rule set:
+ When evaluating a new player to add to a proposed match (or to backfill a spot in an existing match), the player might be rejected for either of the following reasons:
  + If the new player is on a block list for any players that are already selected for the match.
  + If any players that are already selected for the match are on the new player's block list.
+ As shown, this rule set prevents matching a player with any player on their block list. You can change this requirement to a preference (also called an "avoid" list) by adding a rule expansion and increasing the `maxCount` value.

```
{
    "name": "Player Block List",
    "ruleLanguageVersion": "1.0",
    "teams": [{
        "maxPlayers": 5,
        "minPlayers": 5,
        "name": "red"
    }, {
        "maxPlayers": 5,
        "minPlayers": 5,
        "name": "blue"
    }],
    "playerAttributes": [{
        "name": "BlockList",
        "type": "string_list",
        "default": []
    }],
    "rules": [{
        "name": "PlayerIdNotInBlockList",
        "type": "collection",
        "operation": "reference_intersection_count",
        "measurements": "flatten(teams[*].players.attributes[BlockList])",
        "referenceValue": "flatten(teams[*].players[playerId])",
        "maxCount": 0
    }]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
