---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-hls-pull.html
---

# Channel input—HLS pull input
<a name="input-hls-pull"></a>

To verify that the input is set up correctly, look at the **Input sources** section. It shows the locations of the source video. You specified these locations when you created the input:
+ If the channel is set up as a standard channel, you specified two locations.
+ If the channel is set up as a single-pipeline channel, you specified one.

For example, for an HTTPS pull:

**https://203.0.113.13/sports/curling.m3u8** and

**https://203.0.113.54/sports/curling.m3u8**

Or, for a pull from an Amazon S3 bucket:

**s3ssl://amzn-s3-demo-bucket/filler-videos/main/oceanwaves.mp4** and

**s3ssl://amzn-s3-demo-bucket/filler-videos/redundant/oceanwaves.mp4**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
