---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/electronic-healthcare-record-and-revenue-cycle-systems.html
---

# Electronic healthcare record and revenue cycle systems
<a name="electronic-healthcare-record-and-revenue-cycle-systems"></a>

 Healthcare providers, payers, and SaaS ISVs operate transactional systems of record, such as electronic healthcare record and claims adjudication systems, that are critical to the parent organization’s operation.

 Characteristics of these solutions include:
+  High-scale transactional databases that host patient, care delivery, and payment records. These databases vary by ISV and application, but commonly support high levels of concurrent transactions and employ complex data schemas.
+  Workflow specific user interfaces, often catering to highly skilled end users. Healthcare customers may also customize commercial solutions to meet their specific needs.
+  Embedded analytics and AI/ML algorithms that support end user workflows.
+  Stringent availability and resilience requirements, as these systems are often critical to the operation of the parent organization.
+  Integration with third party applications that make up the electronic medical record.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
