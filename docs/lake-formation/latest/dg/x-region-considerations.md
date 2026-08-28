---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/x-region-considerations.html
---

# Cross-Region data access limitations
<a name="x-region-considerations"></a>

 Lake Formation supports querying Data Catalog tables across AWS Regions. You can access data in a Region from other Regions using Amazon Athena, Amazon EMR, and AWS Glue ETL by creating resource links in other Regions pointing to the source databases and tables. With cross-Region table access, you can access data across Regions without copying the underlying data or the metadata into the Data Catalog.

The following limitations apply to cross-Region table access.
+ Lake Formation doesn't support querying Data Catalog tables from another Region using Amazon Redshift Spectrum.
+ In the Lake Formation console, the database and table views don't show the source Region database/table names.
+ To view the list of tables under a shared database from another Region, you need to first create a resource link to the shared database, then select the resource link, and choose **View tables**.
+ Lake Formation doesn't support cross-Region resource link calls made by SAML users.
+ Lake Formation's cross-Region feature doesn't involve additional charges for data transfers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
