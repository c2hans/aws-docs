---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/edge-computing-infrastructure-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Edge computing infrastructure management
<a name="edge-computing-infrastructure-management"></a>

A typical manufacturing facility has on-premises computing infrastructure to manage, such as industrial data centers, industrial PCs, and gateways. Managing this infrastructure can be a challenge due to disparate hardware/software, lack of centralized management interface, and no easy way to implement best practices. The responsibility of this infrastructure is shared between OT and IT domains. Customers can leverage the experience of AWS by following the best practices of IT infrastructure management, and by leveraging on-premises management and monitoring services such as [AWS Systems Manager](https://aws.amazon.com/systems-manager/) and [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/). These services help manage the on-premises infrastructure at scale, in a similar way as the cloud resources. This removes the barriers to implementing best practices on-premises.

For example, CloudWatch agents can be used to monitor health/usage metrics and logs from edge servers running manufacturing applications. Customers can configure alerts to get notified in case of failures or exceptions. AWS Systems Manager can be used for centralized device management. Customers can collect software inventories, operation system versions, and installed patches. They can automate tasks such as software installation and patch management. This also helps you to maintain your security and compliance requirements, by scanning the instances against specified patch, configuration, and custom policies.

[AWS Outposts](https://aws.amazon.com/outposts/), on the other hand, provides a fully managed service that extends utility computing to the edge. It is managed from the [AWS Management Console](https://aws.amazon.com/console/), SDK, and API, like any other cloud facility, and is deployed at the customer’s premises. It is designed to simplify the management and governance of on-premises infrastructure, and remove barriers to implementing best practices. It utilizes the power of cloud services to augment existing infrastructure, and blurs the boundary between on-premises and cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
