---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/no-aws-operator-access.html
---

# No AWS operator access
<a name="no-aws-operator-access"></a>

 By design the Nitro System has no operator access. There is no mechanism for any system or person to log in to EC2 Nitro hosts, access the memory of EC2 instances, or access any customer data stored on local encrypted instance storage or remote encrypted EBS volumes. If any AWS operator, including those with the highest privileges, needs to do maintenance work on an EC2 server, they can only use a limited set of authenticated, authorized, logged, and audited administrative APIs. None of these APIs provide an operator the ability to access customer data on the EC2 server. Because these are designed and tested technical restrictions built into the Nitro System itself, no AWS operator can bypass these controls and protections.

 As with most engineering decisions, the choice to design the Nitro System without a mechanism for operator access came with trade-offs. In rare cases subtle issues can arise that, because there are no general access capabilities on our production hardware, AWS operators are unable to debug in-place. In those rare circumstances we must work with customers, at their request, to reproduce those subtle issues on dedicated non-production Nitro debugging hardware. This can be less convenient than if our operators could debug in-place, but we strongly believe that this is the better trade-off for our customers. As a result, we must by necessity hold ourselves to the highest standard for system quality and testing prior to production release.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
