---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/shared-responsibility-model.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Shared responsibility model
<a name="shared-responsibility-model"></a>

 Security and compliance are shared responsibilities between AWS and the customer. Depending on the services deployed, this shared model can help relieve the customer’s operational burden. This is because AWS operates, manages, and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. The customer assumes responsibility and management of the guest operating system (including updates and security patches) and other associated application software, in addition to the configuration of the AWS-provided security group firewall.

 We recommend that customers carefully consider the services they choose because their responsibilities vary depending on the services used, the integration of those services into their IT environment, and applicable laws and regulations. It is possible for customers to enhance their security and/or meet their more stringent compliance requirements by leveraging technology such as host-based firewalls, host-based intrusion detection and prevention, encryption, and key management.

 The nature of this shared responsibility also provides the flexibility and customer control that permits customers to deploy solutions that meet industry-specific certification requirements.

![Chart showing the AWS customer and AWS shared responsibility](http://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/images/image2.png)

 This shared responsibility model also extends to IT controls. Just as the responsibility to operate the IT environment is shared between AWS and its customers, the management, operation, and verification of IT controls is also a shared responsibility. AWS can help customers by managing those controls associated with the physical infrastructure deployed in the AWS environment. Customers can then use the AWS control and compliance documentation available to them to perform their control evaluation and verification procedures as required. For examples of how responsibility for certain controls is shared between AWS and its customers, see the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
