---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-game-development.html
---

# Game development services
<a name="sns-event-sources-game-development"></a>

The following table describes how Amazon SNS integrates with Amazon GameLift Servers to provide notifications for matchmaking and queue events in session-based multiplayer game servers.

This integration helps game developers automate and monitor the deployment, operation, and scaling of their game servers, ensuring a seamless gaming experience.

| AWS service | Benefit of using with Amazon SNS |
| --- | --- |
| [Amazon GameLift Servers](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-intro.html) – Provides solutions for hosting session-based multiplayer game servers in the cloud, including a fully managed service for deploying, operating, and scaling game servers. | Receive matchmaking and queue event notifications. For more information, see the following pages:+  For matchmaking notifications, see [Set up FlexMatch event notification](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html) in the *Amazon GameLift Servers FlexMatch Developer Guide*. <br />+  For queue notifications, see [Set up event notification for game session placement](https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html) in the *Amazon GameLift Servers Developer Guide*.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
