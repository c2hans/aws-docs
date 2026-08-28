---
source_url: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/workload-lifecycle.html
---

# Workload lifecycle
<a name="workload-lifecycle"></a>

**Review accuracy of supporting operational data.** Make sure that there are periodic reviews of the tags associated with your workload lifecycle, and that the appropriate stakeholders are involved in these reviews.

 *Table 7 – Review operational tags as part of the workload lifecycle*

|  Use Case  |  Tag Key  |  Rationale  |  Example Values  |
| --- | --- | --- | --- |
|  Account Owner  | example-inc:account-owner:owner  |  The owner of the account and it's contained resources.  | ops-center, dev-ops, app-team  |
|  Account Owner Review  | example-inc:account-owner:review  |  Review of account ownership details being up to date and correct.  | <review date in the correct format defined in your tagging library>  |
|  Data Owner  | example-inc:data-owner:owner  |  The data owner of the accounts residing data.  | bi-team, logistics, security  |
|  Data Owner Review  | example-inc:data-owner:review  |  Review of data ownership details being up to date and correct.  | <review date in the correct format defined in your tagging library>  |

## Assigning tags to suspending accounts before migrating to the suspended OU
<a name="assigning-tags-to-suspending-accounts"></a>

 Before suspending an account and moving into the suspended OU as detailed in the [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) whitepaper, tags should be added to the account to aid in your internal tracing and auditing of an account’s lifecycle. For example, a relative URL or ticket reference on an organization’s ITSM ticketing system, that shows the audit trail for an application being suspended.

 *Table 8 - Add operational tags when workload lifecycle enters new stage*

|  Use Case  |  Tag Key  |  Rationale  |  Example Values  |
| --- | --- | --- | --- |
|  Account Owner  | example-inc:account-owner:owner  |  The owner of the account and it's contained resources.  | ops-center, dev-ops, app-team  |
|  Data Owner  | example-inc:data-owner:owner  |  The data owner of the accounts residing data.  | bi-team, logistics, security  |
|  Suspended Date  | example-inc:suspension:date  |  The date that the account was suspended  |  <suspended date in the correct format defined in your tagging library>  |
|  Approval for suspension  | example-inc:suspension:approval  |  The link to the approval of account suspension  | workload/deprecation  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
