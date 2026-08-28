---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-examples-6.html
---

# Example: Compare attributes across all players
<a name="match-examples-6"></a>

This example illustrates how to compare player attributes across a group of players.

The example rule set describes a match with the following characteristics:
+ Team structure: Two single-player teams
+ Player attributes:
  + *gameMode*: Type of game chosen by the player (if not provided, default to "turn-based").
  + *gameMap*: Game world chosen by the player (if not provided, default to 1).
  + *character*: Character chosen by the player (no default value means that players must specify a character).
+ Match rules: Matched players must meet the following requirements:
  + Players must choose the same game mode.
  + Players must choose the same game map.
  + Players must choose different characters.

Notes on using this rule set:
+ To implement the match rule, this example uses comparison rules to check all players' attribute values. For game mode and map, the rule verifies that the values are the same. For character, the rule verifies that the values are different.
+ This example uses one player definition with a quantity property to create both player teams. The team are assigned the following names: "player\_1" and "player\_2".

```
{
    "name": "",
    "ruleLanguageVersion": "1.0",

    "playerAttributes": [{
        "name": "gameMode",
        "type": "string",
        "default": "turn-based"
    }, {
        "name": "gameMap",
        "type": "number",
        "default": 1
    }, {
        "name": "character",
        "type": "number"
    }],

    "teams": [{
        "name": "player",
        "minPlayers": 1,
        "maxPlayers": 1,
        "quantity": 2
    }],

    "rules": [{
        "name": "SameGameMode",
        "description": "Only match players when they choose the same game type",
        "type": "comparison",
        "operation": "=",
        "measurements": ["flatten(teams[*].players.attributes[gameMode])"]
    }, {
        "name": "SameGameMap",
        "description": "Only match players when they're in the same map",
        "type": "comparison",
        "operation": "=",
        "measurements": ["flatten(teams[*].players.attributes[gameMap])"]
    }, {
        "name": "DifferentCharacter",
        "description": "Only match players when they're using different characters",
        "type": "comparison",
        "operation": "!=",
        "measurements": ["flatten(teams[*].players.attributes[character])"]
    }]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
