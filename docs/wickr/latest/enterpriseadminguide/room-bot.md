---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/room-bot.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Manage Room Bot
<a name="room-bot"></a>

The Room Bot allows network administrators to deploy pre-created rooms managed by this bot. The bot will add all users in a particular security group or network to a room and automatically re-add users if they attempt to leave. Multiple rooms can be created for any group.

The Room Bot is disabled, by default, and can be enabled anytime. If disabled after network administrators have created rooms, all active rooms will still exist, however, they will not be able to be managed and will always have the same members.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
