---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec02-bp01.html
---

# ADVSEC02-BP01 Encrypt DSP to SSP communication in transit using TLS
<a name="advsec02-bp01"></a>

 Protect data in transit by using encrypted communication channel at the network communication level.

## Implementation guidance
<a name="implementation-guidance-13"></a>

 Protecting data that is transmitted from network to network remains a top security priority. Data confidentiality, integrity, and authenticity of the supported workloads are crucial for securing sensitive information, preventing unauthorized access, and enabling reliable operations within the workload.

 Use [AWS PrivateLink](https://aws.amazon.com/privatelink/) to establish connectivity between Amazon VPCs and other services without exposing the data to the public internet. If you have on-premises resources, consider using [AWS Direct Connect](https://aws.amazon.com/directconnect/). Direct Connect can make it easy to establish private connectivity between an AWS datacenter and your internal network. Implementing MACsec security on your Direct Connect connection provides point-to-point encryption for your traffic.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
