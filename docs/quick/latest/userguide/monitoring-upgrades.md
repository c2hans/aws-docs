---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/monitoring-upgrades.html
---

# Monitoring upgrades
<a name="monitoring-upgrades"></a>

|  |
| --- |
|  Applies to:  Enterprise Edition  |

|  |
| --- |
|    Intended audience:  System administrators and Amazon Quick administrators  |

Administrators can monitor user upgrades through:
+ **CloudTrail logs** — Provides audit trails of all upgrade requests and approvals.

## Billing considerations for administrators
<a name="billing-considerations"></a>
+ Users are billed for their highest license tier within each billing period.
+ **Prorated Billing:** When you upgrade a user subscription in Amazon QuickSuite, billing is prorated for the month of the upgrade. This means:

  If you upgrade from BI Reader ($3/month) to Professional ($20/month), you're billed at the $20/month rate from the time of upgrade until the end of that billing month.

  If you then upgrade again from Professional ($20/month) to Enterprise ($40/month) within the same month, you're billed at the $40/month rate from that second upgrade time until the end of the month.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
