---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/building-data-lake-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Storage Best Practices for Data and Analytics Applications
<a name="building-data-lake-aws"></a>

Publication date: **November 16, 2021** ([Document history](document-details.md))

Amazon Simple Storage Service (Amazon S3) and Amazon Glacier (Amazon Glacier) provide ideal storage solutions for data lakes. Data lakes, powered by Amazon S3, provide you with unmatched availability, agility, and flexibility required to combine different types of data and analytics approaches to gain deeper insights, in ways that traditional data silos and data warehouses cannot. In addition, data lakes built on Amazon S3 integrate with other analytical services for ingestion, inventory, transformation, and security of your data in the data lake. This guide explains each of these options and provides best practices for building, securing, managing, and scaling a data lake built on Amazon S3.

## Introduction
<a name="introduction"></a>

Because organizations are collecting and analyzing increasing amounts of data, traditional on-premises solutions for data storage, data management, and analytics can no longer keep pace. Data silos that aren’t built to work well together make it difficult to consolidate the storage for more comprehensive and efficient analytics. This, in turn, limits an organization’s agility and ability to derive more insights and value from its data. In addition, this reduces the capability to seamlessly adopt more sophisticated analytics tools and processes, because it necessitates upskilling of the workforce.

 A *data lake* is an architectural approach that allows you to store all your data in a centralized repository, so that it can be categorized, catalogued, secured, and analyzed by a diverse set of users and tools. In a data lake you can ingest and store structured, semi-structured, and unstructured data, and transform these raw data assets as needed. Using a cloud-based data lake you can easily decouple the compute from storage, and scale each component independently, which is a huge advantage over an on-premises or Hadoop-based data lake. You can use a complete portfolio of data exploration, analytics, machine learning, reporting, and visualization tools on the data. A data lake makes data and the optimal analytics tools available to more users, across more lines of business, enabling them to get all of the business insights they need, whenever they need them.

 More organizations are building data lakes for various use cases. To guide customers in their journey, Amazon Web Services (AWS) has developed a data lake architecture that allows you to build scalable, secure data lake solutions cost-effectively using [Amazon S3](https://aws.amazon.com/s3/) and other AWS services.

 Using the data lake built on Amazon S3 architecture capabilities you can:
+  Ingest and store data from a wide variety of sources into a centralized platform.
+  Build a comprehensive data catalog to find and use data assets stored in the data lake.
+  Secure, protect, and manage all of the data stored in the data lake.
+  Use tools and policies to monitor, analyze, and optimize infrastructure and data.
+  Transform raw data assets in place into optimized usable formats.
+  Query data assets in place.
+  Integrate the unstructured data assets from Amazon S3 with structured data assets in a data warehouse solution to gather valuable business insights.
+  Store the data assets into separate buckets as the data goes through extraction, transformation, and load process.
+  Use a broad and deep portfolio of data analytics, data science, machine learning, and visualization tools.
+  Quickly integrate current and future third-party data-processing tools.
+  Securely share processed datasets and results.
+  Scale virtually to unlimited capacity.

The remainder of this paper provides more information about each of these capabilities. The following figure illustrates a sample AWS data lake platform.

![High-level AWS data lake technical reference architecture](http://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/images/storage-best-practices1.png)
