---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/data-loss-prevention.html
---

# Data Loss Prevention
<a name="data-loss-prevention"></a>

We'll look at two kinds of data loss prevention.

## Client to AppStream 2.0 Instance Data Transfer Controls
<a name="client-to-AppStream-instance-data-transfer-controls"></a>

 *Table 9 — Guidance for controlling data ingress and egress*

|  **Setting**  |  **Options**  |  **Guidance**  |
| --- | --- | --- |
|  Clipboard  |  +   Copy and paste to remote session only  <br />+   Copy to local device only  <br />+   Disabled    |  Disabling this setting does not disable copy and paste within the session. If copying data into the session is required, choose Paste to remote session only to minimize the potential for data leakage.  |
|  File transfer  |  +   Upload and download  <br />+   Upload only  <br />+   Download only  <br />+   Disabled    |  Avoid enabling this setting to prevent data leakage.  |
|  Print to local device  |  +   Enabled  <br />+   Disabled    |  If printing is required, use network mapped printers that are controlled and monitored by your organization.  |

 Consider the advantages of the existing organizational data transfer solution over the stack settings. These configurations are not designed to replace a comprehensive secure data transfer solution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
