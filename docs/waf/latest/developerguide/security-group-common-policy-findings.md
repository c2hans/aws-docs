---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/security-group-common-policy-findings.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Security group common policy Firewall Manager findings
<a name="security-group-common-policy-findings"></a>

This page explains Firewall Manager findings for security group common policies.

For information about security group common policies, see [Using security group policies in Firewall Manager to manage Amazon VPC security groups](security-group-policies.md).

**Resource has misconfigured security group.**
Firewall Manager has identified a resource that is missing the Firewall Manager managed security group associations that it should have, according to the Firewall Manager policy. You can enable Firewall Manager remediation on the policy, which creates the associations according to the policy settings.
+ Severity – 70
+ Status settings – PASSED/FAILED
+ Updates – Firewall Manager updates this finding.

**Firewall Manager replica security group is out of sync with primary security group.**
A Firewall Manager replica security group is out of sync with its primary security group, according to their common security group policy. You can enable Firewall Manager remediation on the policy, which syncs the replica security groups with the primary.
+ Severity – 80
+ Status settings – PASSED/FAILED
+ Updates – Firewall Manager updates this finding.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
