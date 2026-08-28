---
source_url: https://docs.aws.amazon.com/elemental-server/latest/ug/scte-message-processing.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Including SCTE-35 Markers with AWS Elemental Server
<a name="scte-message-processing"></a>

You can use AWS Elemental Server to manipulate the SCTE-35 messages in MPEG-2 transport stream (TS) inputs. These messages may or may not include segmentation descriptors. You can also use AWS Elemental Server to remove or include the cueing information conveyed by SCTE messages in the output streams (video, audio, closed captioning, data) and in any associated manifests. The processing instructions are all set up in the AWS Elemental Server job.

Note that AWS Elemental encoders do not support processing of manifests that are present in the input. The information in these manifests is not ingested by the AWS Elemental encoder and is not included in the output or the output manifest.

**About this topic**
SCTE messages may convey DPI cueing information for ad avails and for other non-ad-avail messages such as programs and chapters.

This topic covers both ESAM and non-ESAM processing of SCTE messages.

**Assumptions**
This topic assumes you are familiar with the following:
+ SCTE-35 standards and how the input you are encoding implements these standards
+ Profiles and with managing AWS Elemental Server jobs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
