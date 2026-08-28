---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/mediapackage.html
---

# MediaPackage
<a name="mediapackage"></a>

This solution includes the option to use MediaPackage as part of the workflow. When activated, the solution creates a separate set of MediaConvert custom templates that include H.265 MP4 and HLS. The solution also creates a packaging group in MediaPackage that is configured to ingest the MediaConvert HLS output stored in Amazon S3. MediaPackage packages the content, formatting it in response to playback requests from downstream devices. By default, this solution creates packaging configurations for HLS, DASH, MSS, and CMAF.

**Important**
Customers who ingest large quantities of files may exceed MediaPackage limits for video-on-demand content. For more information and instructions on how to request a limit increase, refer to [VOD Content Limits](https://docs.aws.amazon.com/mediapackage/latest/ug/limits-vod.html) in the *AWS Elemental MediaPackage User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
