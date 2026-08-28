---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/version-dependencies.html
---

# Version dependencies
<a name="version-dependencies"></a>

The version dependencies focus area helps you to build a roadmap of your migration journey through various versions to reach the latest version of Amazon OpenSearch Service. Consider the following are key points:
+ Selecting the engine version
+ Upgrading to the latest version
+ Version upgrade strategy
+ Pre-upgrade checks

## Selecting the engine version
<a name="engine-version"></a>

It is very important to consider version dependencies carefully. Amazon OpenSearch Service supports a number of Elasticsearch versions and all major OpenSearch engine versions. (However, the latest version of OpenSearch can take a few weeks to be supported in Amazon OpenSearch Service from the date of release.) We recommend that you review the [features supported by engine version](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/features-by-version.html) in the Amazon OpenSearch Service documentation to identify the right version for your requirements. By choosing the same major (and closest minor) version, you can use the [snapshot restore approach](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/migration.html) to migrate. This is often the most direct approach.

## Upgrading to the latest OpenSearch Service version
<a name="upgrade"></a>

While you might be able to operate an earlier version of Amazon OpenSearch Service, we highly recommend upgrading to the latest available version. This helps you take advantage of the performance improvements, reliability, cost savings, and many new features that are available in the latest versions of the engine. Migration is a good opportunity to reduce the technical debt that can be incurred from running earlier versions of software.

## Version upgrade strategy
<a name="upgrade-strategy"></a>

If you decide that you want to upgrade to the latest version of the software during the migration, determine the steps and an upgrade strategy. Amazon OpenSearch Service documentation provides information on [upgrade paths](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/version-migration.html). It's important to understand the breaking changes between different versions. In some cases, the breaking changes might require you to plan for adjustments to your index modeling and design.

**Note**
The *Multiple mapping types* functionality is available only in Elasticsearch versions 5.x and earlier. Indexes created in versions 6.x and later support only a single mapping type for each index. If you are using multiple mapping types, we recommend remodeling that data into multiple indexes.

In the case of a time-sensitive migration, consider a basic option where you perform an equivalent version migration (for example, 5.x to 5.x), and then upgrade the OpenSearch Service version at a later date. OpenSearch Service offers in-place upgrades for domains that run Elasticsearch versions 5.1 (if compatible) or later, and OpenSearch 1.0 or later. Perform a test to see if your indexes are compatible for in-place upgrades when you are running Elasticsearch version 5.x. This means you might be able to migrate to the equivalent version, and perform an in-place upgrade after you have made the necessary changes to make your indexes and other functionality compatible with the latest version. Review the [upgrade domain documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/version-migration.html) carefully.

## Pre-upgrade checks
<a name="checks"></a>

Amazon OpenSearch Service upgrade functionality can perform [pre-upgrade checks](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/version-migration.html) by scanning the environment to determine issues that can block the upgrade. The upgrade doesn't proceed to the next step unless these checks succeed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
