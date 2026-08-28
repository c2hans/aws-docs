---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/important-considerations.html
---

# Important Considerations
<a name="important-considerations"></a>

**Accounts directly under the root**: When selecting specific OUs for your membership, accounts that are directly under the organization root (not part of any OU) will not be associated with your membership. To include these accounts in your membership coverage, you must first add them to an OU, then associate that OU with your membership.

**Note**
AWS Security Incident Response is continuously improving the OU association user experience to make the process more intuitive and self-explanatory.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
