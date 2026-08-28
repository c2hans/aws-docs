---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/default-rooms.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Default rooms
<a name="default-rooms"></a>

When the super administrator has enabled the default room option, network administrators can create rooms managed by a bot. This bot will automatically add users to a room. If users leave the room, they will be re-added.

A room can be made for all users in the network, for specific security groups, or both.

In these rooms, there are no other moderators other than the default room bot, so settings and users can’t be managed within the app by end users.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
