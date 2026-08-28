---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/cbr-vbr-qvbr.html
---

# Using the QVBR rate control mode
<a name="cbr-vbr-qvbr"></a>

The rate control mode that you choose for your output determines whether the encoder uses more data for complex parts of your video or maintains a constant amount of data per frame. This chapter provides guidance for choosing the right rate control mode for your asset, depending on how you plan to distribute it. In general, you get the best video quality for a given file size by using quality-defined variable bitrate (QVBR) for your rate control mode.

**Topics**
+ [Comparison of QVBR with other rate control modes](choosing-rate-control-mode.md)
+ [Configuring quality-defined variable bitrate mode](qvbr-guidelines.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
