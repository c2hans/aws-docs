---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-mesh/roles-responsibilities.html
---

# Roles and responsibilities
<a name="roles-responsibilities"></a>

This section highlights the common business and technical personas, that contribute to the data mesh–based data solution. The alignment of these personas with the teams might differ based on the size and structure of your organization and the technology used in the data mesh solution.

Use executive sponsorship to onboard these personas in their respective teams from early on. Ensure that the responsibilities of these personas have well-defined boundaries. In the following table, the focus of the personas is indicated in the first column in parentheses. If there are two entries in the parentheses, the secondary focus follows the primary.

|
|
| Role (focus) | Recommended team | Key responsibilities |
| --- |--- |--- |
| Data owner (business) | Domain team | + Act as the business contact for the data.<br />+ Be responsible for data quality and business metadata.<br />+ Be responsible for data-access management.<br />+ Be responsible for business decisions related to the data product. |
| Data steward (technical, business) | Self-service data platform team, domain teams, governance team | + Manage access to data products.<br />+ Ensure metadata meets organizational and security standards.<br />+ Ensure data is accurate, trustworthy and accessible.<br />+ Be responsible for educating, communicating, and promoting data throughout the organization. |
| Data architect (technical, business) | Self-service data platform team, domain teams | + Act as the primary contact for technical topics related to data.<br />+ Design scalable, resilient, and secure data architecture.<br />+ Collaborate with business to define data product configuration and governance.<br />+ Help discover and implement features in the data mesh–based data solution. |
| Use-case owner (business) | Domain team | + Act as the business contact for the use-case.<br />+ Define the scope of the use case, its business feasibility, and success metrics.<br />+ Establish the roadmap of the use case.<br />+ Ensure that the business value is delivered within the defined time frame.<br />+ Be responsible for business decisions and the application of those decisions related to the use-case team. |
| Data solution owner (business) | Self-service data platform team | + Act as the primary business contact for topics related to the self-service data platform team.<br />+ Collaborate with the stakeholders to establish data strategy, enable use cases, and define the roadmap of the data solution.<br />+ Be responsible for the resiliency and availability of the data solution.<br />+ Approve data glossaries and definitions. |
| Data engineer (technical, business) | Self-service data platform team, domain teams, assets team | + Implement additional solutions for data ingestion, data storage, data transformation, and data consumption.<br />+ Implement data features in the data mesh–based data solution.<br />+ Collaborate with the domain teams to implement reusable data assets. |
| Cloud architect or DevOps architect (technical, business) | Self-service data platform team, domain teams, assets team, cloud foundation team | + Translate business requirements into technical requirements.<br />+ Implement features related to infrastructure as code, automation, monitoring, and notification.<br />+ Ensure end-to-end delivery of features. |
| Engagement manager (business, technical) | Self-service data platform team, domain teams, assets team, cloud foundation team, governance team | + Manage the budget and resources for each team to reach that team's goal.<br />+ Monitor daily project activities.<br />+ Identify, diagnose, and fix business-critical issues to ensure service-level agreements (SLAs) are met with internal stakeholders.<br />+ Report project health to executive sponsorship. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
