---
source_url: https://docs.aws.amazon.com/detective/latest/userguide/accounts-orgs-members.html
---

# Managing organization accounts as Detective member accounts
<a name="accounts-orgs-members"></a>

In the organization behavior graph, the Detective administrator account determines which organization accounts to enable as member accounts. By default, new organization accounts are not enabled as member accounts. Their status is **Not a member**. The Detective administrator account can configure Detective to automatically enable new organization accounts as member accounts in the organization behavior graph.

The Detective administrator can configure Detective to enable new organization accounts as member accounts automatically. When you choose to enable organization accounts automatically, then Detective begins to enable new accounts as member accounts as they are added to the organization. Detective does not enable existing organization accounts that are not yet enabled.

The Detective can enable organization accounts as member accounts manually, if you do not want to automatically enable new organization accounts. They can also manually enable disassociated organization accounts. The Detective administrator cannot enable an organization account as a member account if the organization behavior graph already has the maximum 1,200 enabled accounts. In this case, the organization account status remains **Not a member**.

The Detective administrator also can disassociate organization accounts from the organization behavior graph. To stop ingesting data from an organization account in the organization behavior graph, you can disassociate the account. Existing data for that account remains in the behavior graph.

**Topics**
+ [Enabling new organization accounts as Detective member accounts](accounts-orgs-members-autoenable.md)
+ [Enabling organization accounts as Detective member accounts](accounts-orgs-members-enable.md)
+ [Disassociating organization accounts as Detective member accounts](accounts-orgs-members-disassociate.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
