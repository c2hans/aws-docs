---
source_url: https://docs.aws.amazon.com/elemental-server/latest/ug/using-dolby-atmos-passthrough.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Using Dolby Atmos Passthrough with AWS Elemental Server
<a name="using-dolby-atmos-passthrough"></a>

AWS Elemental Server can create Dolby Digital Plus with Atmos outputs by either encoding audio in 9.1.6, 7.1.4, or 5.1.4 PCM mono channels, or by passing through already encoded Dolby Digital Plus with Atmos content.

You set up your job to pass through Dolby Digital Plus with Atmos content in the same way that you pass through Dolby Digital and Dolby Digital Plus content.

**To set up a Dolby Atmos job, passing through finished audio content**

1. Set up your input audio and video as usual.

1. Create outputs and streams. To set up the audio in your streams, for **Audio Codec**, choose **Dolby Digital Pass Through**.

## Feature Restrictions for Dolby Atmos Passthrough
<a name="feature-restrictions-for-dolby-atmos-passthrough"></a>

Note the following restrictions in the AWS Elemental Server implementation of Dolby Atmos passthrough:
+ **Output codec:** You can create Dolby Atmos audio outputs encoded with only the Dolby Digital Plus (EAC3) codec.
+ **Output containers:** For file outputs, you can create Dolby Atmos audio in only one of the video containers that supports Dolby Digital Plus: MPEG-4, MPEG-2 Transport Stream, or QuickTime.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
