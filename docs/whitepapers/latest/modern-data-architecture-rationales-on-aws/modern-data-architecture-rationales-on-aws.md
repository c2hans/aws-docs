---
source_url: https://docs.aws.amazon.com/whitepapers/latest/modern-data-architecture-rationales-on-aws/modern-data-architecture-rationales-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Abstract and introduction
<a name="modern-data-architecture-rationales-on-aws"></a>

Publication date: **February 15, 2022** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

Today, with the rapid growth in data from ever-expanding data producer platforms, organizations are looking for ways to modernize their data analytics platforms. This whitepaper lays out the traditional analytics approaches and their challenges. It then explains why a modern data architecture is required, and how it helps solve the challenges presented by traditional analytics.

This paper also provides context around how Amazon Web Service (AWS) Cloud analytics services provide a foundation for building this modern data architecture platform.

## Introduction
<a name="introduction"></a>

 Many large organizations use [enterprise data warehouses](https://en.wikipedia.org/wiki/Data_warehouse) (EDW) as the single version of truth, and a semantic layer for all the data in the organization. EDW acts as a harmonization layer for data originating from multiple sources into an integrated data model.

 In contrast, a [data lake](https://en.wikipedia.org/wiki/Data_lake) is a storage repository that holds a vast amount of raw data in its native format until it is needed for analytics applications. While a traditional data warehouse stores data in hierarchical dimensions and tables, a data lake uses a flat architecture to store data, primarily in files or object storage.

 EDW became popular in the last two decades because of the popularity of using business intelligence (BI) for strategic decision making, as well as for daily operational activities across the organization.

 The two most popular approaches to realize a data warehouse over the years have been:
+  **Kimball approach** – proposed by Ralph Kimball
+  **Inmon approach** – proposed by Bill Inmon

### Enterprise data warehouse
<a name="enterprise-data-warehouse"></a>

#### Kimball approach
<a name="kimball-approach"></a>

 Ralph Kimball’s view is that data warehouse design is a [bottom-up](https://en.wikipedia.org/wiki/Top-down_and_bottom-up_design) process, and the data warehouse is formed by several smaller [data marts](https://en.wikipedia.org/wiki/Data_mart) ([star schemas](https://en.wikipedia.org/wiki/Star_schema)) based on various business contexts with some key dimensions which are common across multiple business contexts.

 This approach suggests gradual building of the data warehouse by adding new data marts. Data marts are added by adding new [fact tables](https://en.wikipedia.org/wiki/Fact_table) to represent transactional and event data, and by adding new dimensions or attributes to existing conformed dimensions.

![A diagram depicting the bottom-up EDW approach.](http://docs.aws.amazon.com/whitepapers/latest/modern-data-architecture-rationales-on-aws/images/modern-data-arch-1.png)

 The various combination of dimensions and facts form a logical data mart for a specific business use case.

##### Benefits:
<a name="benefits"></a>
+  EDW is purpose-built with logical grouping of data marts; EDW is gradually realized based on business use cases and all the data gets stored in EDW.
+  Data is highly [denormalized](https://en.wikipedia.org/wiki/Denormalization) and redundant, which makes it optimal for analytical purposes with generally better performance. In some cases, a performance layer is also created in terms of physical data marts to achieve optimal performance for use cases such as aggregated reports, trend reports, and time frame reports.
+  EDW is easier to understand for non-IT users, because logical data marts are purpose-built subject areas for a particular business domain. It’s easy to create and understand a business metadata layer.
+  EDW is highly suitable for massively parallel processing Relational Database Management Systems (RDBMS), and also suitable for data lake implementations.

##### Shortcomings:
<a name="shortcomings"></a>
+  Because EDW is use case driven, creating a fully harmonized integration layer might be difficult to achieve. Data duplication and data sync issues also make this task challenging.
+  Tight coupling with consumers causes delay in changes to mitigate the impact on consumers.
+  The data volume of the tables is high, and this results in heavy and long running extract, transform, and load (ETL) jobs. Additional jobs may be required to get a physical performant layer.

#### Inmon approach
<a name="inmon-approach"></a>

 Bill Inmon proposed a [top-down](https://en.wikipedia.org/wiki/Top-down_and_bottom-up_design) approach to create a normalized integrated data model where all the data must first be harmonized and translated to a unified data model as per the organization’s context.

 According to this approach, data from all the source systems is unified, formatted, type casted, and semantically translated (mapped to the same vocabulary up front). To achieve this, organizations must put in significant amounts of time and effort to define a unified data model to align all the data elements from the source systems.

![A diagram depicting the top-down EDW approach.](http://docs.aws.amazon.com/whitepapers/latest/modern-data-architecture-rationales-on-aws/images/modern-data-arch-2.png)

##### Benefits:
<a name="benefits-1"></a>
+  Highly normalized and no/low data redundancy.
+  Data relationships and granularity is clear with proper semantics.
+  Decoupled from consumers, so it can evolve independently.
+  Optimized for storage and historical data.
+  More suitable for RDBS implementations.

##### Shortcomings:
<a name="shortcomings-1"></a>
+  Data model is complex and data preparation effort is large.
+  Integrated model leads to higher dependency in data sources and reduces parallelism.
+  [Third normal form](https://en.wikipedia.org/wiki/Third_normal_form) (3NF) leads to a lot of joins for analysis, making it compute-heavy for doing ad-hoc analysis.
+  Most of the time, source data needs to be broken down for the EDW model, and businesses may need to join multiple tables together to derive a final combined dataset across multiple sources.
+  Usually a presentation layer (consisting of multiple data marts) is created on top, which is de-normalized in a [star](https://en.wikipedia.org/wiki/Star_schema) or [snowflake](https://en.wikipedia.org/wiki/Snowflake_schema) schema for optimal performance for analytical queries.
+  Less suitable for data lake implementation.

 Because of these reasons and the exponential growth of data in recent years, data warehouses by themselves prove to be less agile and tend to increase the time to market to realize data products in a large organization.

 Also, there is an increasing need for organizations to use several tools on this data to create modern data application, whereas traditional data warehouse patterns mostly supported [SQL](https://en.wikipedia.org/wiki/SQL) and BI workloads.

 In recent years, with the advent of cloud and big data tools, organizations are making a shift towards a modern data architecture pattern.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
