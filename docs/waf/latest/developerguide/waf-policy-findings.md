---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-policy-findings.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# AWS WAF policy Firewall Manager findings
<a name="waf-policy-findings"></a>

This page explains Firewall Manager findings for AWS WAF policies.

You can use Firewall Manager AWS WAF policies to apply AWS WAF rule groups to your resources in AWS Organizations. For more information, see [Using AWS Firewall Manager policies](working-with-policies.md).

**Resource is missing Firewall Manager managed web ACL.**
An AWS resource doesn't have the AWS Firewall Manager managed web ACL association in accordance with the Firewall Manager policy. You can enable Firewall Manager remediation on the policy to correct this.
+ Severity – 80
+ Status settings – PASSED/FAILED
+ Updates – If Firewall Manager performs the remediation action, it will update the finding and the severity will lower from `HIGH` to `INFORMATIONAL`. If you perform the remediation, Firewall Manager will not update the finding.

**Firewall Manager managed web ACL has misconfigured rule groups.**
This is a AWS WAF Classic policy finding. The rule groups in a web ACL that's managed by Firewall Manager are not configured correctly, according to the Firewall Manager policy. This means that the web ACL is missing the rule groups that the policy requires. You can enable Firewall Manager remediation on the policy to correct this.
+ Severity – 80
+ Status settings – PASSED/FAILED
+ Updates – If Firewall Manager performs the remediation action, it will update the finding and the severity will lower from `HIGH` to `INFORMATIONAL`. If you perform the remediation, Firewall Manager will not update the finding.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
