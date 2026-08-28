---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec05-bp01.html
---

# HNSEC05-BP01 Use IPSec VPN over Internet
<a name="hnsec05-bp01"></a>

 For hybrid network connectivity over the internet, IPSec VPN services can be used to create encrypted tunnels between cloud and on-premises environments.

 **Desired outcome:** Ensure that all data transmitted between AWS and on-premises networks over the internet is encrypted and protected from unauthorized access.

 **Level of risk exposed if this best practice is not established:** High

 **Benefits of establishing this best practice:**
+  Provides encryption for data in transit
+  Reduces risk of data interception or tampering over public networks
+  Supports compliance with security and privacy requirements
+  Enables secure, flexible hybrid networking without dedicated links

## Implementation guidance
<a name="implementation-guidance-22"></a>
+  Establish IPSec VPN tunnels between your cloud and on-premises network, such as using AWS Site-to-Site VPN.
+  Configure VPN endpoints to enforce strong encryption and authentication.
+  Monitor tunnel health and activity.
+  Ensure only approved subnets and IP ranges are routable over the VPN.

## Resources
<a name="resources-20"></a>
+  [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
+  [Get started with AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
