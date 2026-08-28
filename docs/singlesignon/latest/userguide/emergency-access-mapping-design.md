---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access-mapping-design.html
---

# How to design emergency role, account, and group mapping
<a name="emergency-access-mapping-design"></a>

The following diagram shows how to map your emergency access groups to roles in your emergency access account. The diagram also shows the cross-account role trust relationships that enable emergency access account roles to access corresponding roles in your workload accounts. We recommend that your emergency plan design use these mappings as a starting point.

![IAM Identity Center workflow: map emergency access groups to roles in emergency account.](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/emergency-access-mapping.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
