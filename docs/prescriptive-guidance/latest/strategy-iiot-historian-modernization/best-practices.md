---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-iiot-historian-modernization/best-practices.html
---

# Best practices
<a name="best-practices"></a>

Historians acquire real-time data from programmable logic controllers (PLCs), sensors, and other automation systems to store time-series data at high speed while maintaining data quality. Data from on-site historians can be consolidated to a modernized enterprise historian in the cloud. The following are some best practices for planning a modernized historian approach for your organization:

1. Start by building a case study explaining why a modernize approach is required. Consider business drivers and industry challenges, such as advanced analytics, costs of on-premises data centralization, and multi-site visibility.

1. Historians can be expensive. Create a return on investment (ROI) analysis to justify the investment. Explain how historian modernization, in the long term, can reduce costs and provide returns.

1. Identify two or three business use cases that quickly show the value of implementing a modern historian approach.

1. Provide a configurable approach for hot and cold time-series data. Based on the access patterns and personas, clearly document how end users would interact with the system.

1. Integrate the cloud-based historian with any existing data stores to help drive advanced use cases, such as preventive maintenance, anomaly detection, and digital twins.

1. Build high availability and disaster recovery (HA/DR) into the architecture.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
