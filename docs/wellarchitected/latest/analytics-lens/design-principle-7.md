---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/design-principle-7.html
---

# 7 – Govern data and metadata changes
<a name="design-principle-7"></a>

 **How do you govern data and metadata changes?** Controlled changes are not only necessary for infrastructure, but also required for data quality assurance. If the data changes are uncontrolled, it becomes difficult to anticipate the impact of these changes. It also makes downstream systems harder to manage data quality issues of their own.

|  **ID**  |  **Priority**  |  **Best practice**  |
| --- | --- | --- |
| ☐ BP 7.1  |  Required  |  Build a central Data Catalog to store, share, and track metadata changes.  |
| ☐ BP 7.2  |  Required  |  Monitor for data quality anomalies.  |
| ☐ BP 7.3  |  Required  |  Trace data lineage.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
