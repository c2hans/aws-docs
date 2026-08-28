---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/data-warehousing-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data Warehousing on AWS
<a name="data-warehousing-on-aws"></a>

Publication date: **January 15, 2021** ([Document history and contributors](document-revisions.md))

 Enterprises across the globe want to migrate data warehousing to the cloud to improve performance and lower costs. This whitepaper discusses a modern approach to analytics and data warehousing architecture. It outlines services available on Amazon Web Services (AWS) to implement this architecture, and provides common design patterns to build data warehousing solutions using these services.

 This whitepaper is aimed at data engineers, data analysts, business analysts, and developers.

## Introduction
<a name="introduction"></a>

 Data is an enterprise’s most valuable asset. To fuel innovation, which fuels growth, an enterprise must:
+  Store every relevant data point about their business
+  Give data access to everyone who needs it
+  Have the ability to analyze the data in different ways
+  Distill the data down to insights

 Most large enterprises have data warehouses for reporting and analytics purposes. They use data from a variety of sources, including their own transaction processing systems, and other databases.

 In the past, building and running a data warehouse—a central repository of information coming from one or more data sources—was complicated and expensive. Data warehousing systems were complex to set up, cost millions of dollars in upfront software and hardware expenses, and took months of planning, procurement, implementation, and deployment processes. After making the initial investments and setting up the data warehouse, enterprises had to hire a team of database administrators to keep their queries running fast and protect against data loss.

 Traditional data warehouse architectures and on-premises data warehousing pose many challenges:
+  They are difficult to scale and have long lead times for hardware procurement and upgrades.
+  They have high overhead costs for administration.
+  Proprietary formats and siloed data make it costly and complex to access, refine, and join data from different sources.
+  They cannot separate cold (infrequently used) and warm (frequently used) data, which results in bloated costs and wasted capacity.
+  They limit the number of users and the amount of accessible data, which leads to anti-[democratization](https://towardsdatascience.com/data-democratization-918416c0f0e0) of data.
+  They inspire other legacy architecture patterns, such as retrofitting use cases to accommodate the wrong tools for the job, instead of using the correct tool for each use case.

 In this whitepaper, we provide the information you need to take advantage of the strategic shift happening in the data warehousing space from on-premises to the cloud:
+  Modern analytics architecture
+  Data warehousing technology choices available within that architecture
+  A deep dive on Amazon Redshift and its differentiating features
+  A blueprint for building a complete data warehousing system on AWS with Amazon Redshift and other AWS services
+  Practical tips for migrating from other data warehousing solutions and tapping into our partner ecosystem

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
