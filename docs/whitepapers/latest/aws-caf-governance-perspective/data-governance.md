---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-governance-perspective/data-governance.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data governance
<a name="data-governance"></a>

 **Exercise authority and control over your data to meet stakeholder expectations. **

 Your digital transformation efforts depend on accurate, complete, timely, and relevant data. Data governance focuses on ensuring that data are treated as a strategic asset and on developing competences to put that strategic asset to effective use. An effective data governance capability will help you reduce data duplication and sprawl, improve data quality and decision-making, drive organizational efficiencies, and accelerate your business outcomes on your way to becoming a [data-driven organization](https://aws.amazon.com/executive-insights/content/how-do-you-become-a-data-driven-organization/).

## Start
<a name="start-5"></a>

 Define key data governance roles and responsibilities, such as data owners, stewards, and custodians. While taking segregation of duties into account, assign key roles to appropriate individuals in your organization. Data owners should be recognized at an organizational level that includes both technology and business representatives and data stewardship should be a responsibility of all data-facing business personnel. Ensure that individual goals are aligned with data governance objectives and that relevant KPIs are defined, measured, and reported.

 Specify standards, including data dictionaries, taxonomies, and business glossaries. Identify what data sets need to be mastered and model the relationships between master data entities. Ensure that data policies are defined, documented, and communicated within your organization. Define, document, and communicate data classification, purging, archiving, retention, encryption, and protection policies. Monitor and enforce compliance and acceptable use of data.

 Define a data access request process, ensure that it is approved by the security teams, data owners, and data stewards, and that it is adopted across your organization. Prioritize your [data quality](https://d1.awsstatic.com/executive-insights/en_US/ebook-becoming-data-driven.pdf) efforts in line with your strategic and operational data needs. Establish data quality standards: identify key quality attributes, business rules, metrics, and targets.

 Make sure that your data governance strategy is documented, aligned to your business goals, and effectively communicated across your organization. Define KPIs to measure the associated business value. Define your data organization structure, identify the required skills based on the data governance strategy, and obtained leadership sponsorship.

## Advance
<a name="advance-5"></a>

 Start enforcing common data standards and practices while updating them as needed. Define key components of your data governance operating model. For example, you may wish to establish data governance councils/committees to help enforce critical data governance principles.
+  Develop [data lifecycle](https://pages.awscloud.com/rs/112-TZM-766/images/Data_Lifecycle_and_Analytics_Reference_Guide.pdf) policies, and implement continuous compliance monitoring.
+  Define and start implementing role-based data access processes.
+  Define a process for identifying critical data products.
+  Store data quality metrics in a common repository and ensure that trending analysis is available and actioned by data quality stakeholders.
+  Make sure that each line of business has data quality tool and methodologies and that they are consistently used within each line of business.
+  Start capturing data lineage metadata and conducing data profiling and data cleansing.
+  Develop data quality identification and remediation processes and begin to remediate data issues upstream. Implement data quality dashboards for critical data products.
+  Start measuring the effectiveness/business impact of data quality assessment and analyze trends to demonstrate progress over time.
+  Start developing automated, repeatable processes to ensure that all data are adherent to the policies. Start implementing automations (preventative, detective, and corrective controls) to help identify and remediate data-related violations.
+  Develop and implement measurements to enhance data lifecycle process quality.

 One of the most important aspects of a modern data architecture is the ability to authorize, manage, and audit access to data. This can be challenging because managing security, access control, and audit trails across all of the data stores in your organization is complex and time-consuming. AWS gives you the governance capability to manage access to all your data across your data lake and purpose-built data stores from a single place. Develop uniform access control for enterprise-wide data sharing by using [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) to centrally define and manage security, governance, and auditing policies.

## Excel
<a name="excel-5"></a>
+  Ensure that all data management processes are documented and automated.
+  Define data quality thresholds and implement continuous quality evaluation of critical data products.
+  Promote common data quality tools, methodology, and a business rules engine across the organization while continuously evaluating their effectiveness and evolving them as needed.
+  Ensure that data quality issues are remediated at the source.
+  Implement data quality alerting within operational dashboards and integrate those into your metadata repository/data catalog.
+  Enable data consumers to access data quality metrics for each data asset.
+  Enable product teams to define data quality rules and implemented them within data pipelines.
