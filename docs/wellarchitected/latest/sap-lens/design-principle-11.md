---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/design-principle-11.html
---

# 11 – Detect and react to failures
<a name="design-principle-11"></a>

 **How do you detect and react to failures impacting your SAP workload?** Design how software or operating procedures can help ensure the health and resilience of your SAP workload. Monitor for potential and actual failures, focusing on prevention where possible. Consider whether a component is distributed or is a single point of failure and design a resiliency solution that minimizes the impact to your workload. In addition to testing periodically to understand your risk profile, examine how automation could improve your resilience.

| ID | Priority | Best Practice |
| --- | --- | --- |
| ☐ BP 11.1 | Required | Monitor failures of SAP applications, AWS resources, and connectivity |
| ☐ BP 11.2 | Highly Recommended | Define an approach to maintain availability |
| ☐ BP 11.3 | Highly Recommended | Define an approach to restore service availability |
| ☐ BP 11.4 | Highly Recommended | Conduct periodic tests of resilience |
| ☐ BP 11.5 | Recommended | Automate reaction to failures |

 For more details, refer to the following:
+  AWS Documentation: [Architecture Guidance for Availability and Reliability of SAP on AWS including Failure Scenarios and Architecture Patterns ](https://docs.aws.amazon.com/sap/latest/general/architecture-guidance-of-sap-on-aws.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
