---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations-emp-info.html
---

# Collect the information for standard MediaPackage
<a name="hls-destinations-emp-info"></a>

For standard MediaPackage, the two URLs for a channel look like these examples:

`6d2c.mediapackage.us-west-2.amazonaws.com/in/v2/9dj8/9dj8/channel`

`6d2c.mediapackage.us-west-2.amazonaws.com/in/v2/9dj8/e333/channel`

Where:

`mediapackage` indicates that the input endpoints uses version 1 of the MediaPackage API

`channel` always appears at the end of the URL. It is the base filename for all the files for this destination.

The two URLs are always identical except for the folder just before `channel`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
