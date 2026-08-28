---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-client-track.html
---

# Track matchmaking events
<a name="match-client-track"></a>

Set up notifications to track events that Amazon GameLift Servers emits for matchmaking processes. You can set up notifications either directly, by creating an SNS topic, or by using Amazon EventBridge. For more information on setting up notifications, see [Set up FlexMatch event notifications](match-notification.md). Once you've set up notifications, add a listener on your client service to detect the events and respond as needed.

It's also a good idea to back up notifications by periodically polling for status updates when a significant period of time passes without notification. To minimize impact on matchmaking performance, be sure to poll only after waiting at least 30 seconds after the matchmaking ticket was submitted or after the last received notification.

Retrieve a matchmaking request ticket, including current status, by calling [DescribeMatchmaking](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeMatchmaking.html) with the request's ticket ID. We recommend polling no more than once every 10 seconds. This approach is for use during low-volume development scenarios only.

**Note**
You should set up your game with event notifications before you have high-volume matchmaking usage, such as with pre-production load testing. All games in public release should use notifications regardless of volume. The continuous polling approach is only appropriate for games in development with low matchmaking usage.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
