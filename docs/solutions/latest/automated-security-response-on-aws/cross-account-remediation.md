---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/cross-account-remediation.html
---

# Cross-account remediation
<a name="cross-account-remediation"></a>

Automated Security Response on AWS uses cross-account roles to work across primary and secondary accounts. These roles are deployed to member accounts during solution installation. Each remediation is assigned an individual role. The remediation process in the primary account is granted permission to assume the remediation role in the account that requires remediation. Remediation is performed by AWS Systems Manager runbooks running in the account that requires remediation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
