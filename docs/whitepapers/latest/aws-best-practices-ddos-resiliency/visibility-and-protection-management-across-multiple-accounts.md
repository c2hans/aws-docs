---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/visibility-and-protection-management-across-multiple-accounts.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Visibility and protection management across multiple accounts
<a name="visibility-and-protection-management-across-multiple-accounts"></a>

 In scenarios when you operate across multiple AWS accounts and have multiple components to protect, using techniques that enable you to operate at scale and reduce operational overhead increase your mitigation capabilities. When managing AWS Shield Advanced protected resources in multiple accounts, you can set up centralized monitoring by using AWS Firewall Manager and AWS Security Hub CSPM. With Firewall Manager, you can create a security policy that enforces DDoS protection compliance across all your accounts. You can use these two services together to manage your protected resources across multiple accounts and centralize the monitoring of those resources.

 Security Hub CSPM automatically integrates with Firewall Manager, allowing Shield Advanced customers to view security findings in a single dashboard, alongside other high priority security alerts and compliance statuses.

 For example, when Shield Advanced detects anomalous traffic destined for a protected resource in any AWS account within the scope, this finding will be visible in the Security Hub CSPM console. If configured, Firewall Manager can automatically bring the resource into compliance by creating it as a Shield Advanced–protected resource, and then update Security Hub CSPM when the resource is in a compliant state.

![Architecture diagram showing monitoring AWS Shield-protected resources with Firewall Manager and Security Hub CSPM](http://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/images/shield-protected-resources-ref-arch.jpg)

 For more information about central monitoring of Shield protected resources, refer to [Set up centralized monitoring for DDoS events and auto-remediate noncompliant resources](https://aws.amazon.com/blogs/security/set-up-centralized-monitoring-for-ddos-events-and-auto-remediate-noncompliant-resources).
