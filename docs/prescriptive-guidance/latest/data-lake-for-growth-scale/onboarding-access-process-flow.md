---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/onboarding-access-process-flow.html
---

# Onboarding and granting access
<a name="onboarding-access-process-flow"></a>

This guide's data lake reference architecture helps you to independently scale data producers and data consumers, in addition to defining and establishing a consistent process for onboarding and granting access to those data consumers.

The following sections describe the onboarding process for data producers and data consumers and how to grant access in a data consumer account. This guide uses the [named resource method](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-cat-perms-named-resource.html) between the centralized catalog and data consumers. The process for the [LF-TBAC method](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-perms-TBAC.html) is similar but slightly different. We recommend that you evaluate and configure these approaches to meet your organization's data governance practices and policies.

For more information about these two methods, see the [Centralized catalog](reference-architecture-components.md#centralized-catalog) section of this guide.

## Onboarding data producers
<a name="onboarding-data-producers"></a>

The following diagram shows how to onboard a new data producer to your data lake.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/images/guide-img/dab5abfa-9d34-4ff1-9eb1-8a82c673378f/images/f031ec8a-d6a1-4694-a3d5-a751c4f8cb71.png)

The diagram shows the following onboarding process:

1. The data producer selectively provides the centralized catalog with access to its data (for example, an Amazon Simple Storage Service (Amazon S3) bucket and AWS KMS key). Access is provided to the centralized catalog's AWS Identity and Access Management (IAM) principals to register the data producer's data lake location in AWS Lake Formation and the IAM principals used to maintain the data producer's catalog.

1. Register the data producer's data lake location (for example, an Amazon S3 bucket) that uses the centralized catalog's Lake Formation.

1. Create the database, tables, and table schemas for the new data from the data producer in the AWS Glue Data Catalog.

## Onboarding data consumers
<a name="onboarding-data-consumers"></a>

The following diagram shows how to onboard a new data consumer to your data lake.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/images/guide-img/dab5abfa-9d34-4ff1-9eb1-8a82c673378f/images/c4bd5cc0-5a61-4c69-8e58-438d4c3ca364.png)

The diagram shows the following onboarding process:

1. The data consumer requests approval to view the data producer's data and specifies the data that it needs to access.

1. The data producer's data steward reviews the request from the data consumer and evaluates whether to:
   + Share some or all tables in the requested databases. We recommend database-level sharing when there are no data security implications of sharing all tables with the data consumer, which helps avoid the management overhead of table-level sharing.
   + Share at the data consumer's organization, OU, or account level.

1. When approved by the data producer, the required Data Catalog resources are shared with the data consumer in the centralized catalog.

1. Resource links can be created in the data consumer's account by using Lake Formation and then point to the shared Data Catalog resources in the centralized catalog.

After the onboarding process is complete, the data consumer's Lake Formation administrator can see the database catalog resource from the centralized catalog and the resource link. At this stage, no one else in the data consumer's account can access the data producer's data.

## Grant Select access in a data consumer account
<a name="grant-select-access-in-a-data-consumer-account"></a>

The following diagram shows the process for granting [Select access](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-table-permissions.html) to shared data resources with a local IAM principal in the data consumer account. The local IAM principal can be the IAM role for individual users or an IAM role that is consumed by specific AWS services.

**Note**
When the data being shared is of low sensitivity, you can delegate access granting to the data consumer itself without requiring approval from the data producer. This is because trust and sharing are already established between them.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/data-lake-for-growth-scale/images/guide-img/dab5abfa-9d34-4ff1-9eb1-8a82c673378f/images/eab1e988-490b-4e30-9470-d9f9af414ea3.png)

The diagram shows the following process:

1. The individual IAM principal in the data consumer account requests Select access to the resource link from the IAM principal in the data consumer account.

1. The data producer's data steward reviews the request from the data consumer and provides approval if all requirements are met.

1. Select access is granted and this allows the IAM principal to consume the requested data.
