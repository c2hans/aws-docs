---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/url-pull-hls-input-configuration.html
---

# URL Pull (HLS) input configuration
<a name="url-pull-hls-input-configuration"></a>

URL Pull provides the option to ingest an HLS stream over HTTP or HTTPS. The following parameters are required to configure the solution to ingest an HLS stream:
+  **Source Input Type** - URL\_PULL
+  **Source URL** - The HTTP(s) link to the HLS stream manifest file. The default value is a demo stream from AWS.
+  **Source Username** - Only required if you have basic authentication setup on your source HLS stream.
+  **Source Password** - Only required if you have basic authentication setup on your source HLS stream.
+  **Encoding Profile** - Select the profile that best matches your source resolution.
+  **Start MediaLive Channel** - If your device is ready to stream, select **true**. Otherwise, select **false**--you can start the MediaLive channel through the AWS console when you’re ready to stream.

**Note**
Refer to [Creating an input](https://docs.aws.amazon.com/medialive/latest/ug/create-input.html) in the *AWS Elemental MediaLive User Guide* for a full list of input types and configuration details.

 **URL Pull (HLS) input configuration**

![hls input config](http://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/images/hls-input-config.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Live Streaming on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
