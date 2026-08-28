---
source_url: https://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/derive-insights-from-aws-modern-data.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Derive Insights from AWS Modern Data
<a name="derive-insights-from-aws-modern-data"></a>

Publication date: **June 3, 2021** ([Document history](document-revisions.md))

 [Modern Data architecture](https://aws.amazon.com/big-data/datalakes-and-analytics/data-lake-house/) enables you to query data across your data warehouse, data lake, and operational databases to gain faster and deeper insights that would not be possible otherwise. This whitepaper helps cloud architects, data scientists, and developers in deriving insights from Modern Data in the Amazon Web Services (AWS) Cloud by providing various design patterns based on user role or job function.

 This paper concludes with scenarios that showcase the Modern Data persona-centric analytics options, and additional resources for getting started with Modern Data on AWS.

## Introduction
<a name="introduction"></a>

 As we become a more digital society, the amount of data being created and collected constantly grows and accelerates. Organizations collect and analyze increasing amounts of data to make better decisions as quickly as changes occur. Traditional on-premises solutions for data storage, data management, and analytics can no longer keep pace. Data siloes that aren’t built to work well together make it difficult to consolidate data to perform comprehensive and efficient analytics. This limits an organization’s agility, ability to derive more insights and value from its data, and capability to adopt more sophisticated analytics tools and processes as its needs evolve. As a result, AWS has noted an acceleration in customers looking to modernize their data and analytics infrastructure by moving to the cloud.

 Organizations often build data warehouse and data lake solutions in isolation from each other, each having its own separate data ingestion, storage, management, and governance layers. These disjointed efforts to build separate data warehouse and data lake ecosystems often end up creating data and processing silos, data integration complexity, excessive data movement, and data consistency issues. These can lead to delays and increased cost of data-driven decisions, and prevent the deeper insights that come when you analyze all your relevant data together.

 This whitepaper presents [Modern Data](https://aws.amazon.com/big-data/datalakes-and-analytics/data-lake-house/) persona-centric usage patterns that enable you to collect, manage, process, and analyze all your structured and unstructured data in a simple and integrated fashion. A Modern Data architecture also enables you to use all your data for a variety of use cases, such as interactive SQL, business intelligence (BI), machine learning (ML), streaming, and big data analytics.

 This whitepaper first discusses the concept of the Modern Data solution as compared to data warehouse and data lake solutions. It then presents three Modern Data patterns to derive insights from your Modern Data, based on user role or job function.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
