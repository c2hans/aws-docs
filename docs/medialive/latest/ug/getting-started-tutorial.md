---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/getting-started-tutorial.html
---

# AWS Elemental MediaLive tutorial
<a name="getting-started-tutorial"></a>

This tutorial describes how to ingest a video source from an RTP source and generate one HLS output that contains one H.264 video encode and one audio encode. MediaLive will send the output to AWS Elemental MediaPackage. The output will consist of the following:
+ One parent manifest: channel.m3u8
+ One rendition manifest: channel-1.m3u8
+ TS files for each output: channel-1.00001.ts, channel-1.00002.ts, channel-1.00003.ts, and so on

This tutorial uses the default values for most configuration fields in the channel.

**Note**
All the text marked as an example in this tutorial is just that—a sample that shows what a piece of information typically looks like. You must replace each example with the information that is valid for your situation.

**Topics**
+ [Prerequisites for the tutorial](getting-started-prerequisites.md)
+ [Step 1: Set up the upstream system](getting-started-step1.md)
+ [Step 2: Set up the downstream system](getting-started-step2.md)
+ [Step 3: Create an input](getting-started-step3.md)
+ [Step 4: Set up key information](getting-started-step4.md)
+ [Step 5: Attach the input](getting-started-step4b.md)
+ [Step 6: Set up input video, audio, captions](getting-started-step4a-input-selectors.md)
+ [Step 7: Create an HLS output group](getting-started-step5.md)
+ [Step 8: Set up the output and encodes](getting-started-step6.md)
+ [Step 9: Create your channel](getting-started-step7.md)
+ [Step 10: Start the upstream system and the channel](getting-started-step8.md)
+ [Step 11: Clean up](getting-started-step9.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
