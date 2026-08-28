---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/thumbnail-limits.html
---

# Limit on thumbnails in MediaLive
<a name="thumbnail-limits"></a>

There is a limit to the number of MediaLivethumbnails that you can view or retrieve. The limit is:

`A number of API transactions per second, per account, in one Region`

The transaction limit is shared by all thumbnails — those that you display on the console, and those that you retrieve using an AWS API. For the current limit, see the MediaLive page in the [Service Quotas](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/medialive/quotas) console.

On the console, a thumbnail is generated for a channel only when the channel details page is displayed, and only in the active tab (meaning only for one pipeline in the channel). For the relevant pipelines, MediaLive makes a call to the API approximately every 2 seconds.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
