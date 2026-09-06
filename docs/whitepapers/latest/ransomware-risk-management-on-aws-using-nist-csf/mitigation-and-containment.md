---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ransomware-risk-management-on-aws-using-nist-csf/mitigation-and-containment.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Mitigation and containment
<a name="mitigation-and-containment"></a>

 The Mitigation and containment component provides the ability to limit a destructive event’s effect on the enterprise.

* Table 10 — Mitigation and containment capability and the associated AWS services *

|  Capability and CSF mapping  |  AWS service  |  AWS service description  |  Function  |  [AWS GovCloud (US)](https://aws.amazon.com/govcloud-us/) available?  |
| --- | --- | --- | --- | --- |
|  Mitigation and containment <br /> DE.CM-5, RS.RP-1, RS.MI-1, RS.MI-2  |  [Amazon EC2 Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)  |  A security group is a virtual firewall that controls inbound and outbound traffic to your network resources and Amazon EC2 instance.  |  Provides capability to limit communication to allowed IP addresses.  |  Yes  |
|   |  [AWS Nitro Enclaves](https://aws.amazon.com/ec2/nitro/nitro-enclaves/)  |  AWS Nitro Enclaves enables customers to create isolated compute environments to further protect and securely process highly sensitive data such as personally identifiable information (PII), healthcare, financial, and intellectual property data within their Amazon EC2 instances. <br /> Nitro Enclaves uses the same [Nitro Hypervisor technology](https://aws.amazon.com/ec2/nitro/) that provides CPU and memory isolation for EC2 instances.  |  Provides an isolated run environment for signed code to handle sensitive data, accessible only by local virtual network socket interface.  |  Yes  |
