---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/per-frame-metrics-troubleshooting.html
---

# Troubleshooting
<a name="per-frame-metrics-troubleshooting"></a>

The following is a list of troubleshooting tips for issues that you might encounter while working with per-frame metric reports:

**Missing metric reports**
Verify that you've enabled the metrics at either the output group level or individual output level.

**QVBR metrics not appearing**
Confirm that your output settings include the QVBR rate control mode.

**Unexpected metric values**
Check that your content is appropriate for the selected metrics and review the interpretation guidelines for each metric type.

**Job taking too long**
Consider reducing the number of selected metrics or applying them to fewer outputs to reduce processing time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
