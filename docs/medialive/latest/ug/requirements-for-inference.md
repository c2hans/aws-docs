---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-inference.html
---

# Requirements for Elemental Inference
<a name="requirements-for-inference"></a>

Your organization might implement [AWS Elemental Inference features](elemental-inference.md) in a channel. Users who configure the channel to use these features need permissions to work with feeds.
+ Users need permissions to work with feeds. Users need these permissions even though they are using the MediaLive console or API to set up the feeds and to associate the channel with the feed.
+ Users need permissions to let MediaLive perform setup on a feed after the channel has been created or modified. The setup involves associating the channel with the feed. MediaLive uses IAM forward access sessions (FAS) to send and retrieve.

| Permissions | Service name in IAM | Actions |
| --- | --- | --- |
| When configuring a channel, so that MediaLive can work with the Elemental Inference feed. | Elemental Inference | CreateFeed`DeleteFeed`<br />`GetFeed`<br />`ListFeeds`<br />`UpdateFeed` |
| After configuration of a channel, so that MediaLive can use FAS to associate the channel with the Elemental Inference feed. | Elemental Inference | `AssociateFeed`<br />`DisassociateFeed`<br />`GetFeed` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
