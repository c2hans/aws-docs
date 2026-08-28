---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/troubleshooting-billed-twice.html
---

# I was billed twice for the same hosted zone
<a name="troubleshooting-billed-twice"></a>

We don't bill you if you delete a hosted zone within 12 hours after you create it. After 12 hours, we immediately charge the standard monthly fee for a hosted zone. The monthly charge for a hosted zone is not prorated for partial months. (The same charge applies for the hosted zone that we automatically create when you register a domain.)

If you create a hosted zone on the last day of the month (for example, January 31), the charge for January might appear on the February invoice, along with the charge for February. Note that Amazon Route 53 uses Coordinated Universal Time (UTC) as the time zone to determine when a hosted zone was created.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
