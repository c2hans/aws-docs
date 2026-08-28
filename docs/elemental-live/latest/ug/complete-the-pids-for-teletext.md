---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/complete-the-pids-for-teletext.html
---

# Complete the PIDs for Teletext
<a name="complete-the-pids-for-teletext"></a>

This section applies when you set up the captions encode as described in [Step 1: Identify the source captions that you want](identify-captions-in-the-input.md), if the output group is UDP/TS and the output captions format is teletext. It describes how to complete the PIDs for the output that contains these captions.

**To complete the PIDs (teletext)**

1. In the Output section, open the PID Control section.

1. In the **DVB Teletext PID** field, enter the PID for the Teletext caption in the stream for this output. Or leave the default.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
