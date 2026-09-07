---
source_url: https://docs.aws.amazon.com/whitepapers/latest/enterprise-data-governance-catalog/implementation-reference-architecture-diagrams.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Implementation reference architecture diagrams
<a name="implementation-reference-architecture-diagrams"></a>

 The following are two reference architecture diagrams to help with the design and build phases of implementing a Data Catalog.
+  [**Reference architecture diagram 1**](#diagram1design) illustrates how an organization can build a Data Catalog without the use of third-party data cataloging tools, instead collecting technical metadata and enriching it using business metadata with help from a team of data stewards.
+  [**Reference architecture diagram 2**](#diagram2design) illustrates how an organization can use third-party tools like [Collibra](https://www.collibra.com/us/en) to collect technical metadata, and enrich technical metadata using business metadata with help from a team of data stewards.

 A Data Catalog ensures that data is well managed, because data are the building blocks to establish a strong data culture. Data comes in many shapes, sizes, and formats, and each must be captured and depicted in its native format. A Data Catalog captures and depicts data by classifying the data. Implementation of a Data Catalog enables an organization to know datasets’ origins, and how data transforms as it flows across different applications, reducing data analysis time.

## Implementation reference architecture diagram 1
<a name="implementation-reference-architecture-diagram-1"></a>

 Reference architecture diagram 1 describes the high-level implementation of a Data Catalog using a custom build approach. This approach uses a relational database ([Amazon Aurora PostgreSQL](https://aws.amazon.com/rds/aurora/postgresql-features/)/ [MySQL](https://www.mysql.com/)), and [AWS Glue](https://aws.amazon.com/glue/) or other available data integration tools.

 Technical metadata, which is comprised of tables, attributes, definitions, and so on, are captured by the source and pulled on a scheduled basis from various heterogenous source data dictionaries.

 Business metadata, consisting of business context, is prepared and gathered by data stewards who are data architects, product managers, and data analysts. The technical and business metadata is combined together, and it provides a single version of truth for the collected metadata.

 Combined business and technical metadata provide details around the data taxonomy, data classification, reference data, business glossary, and security management.

 Data taxonomy is the classification of data based on data domains, subject areas, and data facets that introduce common terminologies and semantics across multiple systems. <a name="diagram1design"></a>

![Reference architecture diagram 1: Enterprise metadata and data governance management catalog](https://docs.aws.amazon.com/whitepapers/latest/enterprise-data-governance-catalog/images/enterprise-metadata-diagram1.png)

 Technical metadata is collected from various enterprise sources by a Database/Application Programming Interface (API). The API/JDBC connection periodically pulls data dictionary details from various relational/application data stores. This technical metadata is stored in a relational database modeled to meet the organizations data governance requirements.

 The metadata is enriched by additional business metadata related to the objects and attributes such as description, lineage info, security classifications, ownership, and so on. Data lineage is the process of understanding, recording, and visualizing data as it flows from data sources to consumption. It includes all transformations the data underwent along the way, and how the data was transformed and consumed.

 The data stewardship team is an essential part of the data governance process. Stewards update the data taxonomy. Data stewardship is the collection of practices that ensure an organization’s data is accessible, usable, safe, and trusted. It includes overseeing aspects of the data lifecycle: creating, preparing, using, storing, archiving, and deleting data. They help promote data quality and integrity that is in line with the data governance principles of an organization. They manage and maintain the Data Catalog using the graphical interface build on top of the relational database that stores the metadata.

## Implementation reference architecture diagram 2
<a name="implementation-reference-architecture-diagram-2"></a>

 Reference architecture diagram 2 describes the high-level implementation of Data Catalog using third-party tools like Collibra, relational databases (Aurora PostgreSQL/MySQL), and AWS Glue or other available data integration pipelines. [Collibra](https://www.collibra.com/us/en) software is an enterprise-oriented data governance platform for Data Catalog and stewardship. It empowers businesses to find meaning in their data and improve business decisions. Collibra’s partnership with AWS makes it possible to unlock the value of data, irrespective of where and how it is stored.

 Technical metadata, which is comprised of tables, attributes, definitions, and so on, is captured by the source and pulled on a scheduled basis from various heterogenous sources using Collibra. Collibra centralizes, governs, and certifies reports and metrics on collected metadata. Technical metadata is enriched with business metadata related to the objects and attributes.

 Third-party tools provide an out-of-the-box graphical user interface for data stewards and users to view and update business metadata. Most third-party tools also provide machine learning capabilities to find similar matching patterns of data and help them inherit definitions and classifications. As depicted in the [reference architecture diagram 1](#diagram1design), technical and business metadata is combined to provide users with a meaningful context for various data assets within the organization. <a name="diagram2design"></a>

![Reference architecture diagram 2: Enterprise metadata and data governance management catalog](https://docs.aws.amazon.com/whitepapers/latest/enterprise-data-governance-catalog/images/enterprise-metadata-diagram2.png)

 Technical metadata is collected from various enterprise sources by a Database/Application Programming Interface (API). The API/JDBC connection periodically pulls data dictionary details from various relational/application data stores.

 Technical metadata is enriched by extended metadata related to the objects and attributes. The third-party data cataloging tool’s graphical user interface is used to view and update the collected metadata. Third-party tools like Collibra also provide out-of-the-box reports around the collected and enriched metadata.
