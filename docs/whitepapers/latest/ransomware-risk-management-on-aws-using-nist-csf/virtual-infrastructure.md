---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ransomware-risk-management-on-aws-using-nist-csf/virtual-infrastructure.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Virtual infrastructure
<a name="virtual-infrastructure"></a>

 The Virtual Infrastructure component provides virtual capabilities to the enterprise for hosting applications and providing backup and restoration capabilities to support the data integrity architecture.

* Table 15 — Virtual infrastructure capability and the associated AWS services *

|  Capability and CSF mapping  |  AWS service  |  AWS service description  |  Function  |  [AWS GovCloud (US)](https://aws.amazon.com/govcloud-us/) available?  |
| --- | --- | --- | --- | --- |
|  Virtual Infrastructure <br /> PR.DS-1, PR.IP-4, PR.PT-1  |  [Amazon EBS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)  |  Amazon EBS provides the ability to create snapshots (backups) of any EBS volume. A snapshot takes a copy of the EBS volume and places it in S3, where it is stored redundantly in multiple Availability Zones.  |  Provides backup and restoration capabilities for systems and immutable storage.  |  Yes  |
|   |  [AWS Backup](https://aws.amazon.com/backup/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)  |  AWS Backup enables you to centralize and automate data protection across AWS services. AWS Backup offers a cost-effective, fully managed, policy-based service that further simplifies data protection at scale.  |  Provides backup and restoration capabilities for systems; performs periodic backups of information; provides immutable storage.  |  Yes  |
