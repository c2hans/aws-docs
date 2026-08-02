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
| Data owner (business) | Domain team | Act as the business contact for the data.Be responsible for data quality and business metadata.Be responsible for data-access management.Be responsible for business decisions related to the data product. |
| Data steward (technical, business) | Self-service data platform team, domain teams, governance team | Manage access to data products.Ensure metadata meets organizational and security standards.Ensure data is accurate, trustworthy and accessible.Be responsible for educating, communicating, and promoting data throughout the organization. |
| Data architect (technical, business) | Self-service data platform team, domain teams | Act as the primary contact for technical topics related to data.Design scalable, resilient, and secure data architecture.Collaborate with business to define data product configuration and governance.Help discover and implement features in the data mesh–based data solution. |
| Use-case owner (business) | Domain team | Act as the business contact for the use-case.Define the scope of the use case, its business feasibility, and success metrics.Establish the roadmap of the use case.Ensure that the business value is delivered within the defined time frame.Be responsible for business decisions and the application of those decisions related to the use-case team. |
| Data solution owner (business) | Self-service data platform team | Act as the primary business contact for topics related to the self-service data platform team.Collaborate with the stakeholders to establish data strategy, enable use cases, and define the roadmap of the data solution.Be responsible for the resiliency and availability of the data solution.Approve data glossaries and definitions. |
| Data engineer (technical, business) | Self-service data platform team, domain teams, assets team | Implement additional solutions for data ingestion, data storage, data transformation, and data consumption.Implement data features in the data mesh–based data solution.Collaborate with the domain teams to implement reusable data assets. |
| Cloud architect or DevOps architect (technical, business) | Self-service data platform team, domain teams, assets team, cloud foundation team | Translate business requirements into technical requirements.Implement features related to infrastructure as code, automation, monitoring, and notification.Ensure end-to-end delivery of features. |
| Engagement manager (business, technical) | Self-service data platform team, domain teams, assets team, cloud foundation team, governance team | Manage the budget and resources for each team to reach that team's goal.Monitor daily project activities.Identify, diagnose, and fix business-critical issues to ensure service-level agreements (SLAs) are met with internal stakeholders.Report project health to executive sponsorship. |
