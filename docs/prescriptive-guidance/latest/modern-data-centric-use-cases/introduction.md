---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/introduction.html
---

# Best practices for designing and implementing modern data-centric architecture use cases
<a name="introduction"></a>

*Apoorva Patrikar and Santosh Gantaram, Amazon Web Services*

Organizations are increasingly moving away from application-centric architectures to embrace data-centric architectures where IT infrastructure, application development, and even business processes are designed around data requirements. In a data-centric archicture, data is a core IT asset, and you design your IT systems and processes to optimize your data.

This guide offers best practices for designing a modern data-centric archicture for your use case. You can use these best practices to modernize your data pipelines and the data engineering operations that support that pipeline. This guide also provides an overview of the lifecycle of data in a data pipeline. By understanding this lifecycle, you can build data pipelines that optimize your data.

You can use this guide to overcome the following challenges that many organizations face when designing a data-centric architecture for data pipelines:
+ **Aversion to storing multiple versions of the same dataset** – It's not uncommon to frequently process data multiple times, but this approach has its limitations. In fact, it's often less resource intensive and more cost effective to avoid processing data multiple times. This guide shows you the benefit of taking a different approach that focuses on storing processed data in multiple stages.
+ **Reluctance to embrace data lakes** – It can be difficult to sort through the marketing claims around data lakes, and it can also be challenging to figure out if your organization has the skills and resources required for incorporating a data lake into your IT systems and processes. This guide can help you understand how a data lake can be a useful component in your data-centric architecture.
+ **Hiring enough data engineers** – Market trends suggest that data scientists are expected to perform data engineering tasks in many organizations even though they don't have the right data engineering skills. This skills gaps can have an impact on your time-to-market plans. This guide can help you better understand what data engineering skills are essential for designing a data-centric architecture.
+ **Lack of knowledge about using AWS services for horizontal processing** – Horizontal or distributed processing enables a cluster to process chunks of data in parallel by mapping tasks to multiple nodes and collecting the result before sending it transparently to the user. The move toward horizontal processing represents a shift around how data is viewed and processed. This shift affects not just application logic or the application itself but also the way organizations work with data. For example, horizontal processing affects central storage, task distribution, and modularization. Horizontal processing also favors larger chunks of data for read-write operations. This guide explains how horizontal processing can work for your data pipeline.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
