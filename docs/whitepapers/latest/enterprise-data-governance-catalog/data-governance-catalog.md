---
source_url: https://docs.aws.amazon.com/whitepapers/latest/enterprise-data-governance-catalog/data-governance-catalog.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data governance catalog
<a name="data-governance-catalog"></a>

 Realizing the benefits of managing data assets to get deep business and technical insights, organizations are looking for a framework to implement data governance.

 A data governance catalog revolves around metadata. Primarily metadata is categorized as *technical* and *business*.
+  **Technical metadata** is information such as author, date created, date last modified, source, and size of a dataset.
+  **Business metadata** further enriches technical metadata by adding additional details for data classification, structure, data taxonomy, retention period, and other details for a dataset.

 Data and business have become inseparable. Absence of data-driven decision-making limits an organization’s ability to use their data to its best potential. This results in business decisions being made around growth, investments, and other verticals based on assumptions and personal preferences rather than real data statistics. Business decisions such as how an organization ships goods, interacts with customers, or sends product offerings backed by data empower organizations to run business efficiently.

 A data-first approach is essential for a data governance catalog’s success. Data stewardship is an important step in aligning data and business processes together. *Data stewards* are product managers, data subject matter experts (SMEs), and business owners, along with data architects and analysts. They are responsible for interpreting collected metadata to derive deep business insights, and promoting a culture of data-driven business decision across the organization.

 A Data Catalog aligns people, processes, and technology, helping data users understand and transform data into a business asset. It delivers good visibility into datasets, allowing organizations to comply with global data privacy laws.

 A Data Catalog allows an organization to identify data owners and improve data quality, regulatory compliance, and data usage. It enables organizations to orchestrate workflows to incorporate changes to the metadata.

 Data ownership ensures that someone in the organization is responsible for the data origin, definition, business attributes, relationships, and dependencies. There are various owners for different business units, such as marketing, supply chain, and finance. Business unit collaboration improves business actions such as launching products on time and on budget, interactions with consumers, and making new sales and distribution channels easy to build. For example, with improved collaboration, a marketing business unit can consolidate the customer data in the organization and create new marketing campaigns effectively, targeting the right audience.

 The following diagram depicts how a data governance catalog can create a relationship between various business and non-business assets across an organization to drive business growth.

