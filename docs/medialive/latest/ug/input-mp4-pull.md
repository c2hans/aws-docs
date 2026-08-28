---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-mp4-pull.html
---

# Channel input—MP4 pull input
<a name="input-mp4-pull"></a>

To verify that the input is set up correctly, look at the **Input destinations** section. It shows the locations of the source video. You specified these locations when you created the input:
+ If the channel is set up as a standard channel, you specified two locations.
+ If the channel is set up as a single-pipeline channel, you specified one.

The format of the location depends on the type of upstream system:
+ For an upstream system that uses HTTP or HTTPS, the location is an HTTP or HTTPS URL. For example:

  **https://203.0.113.31/filler-videos/oceanwaves.mp4**

  **https://203.0.113.52/filler-videos/oceanwaves.mp4**
+ For a file that is stored on Amazon S3, the location is the bucket name and object for the file. For example:

  **s3ssl://amzn-s3-demo-bucket/filler-videos/main/oceanwaves.mp4**

  **s3ssl://amzn-s3-demo-bucket/filler-videos/redundant/oceanwaves.mp4**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
