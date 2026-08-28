---
source_url: https://docs.aws.amazon.com/datazone/latest/userguide/publishing-data.html
---

# Data inventory and publishing in Amazon DataZone
<a name="publishing-data"></a>

This section describes the tasks and procedures that you want to perform in order to create an inventory of your data in Amazon DataZone and to publish your data in Amazon DataZone.

In order to use Amazon DataZone to catalog your data, you must first bring your data (assets) as inventory of your project in Amazon DataZone. Creating inventory for a particular project, makes the assets discoverable only to that project’s members. Project inventory assets are not available to all domain users in search/browse unless explicitly published. After creating a project inventory, data owners can curate their inventory assets with the required business metadata by adding or updating business names (asset and schema), descriptions (asset and schema), read me, glossary terms (asset and schema), and metadata forms.

The next step of using Amazon DataZone to catalog your data, is to make your project’s inventory assets discoverable by the domain users. You can do this by publishing the inventory assets to the Amazon DataZone catalog. Only the latest version of the inventory asset can be published to the catalog and only the latest published version is active in the discovery catalog. If an inventory asset is updated after it's been published into the Amazon DataZone catalog, you must explicitly publish it again in order for the latest version to be in the discovery catalog.

For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md)

**Topics**
+ [Configure Lake Formation permissions for Amazon DataZone](lake-formation-permissions-for-datazone.md)
+ [Create custom asset types in Amazon DataZone](create-asset-types.md)
+ [Create and run an Amazon DataZone data source for the AWS Glue Data Catalog](create-glue-data-source.md)
+ [Create and run an Amazon DataZone data source for Amazon Redshift](create-redshift-data-source.md)
+ [Edit a data source in Amazon DataZone](edit-data-source.md)
+ [Delete a data source in Amazon DataZone](delete-data-source.md)
+ [Publish assets to the Amazon DataZone catalog from the project inventory](publishing-data-asset.md)
+ [Manage inventory and curate assets in Amazon DataZone](update-metadata.md)
+ [Manually create an asset in Amazon DataZone](create-data-asset-manually.md)
+ [Unpublish an asset from the Amazon DataZone catalog](archive-data-asset.md)
+ [Delete an Amazon DataZone asset](delete-data-asset.md)
+ [Manually start a data source run in Amazon DataZone](manually-start-data-source-run.md)
+ [Asset revisions in Amazon DataZone](asset-versioning.md)
+ [Data quality in Amazon DataZone](datazone-data-quality.md)
+ [Using machine learning and generative AI in Amazon DataZone](autodoc.md)
+ [Data lineage in Amazon DataZone](datazone-data-lineage.md)
+ [Metadata enforcement rules for publishing](metadata-rules-publishing.md)
+ [Connect Snowflake as a data source in Amazon DataZone](snowflake-data-source.md)
+ [Enable Snowflake lineage for AWS Glue Spark jobs](snowflake-lineage-glue-spark.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
