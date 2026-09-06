---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/cross-account-remediation.html
---

# Cross-account remediation
<a name="cross-account-remediation"></a>

Automated Security Response on AWS uses cross-account roles to work across primary and secondary accounts. These roles are deployed to member accounts during solution installation. Each remediation is assigned an individual role. The remediation process in the primary account is granted permission to assume the remediation role in the account that requires remediation. Remediation is performed by AWS Systems Manager runbooks running in the account that requires remediation.
