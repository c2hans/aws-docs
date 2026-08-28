---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/network-exclusions.html
---

# Network Exclusions
<a name="network-exclusions"></a>

 The WorkSpaces Applications management network range (`198.19.0.0/16`) and following ports and addresses should not be blocked by any security / firewall or antivirus solutions within WorkSpaces Applications instances.

 *Table 7 — Ports in WorkSpaces Applications streaming instances security software must not interfere with*

|  **Port**  |   **Usage**   |
| --- | --- |
|  8300  |  This is used for establishing the streaming connection  |
|  3128  |  This is used for managing the streaming instance by WorkSpaces Applications  |
|  8000  |  This is used for managing the streaming instance by WorkSpaces Applications  |
|  8443  |  This is used for managing the streaming instance by WorkSpaces Applications  |
|  53  |  DNS  |

 *Table 8 — WorkSpaces Applications managed service addresses security software must not interfere with*

|  **Port**  |  **Usage**  |
| --- | --- |
|  169.254.169.123  |  NTP  |
|  169.254.169.249  |  NVIDIA GRID License Service  |
|  169.254.169.250  |  KMS  |
|  169.254.169.251  |  KMS  |
|  169.254.169.253  |  DNS  |
|  169.254.169.254  |  Metadata  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
