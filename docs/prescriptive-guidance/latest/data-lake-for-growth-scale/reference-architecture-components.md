---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/reference-architecture-components.html
---

# Reference architecture components
<a name="reference-architecture-components"></a>

The following diagram shows the three components of this guide's reference architecture: data producers, data consumers, and the centralized catalog.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/images/guide-img/dab5abfa-9d34-4ff1-9eb1-8a82c673378f/images/272b1faa-a96d-445f-ab66-a7318e19dfa6.png)

The diagram shows the following components:

1. A data producer account.

1. A centralized catalog.

1. Two data consumer accounts, which include data-serving and application types.

**Note**
 The diagram shows only one data producer and two data consumers, but this guide's reference architecture supports multiple data producers and data consumers when the data lake grows.

Understanding each component helps your organization to implement reusable patterns and scale your data lake by independently and consistently onboarding new data producers and data consumers.

The following sections discuss the reference architecture's components:
+ [Data producers ](#data-producers)
+ [Centralized catalog ](#centralized-catalog)
+ [Data consumers ](#data-consumers)

## Data producers
<a name="data-producers"></a>

A data producer collects, processes, and stores data from their data domain, in addition to monitoring and ensuring the quality of their data assets. The following diagram shows the data producer account as a component of this guide's reference architecture.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/images/guide-img/dab5abfa-9d34-4ff1-9eb1-8a82c673378f/images/fb46a4ae-3f92-4041-94a4-355e6bb00e62.png)

Each data producer has a private Data Catalog managed by AWS Lake Formation in their AWS account that is used by their internal data process. Data producers provide the centralized catalog with selective permissions to their data, which means that Lake Formation in the centralized catalog account can access data that the data producer wants to share.

This means that data producers don't directly interact with data consumers. Instead, the data producer account and its data storage location are completely abstracted and hidden from the data consumer. This approach reduces costs by removing unnecessary overhead for data producers that experience an increase in their data consumers.

A change to the data producer's data location doesn't impact the data consumer if the new data location is registered by the centralized catalog. If the data producer wants to stop sharing a particular piece of data, they can remove the centralized catalog's permissions. This prevents data consumers from accessing the data and removes the need to manually revoke access for each data consumer.

By using public and private data catalogs, data producers can choose what to share with data consumers, while independently managing internal data access through a private data catalog.

The following table describes the two AWS services that data producers use to share data with the centralized catalog.

|  |  |
| --- |--- |
| [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) | Adjust the bucket policy for Amazon S3 buckets to provide data access to the AWS Identity and Access Management (IAM) roles in the centralized catalog.<br />Data producers can also share data stored in other data applications or services by using Amazon S3 as the intermediate data layer. |
| [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) | Provide permissions for the AWS managed keys to the IAM roles in the centralized catalog and the AWS KMS keys used to encrypt the shared Amazon S3 data in the data producer accounts. |

## Centralized catalog
<a name="centralized-catalog"></a>

The following diagram shows how the centralized catalog connects data producers and data consumers in the data lake.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/images/guide-img/dab5abfa-9d34-4ff1-9eb1-8a82c673378f/images/d6441264-4c5a-4a9c-9dcc-13be15126d71.png)

The centralized catalog stores and manages the shared data catalog for the data producer accounts. The centralized catalog also hosts the shared data's technical metadata (for example, table name and schema) and is the location where data consumers come to access data.

Data consumers can access data from multiple data producers in the centralized catalog and can then mix this data with their own data for further processing. Using a centralized catalog removes the need for data consumers to directly connect with different data producers and reduces operational overhead.

Because the centralized catalog has visibility into data sharing and data consumption by data producers and consumers, it can be an ideal location to apply your centralized data governance functions (for example, access auditing).

The following sections describe how the centralized catalog uses AWS Lake Formation and AWS Glue.

### AWS Lake Formation
<a name="9999999999999999lflong-.1402ab43-d829-5052-878e-b9858d780349"></a>

[AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) helps create databases in an AWS Glue Data Catalog that point to the locations of multiple data producers in your data lake. An AWS Identity and Access Management (IAM) role is created for Lake Formation in the centralized catalog. By using Lake Formation, the centralized catalog can selectively share data resources (for example, database, tables, or columns) with data consumers. The Lake Formation managed resources are shared with data consumers by using one of the following two methods:
+ [Named resource method](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-cat-perms-named-resource.html) – This method shares managed resources across accounts. Databases, tables, or column names must be specified and a resource can be shared to an organization, organizational unit (OU), or AWS account. To reduce the sharing and management overhead, we recommend that you share resources at higher levels where possible (for example, in an organization or OU instead of an AWS account) . However, you must make sure that this approach meets your organization's data security control requirements.
**Note**
This method works well for data consumers with an application type, where AWS services consume data from the data producer. The data access requirement from this type of data consumer is application-driven, prescriptive, and relatively static.
+ [Lake Formation tag-based access control (LF-TBAC) method](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-perms-TBAC.html) – LF-TBAC is particularly useful for data consumers with a data-serving type. However, Lake Formation tagged resources can currently only be shared at the AWS account level and not at the organization or OU level.

### AWS Glue
<a name="9999999999999999glulong-.c5f0b7ba-0c4c-5835-8524-7c26078f366d"></a>

You must create databases in AWS Glue for each data producer in your centralized catalog. Because the centralized catalog uses AWS Glue to host databases from all data producers, you must make sure that the database name is unique across all data producers and that it reflects the data producer and their type of data. For example, you can use the following database naming structure: `<Data_Producer>– <Environment>–<Data_Group>`
+ `<Data_Producer>` – The data producer's name.
+ `<Environment>` – The data lake environment, such as `dev` for a development environment, `sit` for a system integration test environment, or `prod` for a production environment.
+ `<Data_Group>` – The name of the data group that is used to separate data from a data producer into logical groups. You can use the source system name, ID, or abbreviation as the name. A database description also helps to describe the content and purpose of the database.

You can use an AWS Glue crawler on the data producer's data to maintain its schema in the centralized catalog's database. If data is regularly created on the same frequency by a data producer, you can use a single AWS Glue crawler. In all other cases, you should use multiple AWS Glue crawlers to accommodate different crawling frequencies. Depending on your business use case, the crawler can either be scheduled for a predefined frequency or initiated by events.

You can also maintain table schema in AWS Glue by calling the AWS Glue API to create or update the schema. Although this can provide flexibility, additional effort is required for code development and maintenance. Make sure that you evaluate the use case and business value and then choose the option that meets your requirements and has the least overhead.

## Data consumers
<a name="data-consumers"></a>

Data consumers consume the data from the data producer after the centralized catalog shares it using AWS Lake Formation. The following diagram shows two data consumers in the data lake.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/images/guide-img/dab5abfa-9d34-4ff1-9eb1-8a82c673378f/images/e7fc2a19-2b78-4b2f-b5e8-2e40cb4690a5.png)

There are two types of data consumer: *application* and *data-serving*. The following table describes these two types.

|  |
| --- |
| Application type | Application data consumers run applications in their own AWS accounts. The applications consume the AWS Identity and Access Management (IAM) roles to access the shared data from a data producer and then process it according to their logic.Typically, this type of data consumer has prescriptive data requirements to fulfill an application's needs. |
| --- |--- |
| **Data-serving type** | Data-serving data consumers are typically meant for individuals (for example, data analysts or data scientists) and applications (for example, a business intelligence application) that don't have their own AWS accounts.<br />Multiple data-serving data consumers can exist in one organization's data lake. For example, different lines of business might choose to set up their own data-serving data consumers to help users consume data from the data lake. These data consumers have their own IAM role principals configured in their AWS account (for example, IAM roles associated with [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)) that are used by end users in the data consumer account to access shared data through AWS services (for example, [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)).<br />Typically, this type of data consumer has wide-ranging and continuously increasing data requirements. |

AWS Lake Formation is the most important AWS service used by a data consumer for cross-account data sharing and accessing the centralized catalog. After databases are shared by the centralized catalog, the shared resources are available in Lake Formation in the data consumer account. Data access can then be granted to local IAM principals in the data consumer account, with permission from the data producer, if required. The shared data can then be used by AWS services integrated with Lake Formation (for example, Amazon Athena and AWS Glue). You can use the following AWS services to access shared data in the data consumer account:
+ [Amazon Athena ](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)is an interactive query service that helps directly analyze data in Amazon Simple Storage Service (Amazon S3) using standard SQL. For more information about Athena and Lake Formation, see [How Athena accesses data registered with Lake Formation](https://docs.aws.amazon.com/athena/latest/ug/lf-athena-access.html) in the Amazon Athena documentation.
+ [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html) helps you to efficiently query and retrieve structured and semi-structured data from files in Amazon S3 without having to load the data into Amazon Redshift tables. For more information about Redshift Spectrum and Lake Formation, see [Using Redshift Spectrum with AWS Lake Formation](https://docs.aws.amazon.com/redshift/latest/dg/spectrum-lake-formation.html) in the Amazon Redshift documentation.
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a fully managed extract, transform, and load (ETL) service that makes it simple and costeffective to categorize your data, clean it, enrich it, and move it reliably between different data stores and data streams. An AWS Glue ETL job's associated IAM role can access the data lake data managed by Lake Formation if it has the required access permissions.
+ [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html) helps run big data frameworks (for example, [Apache Hadoop](https://aws.amazon.com/elasticmapreduce/details/hadoop) and [Apache Spark](https://aws.amazon.com/elasticmapreduce/details/spark)) to process and analyze large amounts of data. For more information about Amazon EMR and Lake Formation, see [Integrate Amazon EMR with Lake Formation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-lake-formation.html) in the Amazon EMR documentation.
+ [Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) is a scalable, serverless, embeddable, and machine learning (ML)-powered business intelligence service that you can use to analyze and visualize data from your data lake. For more information about Amazon Quick and Lake Formation, see [Authorizing connections through Lake Formation ](https://docs.aws.amazon.com/quicksight/latest/user/lake-formation.html)in the Quick documentation.
+ [Amazon SageMaker Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html) reduces the time it takes to aggregate and prepare data for ML. For more information about Data Wrangler and Lake Formation, see [Prepare ML Data with Amazon SageMaker Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html) in the Amazon SageMaker AI documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
