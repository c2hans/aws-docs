---
source_url: https://docs.aws.amazon.com/detective/latest/userguide/investigations-summary.html
---

# Detective Investigations report summary
<a name="investigations-summary"></a>

Investigations summary highlights anomalous indicators that require attention, for the selected scope time. Using the summary, you can more quickly identify the root cause of potential security issues, identify patterns, and understand the resources impacted by security events.

In the detailed investigations report summary, you can view the following details.

**Investigations overview**

In the **Overview** panel, you can see a visualization of IPs with high severity activity, which can give more context on the pathway of an attacker.

Detective highlights **Unusual activity** in the investigation, for example impossible travel from a source to a faraway destination by the IAM user.

Detective maps the investigations to tactics, techniques, and procedures (TTPs) used in a potential security event. The MITRE ATT&CK framework is used to understand the TTPs. Tactics are based on the [MITRE ATT&CK matrix for Enterprise](https://attack.mitre.org/matrices/enterprise/).

**Investigations indicators**

You can use the information in the **Indicators** pane, to determine if an AWS resource is involved in unusual activity that could indicate malicious behavior and its impact. An indicator of compromise (IOC) is an artifact observed in or on a network, system, or environment that can (with a high level of confidence) identify malicious activity or a security incident.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
