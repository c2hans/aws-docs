---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/scc-srt-output-captions.html
---

# SCC, SRT, and SMI (sidecar) output captions
<a name="scc-srt-output-captions"></a>

 This section covers how to configure SCC, SRT, and SMI (sidecar) output captions in AWS Elemental MediaConvert. The main topics include:
+ Where to specify the captions.
+ How to specify multiple captions tracks.

## Where to specify the captions
<a name="where-scc-srt-output-captions"></a>

Put your captions in the same output group, but a different output from your video.

After you add captions to an output, delete the **Video** and **Audio 1** groups of settings that the service automatically created with the output.

**To delete the Video and Audio 1 groups of settings**

1. On the **Create job** page, in the **Job** pane on the left, under **Output groups**, choose the output that contains the groups of settings that you want to delete.

1. The **Video** group of settings is automatically displayed in the **Stream settings** section. Choose the **Remove video selector** button.

1. The **Audio 1** group of settings is automatically displayed in the **Stream settings** section. Choose the **Remove** button.

## How to specify multiple captions tracks
<a name="multilang-scc-srt-output-captions"></a>

 For each SRT, SCC or SMI output you must have one output per caption selector. In the caption output, choose the captions selector under **Captions source** that is set up for the track that you want to include. They will appear in the list of settings groups as **Captions Selector 1**, **Captions Selector 2**, and so forth.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
