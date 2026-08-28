---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/thumbnails.html
---

# Viewing input thumbnails
<a name="thumbnails"></a>

MediaLive can generate thumbnails for the video from inputs in your channels. The thumbnail provides a visual verification that the content contains video. You can view the thumbnails for each channel on the MediaLive console. You can also use one of the AWS APIs to work with thumbnails programmatically.

**How thumbnails are generated**

When you have enabled thumbnails in a channel and the channel is running, MediaLive generates a JPEG thumbnail every 2 seconds. The thumbnail exists for only 2 seconds, until it gets replaced by the next thumbnail. Each input has its own thumbnail, which means that MediaLive generates one thumbnail for a single-pipeline channel, and two thumbnails for a standard channel.

As soon as the thumbnail is generated, MediaLive displays it on the console, in the channel details page. It also makes the thumbnail available as binary data. You can use an AWS API to work with the binary data programmatically.

**Encryption of the thumbnail**

MediaLive always encrypts each thumbnail as it is created.

**Topics**
+ [Enabling thumbnails in a channel](thumbnails-enable.md)
+ [Viewing thumbnails on the console](thumbnails-view.md)
+ [Retrieving thumbnails programmatically](thumbnails-work-cli.md)
+ [Limit on thumbnails in MediaLive](thumbnail-limits.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
