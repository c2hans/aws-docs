---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_securely_operate_multi_accounts.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC01-BP01 Separate workloads using accounts
<a name="sec_securely_operate_multi_accounts"></a>

Start with security and infrastructure in mind to enable your organization to set common guardrails as your workloads grow. This approach provides boundaries and controls between workloads. Account-level separation is strongly recommended for isolating production environments from development and test environments, or providing a strong logical boundary between workloads that process data of different sensitivity levels, as defined by external compliance requirements (such as PCI-DSS or HIPAA), and workloads that don’t.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Use AWS Organizations: Use AWS Organizations to centrally enforce policy-based management for multiple AWS accounts.
  + [Getting started with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started.html)
  + [How to use service control policies to set permission guardrails across accounts in your AWS Organization ](https://aws.amazon.com/blogs/security/how-to-use-service-control-policies-to-set-permission-guardrails-across-accounts-in-your-aws-organization/)
+  Consider AWS Control Tower: AWS Control Tower provides an easy way to set up and govern a new, secure, multi-account AWS environment based on best practices.
  +  [AWS Control Tower](https://aws.amazon.com/controltower/)

## Resources
<a name="resources"></a>

 **Related documents:**
+ [IAM Best Practices ](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html?ref=wellarchitected)
+  [Security Bulletins](https://aws.amazon.com/security/security-bulletins)
+  [AWS Security Audit Guidelines](https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html?ref=wellarchitected)

 **Related videos:**
+ [Managing Multi-Account AWS Environments Using AWS Organizations](https://youtu.be/fxo67UeeN1A)
+ [Security Best Practices the Well-Architected Way ](https://youtu.be/u6BCVkXkPnM)
+ [Using AWS Control Tower to Govern Multi-Account AWS Environments ](https://youtu.be/2t-VkWt0rKk)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
