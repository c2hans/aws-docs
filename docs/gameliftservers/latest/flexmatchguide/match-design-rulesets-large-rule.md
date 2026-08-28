---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-design-rulesets-large-rule.html
---

# Set rules for large matches
<a name="match-design-rulesets-large-rule"></a>

Matchmaking for large matches relies primarily on the balancing strategy and latency batching optimizations. Most custom rules are not available. However, you can incorporate the following types of rules:
+ Rule that sets a hard limit on player latency. Use the `latency` rule type with the property `maxLatency`. See [Latency rule](match-rules-reference-ruletype.md#match-rules-reference-ruletype-latency) reference. Here's an example that sets maximum player latency to 200 milliseconds:

  ```
  "rules": [{
          "name": "player-latency",
          "type": "latency",
          "maxLatency": 200
      }],
  ```
+ Rule to batch players based on closeness in a specified player attribute. This is different than defining a balancing attribute as part of the large-match algorithm, which focuses on building evenly matched teams. This rule batches matchmaking tickets based on similarity in the specified attribute values, such as beginner or expert skill, which tends to lead to matches players who are closely aligned on the specified attribute. Use the `batchDistance` rule type, identify a numerically-based attribute, and specify the widest range to allow. See [Batch distance rule](match-rules-reference-ruletype.md#match-rules-reference-ruletype-batchdistance) reference. Here's an example that calls for a match's players to be within one skill level of each other:

  ```
  "rules": [{
          "name": "batch-skill",
          "type": "batchDistance",
          "batchAttribute": "skill",
          "maxDistance": 1
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
