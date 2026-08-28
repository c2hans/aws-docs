---
source_url: https://docs.aws.amazon.com/odb/latest/UserGuide/hpn-troubleshooting.html
---

# Troubleshooting
<a name="hpn-troubleshooting"></a>

## Handling Insufficient Capacity Errors (ICE)
<a name="handling-ice-errors"></a>

If you receive an **Insufficient Instance Capacity Error (ICE)** when launching Amazon EC2 instances with the Oracle Database@AWS placement group:
+ **Retry with a different instance type** – ICE errors are typically instance-type specific. Retrying with a compatible alternative instance type often resolves the issue.
+ **Use [On-Demand Capacity Reservations (ODCR)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-create.html)** – To minimize the risk of ICE occurrences, reserve capacity in advance using ODCR with your Oracle Database@AWS placement group.
+ **Use placement groups selectively** – Reserve placement group usage for workloads that truly require consistent sub-millisecond latency.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database at AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
