---
source_url: https://docs.aws.amazon.com/whitepapers/latest/enterprise-data-governance-catalog/enterprise-data-governance-catalog.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Enterprise Data Governance Catalog
<a name="enterprise-data-governance-catalog"></a>

Publication date: **December 3, 2021** ([Document history](document-revisions.md))

 This whitepaper outlines the benefits and strategies for implementing an enterprise-wide unified Data Governance Platform to enable business users and stakeholder with the ability to find, manage, understand, access, and trust their data to make better data-driven business decisions.

 This whitepaper is for technical and business leaders who are responsible for managing data and analytics platform.

## Introduction
<a name="introduction"></a>

 Business and data users want the capability to analyze the data scattered across various data assets within their organizations. Data assets are stored across various databases, file systems, servers located on-premises and in the cloud (including data warehouses), data lakes, and big data.

 However, many data assets are hidden deep inside data silos without much clarity into the datasets, the classifications associated within the datasets, and their business relationships. Vast amounts of data are created, captured, and consumed by organizations, which further increase the complexities of finding and understanding data assets. Identifying relevant datasets, profiling, and combines the related data to get meaningful technical and business insights is tedious.

 Organizations face numerous challenges to analyze data spread across various data assets within their organization to get business insights and drive business decisions related to growth, adoption, and investments. This is a challenge due to the lack of a data-first paradigm, where data is the driver to make key business growth decisions within the organization. There is a lack of understanding the business value of data as a product, and technical design gaps are introduced while managing data.

 Data Catalogs have evolved from a promising to essential framework which supports organizations data and analytics. In 2017, [Gartner declared Data Catalogs as “the new black in data management and analytics](https://www.datalumen.eu/solutions/data-governance/data-catalogs-must-have-for-data-analytics-leaders/)”, and now they are recognized as a central technology for data management. According to International Data Corporation (IDC), four out of five (80%) of the organizations take advantage of data across multiple organizational processes. However, despite increases in innovation, some studies show that [workers waste 44% of their time each week](https://www.zdnet.com/article/workers-waste-half-their-time-as-they-struggle-with-data/) struggling with data due to a lack of collaboration, knowledge gaps, and organizational resistance to change.

 This whitepaper outlines key considerations to build a Data Catalog, and provides an approach to implement data governance through a Data Catalog using Amazon Web Services (AWS) Cloud technologies. It showcases how a robust Data Catalog empowers data users to explore hidden data insights effectively, while driving their organizations’ growth by making data-driven business decisions.

 This whitepaper also provides a high-level approach to managing metadata (the data providing information about one or more aspects of the data). Metadata can be used to classify, organize, and access data assets to provide deep technical and business insights. Business insights are essential for organizations to make better business decisions, achieve operational efficiency, and improve data understanding and data quality.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
