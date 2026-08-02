---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-governance-perspective/data-curation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data curation
<a name="data-curation"></a>

** Collect, organize, access, and enrich metadata and use it to organize an inventory of data products in a data catalog. **

 A data catalog is an organized inventory of technical and business metadata. Technical metadata deals with structural aspects of data products, describing how data elements are organized within rows, columns, tables, and the like. It tells data professionals if they can work with data as is or if they need to transform them for analysis or integration.

 The [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html) is your persistent technical metadata store in the AWS Cloud. use the Data Catalog together with [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) (IAM) policies and AWS Lake Formation to control access to the tables and databases. By doing this, you can allow different teams to safely publish data to the wider organization while protecting sensitive data in a highly granular fashion. The Data Catalog, along with CloudTrail and Lake Formation, also provides you with comprehensive audit and governance capabilities, with schema change tracking and data access controls. This helps ensure that data is not inappropriately modified or inadvertently shared.

 Business metadata deals with the business value and fitness for use of data products. It facilitates communication and data exchange between technical and business stakeholders. When organized within a taxonomy and made available through search tools, catalogs help data consumers to find the data that they need.

 Data curation is the process of organizing and integrating relevant metadata into the data catalogue. The catalog enables organizations to facilitate data monetization, regulatory compliance, and self-service analytics by helping data consumers quickly locate relevant data assets as well as understand their context, such as data source, business/technical definitions, and quality.

## Start
<a name="start-6"></a>

 Effective data curation starts with the definition of several prerequisites, including data domains, a data taxonomy, and connectors that will be used to ingest the metadata.
+  **Data domains** — Define the primary data domains (such as customer, product, policy, or patient) that you will use to organize your data assets. These domains serve to support the structure of your data catalog and may be used to organize the construction of your data governance organization.
+  **Data taxonomy** — Organize relevant business terminology into a hierarchy. Define each term and establish relationships between associated terms. Doing so will help you help you effectively tag each data asset, enabling data consumers to more easily find what they need.
+  **Metadata connectors** — Being able to use connectors to automatically ingest data from a wide range of systems and tools, including databases, extract, transform, and load (ETL) tools, and reporting systems is another key concern when implementing a data catalog. Many data catalogs have a robust set of connectors, but it would be wise to understand the breadth of your toolset that is supported when beginning your efforts. It is important to consider how you will ingest business glossaries as these are frequently maintained in spreadsheets or web pages. If business definitions have not yet been documented, you should review your tool of choice for the best way to ingest relevant business metadata. It could very well be that your catalogue tool has the ability to support the entry, review, and approval of those definitions.

## Advance
<a name="advance-6"></a>

 As the information contained in the catalog expands, the catalog’s role will often expand as well. Increasingly, catalogs are enabling curation features such a commenting on data sets, ratings by analysts using the data, and ingestion/serving for corporate policies and procedures.

 At this point, one of the key value propositions of a data catalog begins: supporting regulatory compliance efforts. The data stores that were previously ingested can now be reviewed and tagged as to which compliance framework they fall under. Typically, this is a joint effort between the regulatory compliance team and the application teams that understand the data in the original stores that were ingested into the catalog.

 Many of the more advanced catalog tools have begun to use artificial intelligence to automatically suggest compliance tagging when the data is ingested. For example, data in the format NNN-NN-NNNN may be identified as a Social Security Number and tagged as needing to be address as PII.

 The user experience of navigating the catalog is also important to consider as the use expands. For example, it is anticipated that data analyst may use the catalog to understand all the reports that have already been created and how they are being used. Similarly, ETL developers may use the repository as a tool when undertaking data sourcing/data lineage investigations. These and other user experience scenarios should be explored in order to realize the maximum value from your organization’s investments.

## Excel
<a name="excel-6"></a>

 As the collection of data in the catalog becomes more valuable, it will become increasingly important that the business-focused data governance team be involved the maintenance of the catalog platform. In turn, a data catalog can often support that data governance organization by serving as the platform to manage relevant data governance policies, data procedures, and associated standards.

 Consider incorporating additional types of metadata; for example, data science algorithms may be defined and viewable in the data catalog. There is a myriad of different ways in which the data catalog and the curation efforts can benefit your organization; we have touched on just a few here. The more consistent and well understood an organizations data is, the more time and energy collectively it has to focus on driving value.
