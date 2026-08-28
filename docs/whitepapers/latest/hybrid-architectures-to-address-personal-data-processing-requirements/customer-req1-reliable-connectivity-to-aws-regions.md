---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/customer-req1-reliable-connectivity-to-aws-regions.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# CUSTOMER-REQ1 – Reliable connectivity to AWS Regions
<a name="customer-req1-reliable-connectivity-to-aws-regions"></a>

 For reliable and stable latency connectivity from countries without AWS Region or Local Zones to AWS Regions in the EU, AWS recommends using [AWS Direct Connect](https://aws.amazon.com/directconnect/) (with [MACSec](https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACsec.html) or [AWS Site-to-site VPN](https://aws.amazon.com/vpn/) for additional data in transit security).

 This requirement is addressed in the following reference architectures:
+  1.1 [*Hybrid network connectivity from a data center to the AWS Cloud*](hybrid-network-connectivity-from-a-data-center-to-the-aws-cloud.md)
+  2.3 [*Industrial IoT with AWS IoT Greengrass*](industrial-iot-with-aws-iot-greengrass.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
