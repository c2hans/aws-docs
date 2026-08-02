---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/introduction.html
---

# SAP on AWS migration methodology
<a name="introduction"></a>

*Sergej Trisic, Samuel CHNIBER, and Kaustubh Kulkarni, Amazon Web Services*

Enterprises have been migrating and running SAP on Amazon Web Services (AWS) since 2008. The SAP Professional Services team at AWS has been working with customers and AWS Partners, and has integrated their feedback into an SAP migration methodology, in order to improve the experience of users who want to migrate their SAP workloads to the AWS Cloud. AWS customers require a proven, tested way to move their SAP workloads to AWS that will be secure, fast, and cost-effective, with minimum risk and business disruptions. This document outlines the main elements of the SAP on AWS migration methodology we follow at AWS Professional Services to assist customers in preparing, planning, and implementing their migrations.

The document applies to SAP solutions that are based on SAP Business Suite, SAP S/4HANA, SAP Business Warehouse (BW), and SAP NetWeaver (ABAP). Other SAP products (such as Hybris or BusinessObjects) might share the same or similar approach depending on the specific characteristics of their technology stack. The migration process for those SAP products might use different sets of tools and more tailored migration strategies.

Among the migration strategies explained in the blog post [6 Strategies for Migrating Applications to the Cloud](https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/), this document focuses on best practices for implementing a rehosting (lift and shift) migration strategy. This approach consists of migrating your SAP environment to the cloud without applying any changes in terms of application architecture, code, or general modernization. You can use specific tools to perform a fast, efficient, and cost-effective migration.  After you move your SAP workloads to the cloud, you can modernize the application architecture, and modernize and re-architect the code. Those post-migration steps are beyond the scope of this document.

## Intended audience
<a name="overview"></a>

This document is designed to introduce senior SAP stakeholders in an enterprise, such as chief information officers (CIOs), chief digital officers (CDOs), vice presidents (VPs), and directors of enterprise application teams, SAP/ERP Competence Centers, and IT infrastructure teams, to the AWS migration methodology for SAP workloads. The goal is to help them determine a strategy for moving their SAP workloads to AWS in order to achieve critical business objectives. As such, this document doesn't focus on technical details, although it can be used by technical consultants, solutions architects, and other staff for planning and communications. The document includes links to deeper technical content on SAP technologies and migration to AWS.
