---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/downstream-system-cmafi-empv2.html
---

# Obtain destination for a CMAF Ingest output group
<a name="downstream-system-cmafi-empv2"></a>

1. Decide if you need two destination URLs for the output:
   + You need two destinations in a [standard channel](plan-redundancy.md).
   + You need one destination in a single-pipeline channel.

1. Obtain the one or two URLs from the MediaPackage operator. The MediaPackage terminology for the URL is *input endpoint*. Make sure that you obtain the URLs (which start with `https://`), not the channel name (which starts with `arn`).

   Note that you don't use user credentials to send to CMAF Ingest to MediaPackage.

**Example**

Two URLs look like this example:

`https://mz82o4-1.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/curling-channel-group/1/curling-channel/`

`https://mz82o4-2.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/curling-channel-group/1/curling-channel/`

Note the following:
+ The `v1/` near the end of the URL is the version of the MediaPackage destination URL schema, it doesn't refer to MediaPackage v1.
+ `curling-channel-group/` is the name of the channel group that the MediaPackage operator created.
+ `curling-channel/` is the name of the MediaPackage channel that the MediaPackage operator created. It isn't the name of the MediaLive channel.
+ The only difference in the two URLs is the `-1` and `-2` before `.ingest`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
