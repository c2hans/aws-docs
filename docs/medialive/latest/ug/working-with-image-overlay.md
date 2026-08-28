---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/working-with-image-overlay.html
---

# Working with image overlays
<a name="working-with-image-overlay"></a>

You can impose static images onto a video in a MediaLive channel. A static image is a still image that doesn't have motion. You prepare the image or images and store them outside of MediaLive. You then use the [schedule](working-with-schedule.md) feature in MediaLive to set up a timetable that specifies when images will be inserted in the running channel, and when each will be removed.

**Topics**
+ [Two options: global overlay and per-output overlay](image-overlay-features.md)
+ [Preparing the static image overlay file](image-overlay-prepare-step.md)
+ [Handling encode sharing](image-overlay-encode-sharing.md)
+ [Inserting and removing an overlay](image-overlay-insert.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