![Diagram showing business relationships between organization assets](https://docs.aws.amazon.com/whitepapers/latest/enterprise-data-governance-catalog/images/business-relationships-between-assets.png)

 The Data Catalog creates mature data governance processes and adds value to the organization across several dimensions, including data-driven business decisions. The Data Catalog provides measures and metrics around datasets to guide strategic business decisions that align with the organization’s objectives and initiatives.

 In organizations where a Data Catalog is not implemented, data is often left fragmented and siloed across numerous sources (such as legacy systems, data warehouses, flat files stored on individual desktops, and modern, cloud-based repositories). Business stakeholders, data analysts, and other users spend too much time trying to discover data due to a lack of easy access and fragmented data environments.

 A Data Catalog helps implement data classification, encryption, data masking, and access protection to manage an organization’s data securely. Data classification enables data stewards to set up guidelines around the storage and access of classified data, such as customers’ Social Security Numbers (SSNs). SSNs are classified as sensitive data, and handled accordingly by the data processing and consumption pipelines.

 The preceding diagram shows business relationships between organization assets, enabling business users to understand their data’s origins and where it travels over time, without having to understand the underlying technical complexity. It identifies business, data, security and technology assets relationships and is implemented and managed within the Data Catalog.

## Data Catalog benefits for business stakeholders
<a name="data-catalog-benefits-for-business-stakeholders"></a>

 According to International Data Corporation (IDC), organizations are [suffering from inefficiencies and ineffectiveness](https://www.zdnet.com/article/workers-waste-half-their-time-as-they-struggle-with-data/) as they turn to data as the lifeblood of their digital transformation, and the workforce is struggling.

 Business metadata, such as metadata on ontology which is a way of showing the properties of a subject area and how they are related, by defining a set of concepts and categories that represent the subject for rapidly growing and diverse data. A combination of business and technical metadata provides a unified view of data assets, and reduces the effort of searching for the correct data. A Data Catalog enables business units to discover and access data securely, using data classification and policy management. It helps organizations identify new opportunities for problem-solving, innovation, and revenue growth, using [business lineage](https://www.dataversity.net/what-is-data-lineage/) and reports which are generated on the data asset relationships by data stewards. Data Catalogs help customers make connections that weren’t possible before, and drive their business growth while making informed business decisions.

 With robust metadata as the foundation of the Data Catalog, the following diagram illustrates the core features and functions supported:
+  **Data classification** labels related datasets to business domains, subject areas, and data facets, helping data users understand their datasets better.
+  **Data policy management** outlines how data processing and management is carried out to ensure an organization’s data is accurate, accessible, consistent, and protected. The policy establishes who is responsible for information under various circumstances, and specifies what procedures should be used to manage it. It incorporates risk management to identify, assess, and control threats to an organization's capital and earnings. It also introduces data ethics principles to reduce potential business problems from the use of data. Data policy management includes data access management and data retention.
+  **Business lineage** highlights the transformation and aggregation of data needed by a business user. Without this capability, business units cannot identify impacted systems and business processes changes.
+  **Reporting** allows visualization and dashboarding capabilities around various data assets. This reporting capability provides metrics around data volume growth, data classifications, relationships, and more.

 These capabilities make it easier for stakeholders to get an absolute view of their business data, so they can take appropriate business actions.

![Diagram showing Data Catalog core features and supported functions](https://docs.aws.amazon.com/whitepapers/latest/enterprise-data-governance-catalog/images/core-features.png)

## Data Catalog benefits for technical stakeholders
<a name="data-catalog-benefits-for-technical-stakeholders"></a>

 According to [Eckerson Group](https://www.eckerson.com/), one of the leading data analytics consulting and research group, [data cataloging accelerates analysis](https://www.eckerson.com/articles/the-business-case-for-a-data-catalog#:~:text=The%20value%20and%20benefits%20of,spend%20finding%20and%20preparing%20data.) by minimizing the time and effort that analysts spend finding and preparing data. Anecdotally, 80% of self-service analysis without a Data Catalog is spent getting data ready for analysis. Using the Data Catalog cuts that percentage from 80 to 20.

 A well-managed Data Catalog helps technical teams get more business context on technical and operational aspects of data using a business glossary. It enables technical teams to perform data discovery and analysis efficiently, while building data pipelines for the swift launch of data-driven applications to drive business growth. It provides lineage around the data journey, from origin to consumption.

 A Data Catalog provides native and comprehensive data governance capabilities that ensure trust in the data, and proper and compliant use of data across the enterprise. Without the preceding capabilities, it is hard for technical stakeholders to access updated versions of data, and manage the data. This can impact the business user’s ability to do data impact analysis.

 Using [technical lineage](https://www.dataversity.net/what-is-data-lineage/), a Data Catalog enables a business units’ technical support team to analyze downstream system impacts swiftly. System impacts are caused by a change in a source system feed (a change in attribute type or length). Technical lineage depicts the state of data from origin to consumption. It is a time-consuming exercise to manually identify the business impact due to change in the application or data assets.

 A data dictionary and business glossary establish a standard business definition and arrange it consistently across the datasets. With robust metadata as the core of the Data Catalog, many other features and functions are available for an organization’s technical stakeholders, as seen in the following diagram.

![Diagram showing Data Catalog features and functions](https://docs.aws.amazon.com/whitepapers/latest/enterprise-data-governance-catalog/images/features-and-functions.png)

+  The **business glossary** establishes standard business definitions to enable a common understanding of data across the organization. A business glossary ensures organizations speak the same language by clearing up ambiguity in business terminology.
+  The **data dictionary** is a collection of the names, definitions, and attributes for data elements. The data dictionary defines conventions for the project and consistency throughout the dataset. Without a data dictionary, there’s a higher risk of losing crucial information in translation and transition of data. Using a data dictionary helps data users analyze the datasets with ease later on.
+  **Technical lineage** shows how data transforms and flows as it moves from system to system, providing additional understanding and trust in data. It empowers users to understand how data was acquired, and how it may have been transformed to establish dependence in the reporting results or insights generated.
+  **Granular security controls** are role-based, asset-level permissions and access controls for secure enterprise-wide deployment. With a Data Catalog in place, it’s easier to enable the preceding security controls. Any organization that efficiently secures its data builds confidence among internal and external customers, driving business growth.
