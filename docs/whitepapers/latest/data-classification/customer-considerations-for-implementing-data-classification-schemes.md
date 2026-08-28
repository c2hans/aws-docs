---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-classification/customer-considerations-for-implementing-data-classification-schemes.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Customer considerations for implementing data classification schemes
<a name="customer-considerations-for-implementing-data-classification-schemes"></a>

 In addition to implementing a data classification scheme, it is equally important to determine data handling roles. ISO, NIST, and other standards place the responsibility of data classification on data owners, as they are the best positioned to determine the value, use, sensitivity, and criticality of their own data.

 Risk management obligations vary depending on the role of the parties that handle the data. In other words, data owners (such as controllers who generate and control content like agencies and ministries) and non-data owners (such as processors that handle data in order to provision services) should be subject to requirements appropriate for the roles they play. In the context of public sector data classification, agencies or ministries work as the data owner and are responsible for classifying their data and determining the security accreditation that they expect their CSP to meet.

 It is important to note that organizations applying a blanket high classification level to all data (despite its true risk posture) do not reflect a risk-based, outcome-focused approach to security. Protecting data classified at higher levels requires a higher standard of care, which translates into the organization spending increased resources on securing, monitoring, measuring, remediating, and reporting risks. It is impractical to commit the significant resources required to securely manage higher impact data for data that does not meet the requisite thresholds.

 Also, the additional controls placed on data at the lower classification levels can negatively affect the availability, completeness or timeliness of that data to the general workforce, customers, and/or constituents. Where risks can be managed so that data is handled at a lower classification level, organizations will experience the most flexibility around how they use that data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
