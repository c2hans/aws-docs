---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/mediaconvert-templates.html
---

# MediaConvert templates
<a name="mediaconvert-templates"></a>

The Video on Demand on AWS solution outputs 4K, 1080p, and 720p MP4, and any combination of 1080p, 720p, 540p, 360p, and 270p HLS and DASH. By default, the solution selects the job template for MediaConvert based on the source video height. The solution includes three default job templates:
+ MediaConvert\_Template\_2160p: 5 HLS outputs AVC 2160p through 270p
+ MediaConvert\_Template\_1080p: 5 HLS outputs AVC 1080p through 270p
+ MediaConvert\_Template\_720p: 4 HLS outputs AVC 720p through 270p

By default, the solution is configured to leverage Quality-Defined Variable Bitrate (QVBR) mode in MediaConvert. The QVBR settings are configured to the recommended values for each output, as shown in the following table.

| Resolution | Maximum Bitrate | QVBR Quality Level |
| --- | --- | --- |
| 2160p | 15,000 Kbps | 9 |
| 1080p | 8,500 Kbps | 8 |
| 720p | 6,000 Kbps | 8 |
| 540p | 3,500 Kbps | 7 |
| 360p | 1,500 Kbps | 7 |
| 270p | 400 Kbps | 7 |

You can also modify the solution to use different QVBR settings, other system job templates, or your own custom job templates. For more information about working with job templates for MediaConvert, refer to [Working with MediaConvert Job Templates](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-job-templates.html). For more information about QVBR Mode, refer to [Using the QVBR Rate Control Mode](https://docs.aws.amazon.com/mediaconvert/latest/ug/cbr-vbr-qvbr.html).

If you set the solution to ingest source videos and metadata files, you can specify the template using the **JobTemplate** field in your metadata file. For more information, refer to [Metadata file](metadata-file.md). Or, you can replace the default templates in the Input Validate AWS Lambda function by modifying the `MediaConvert_Template_` {{<resolution>}} environment variables.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
