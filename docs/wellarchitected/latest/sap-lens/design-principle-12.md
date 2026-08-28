---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/design-principle-12.html
---

# 12 – Plan for data recovery
<a name="design-principle-12"></a>

 **How do you plan for logical, data-related recovery for your SAP workload?** Work backwards from the business requirements to define an approach to recover or reconstruct your business data. Depending on how you have architected for resilience, different scenarios might fit in this category. At a minimum, your backup or disaster recovery (DR) posture should protect you from accidental deletion, logical data corruption, and malware. Be deliberate about the decision to restore, taking into account the time to return to service and the dependencies between systems.

| ID | Priority | Best Practice |
| --- | --- | --- |
| ☐ BP 12.1 | Required | Establish a method for consistent recovery of business data |
| ☐ BP 12.2 | Highly Recommended | Establish a method for recovering configuration data |
| ☐ BP 12.3 | Highly Recommended | Define a recovery approach for your complete SAP estate |
| ☐ BP 12.4 | Recommended | Conduct periodic tests to validate your recovery procedure |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
