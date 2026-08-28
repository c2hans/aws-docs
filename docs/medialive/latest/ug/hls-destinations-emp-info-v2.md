---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/hls-destinations-emp-info-v2.html
---

# Collect the information for MediaPackage v2
<a name="hls-destinations-emp-info-v2"></a>

For MediaPackage v2, the two URLs for a channel look like these examples:

`mz82o4-1.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/live-sports/1/curling/index`

`mz82o4-2.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/live-sports/2/curling/index`

Where:

| Element | Description |
| --- | --- |
| mz82o4-1 and mz82o4-2 |  Indicate that the two endpoints are for a redundant channel in MediaPackage. The prefixes are always -1 and -2 |
| mediapackagev2 | Indicates that the input endpoints uses version 2 of the MediaPackage API |
| live-sports/1/curling and live-sports/2/curling | Folders for the redundant ingests. One folder always includes /1/, and the other folder always includes /2/  |
| index | Always appears at the end of the URL. It is the base filename for all the files for this destination.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
