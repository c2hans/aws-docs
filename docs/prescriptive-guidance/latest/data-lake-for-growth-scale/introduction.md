---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/introduction.html
---

# Designing a data lake for growth and scale on the AWS Cloud
<a name="introduction"></a>

*Wei Shao and Tony Stricker, Amazon Web Services*

Organizations are increasingly designing and building data lakes on the Amazon Web Services (AWS) Cloud as part of their data modernization strategy. Data lakes can be repositories that store your structured and unstructured data at any scale and make it available to a wide range of internal and external users.

However, it can take significant time and effort to ingest data into data lakes that serve your growing business use cases. To help reduce costs and maximize the value that is generated from the data, many organizations plan a one-time ingestion of data into their data lake and then consume this data multiple times. Designing a data lake architecture that scales with data production, sharing, and consumption is critical for delivering value to business stakeholders when your data lake grows.

A scalable data lake architecture provides your organization with a solid foundation to gain value from your data lake while bringing more data into it. By continuously gaining data insights without being slowed down or interrupted because of scalability constraints, a scalable data lake also helps your organization remain competitive.

Typically, a data lake has *data producers* and *data consumers*. Data producers create data assets by collecting, processing, and storing data from their data domain. These collective data assets form the content of your data lake. Data producers can choose to selectively share their data assets with the data lake's data consumers.

Data consumers need the data from the data producers to fulfill their business use cases and can also occasionally combine this data with their own data. Data producers and data consumers are typically, but not always, part of your organization. Importantly, they can both be data producers or data consumers at the same time.

A scalable data lake architecture helps you to achieve the following outcomes:
+ Onboard data producers at scale without requiring them to maintain the entire data sharing process. This helps data producers onboard their data into the data lake and focus on collecting, processing, and storing data from their data domain.
+ Enable data consumers to access data from multiple data producers without increasing your overall costs and management overhead.

This guide describes the common scaling challenges that can occur when organizations grow their data lake, provides a data lake reference architecture, and outlines approaches for onboarding and granting access to data producers and data consumers. The data lake reference architecture in this guide leverages the different features and capabilities provided by [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html). The guide is intended for teams that are responsible for designing data lakes on the AWS Cloud, including enterprise data architects, data platform architects, designers, or data domain leads.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

You should expect the following three outcomes after designing a data lake for growth and scale on the AWS Cloud:
+ Lower data sharing and data consumption overheads across multiple lines of business in your organization.
+ A secure and consistent approach that helps your organization include external data producers and share data with them in your data lake.
+ Continuously gain data insights without being slowed down or interrupted because of scalability constraints.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
