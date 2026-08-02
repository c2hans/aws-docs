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
|  Clipboard  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/data-loss-prevention.html)  |  Disabling this setting does not disable copy and paste within the session. If copying data into the session is required, choose Paste to remote session only to minimize the potential for data leakage.  |
|  File transfer  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/data-loss-prevention.html)  |  Avoid enabling this setting to prevent data leakage.  |
|  Print to local device  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/data-loss-prevention.html)  |  If printing is required, use network mapped printers that are controlled and monitored by your organization.  |

 Consider the advantages of the existing organizational data transfer solution over the stack settings. These configurations are not designed to replace a comprehensive secure data transfer solution.
