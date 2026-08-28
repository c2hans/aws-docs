---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/hls-custom-manifests.html
---

# Fields for customizing the paths inside the manifests
<a name="hls-custom-manifests"></a>

Inside the main manifest, there are paths to each child manifest. Inside each child manifest, there are paths to the media files for that manifest.

You can optionally change the syntax of these paths. Typically, you only need to change the syntax if the downstream system has special path requirements.

The following fields relate to custom paths inside the manifests:
+ **HLS output group – Location** – the **Base URL content** fields.
+ **HLS output group – Location** – the **Base URL manifest** fields.

For more information about setting up custom paths in manifests, see [Customizing the paths inside HLS manifests](hls-manifest-paths.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
