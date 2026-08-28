---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/developerguide/api-limits-resource-throttling.html
---

# Resource-level throttling
<a name="api-limits-resource-throttling"></a>

Some API operations are subject to resource-level throttling to prevent database hot key issues. While increasing API-level limits for these operations, they may still be throttled at the resource level.

The following API operations are subject to resource-level throttling:
+ DescribeGameSessionPlacement
+ DescribeGameSessions
+ DescribeMatchmaking
+ DescribePlayerSessions

Resource-level throttling is enforced using specific throttle keys that include resource identifiers. For example, DescribeGameSessionPlacement uses the key "Operation:GameLift/DescribeGameSessionPlacement,aws-account-placement-id:" which enforces throttling per account and placement ID combination. This prevents customers from overwhelming the system with requests for specific resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
