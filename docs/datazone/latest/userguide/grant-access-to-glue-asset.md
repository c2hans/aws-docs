---
source_url: https://docs.aws.amazon.com/datazone/latest/userguide/grant-access-to-glue-asset.html
---

# Grant access to managed AWS Glue Data Catalog assets in Amazon DataZone
<a name="grant-access-to-glue-asset"></a>

In Amazon DataZone, subscription requests and approved or granted subscriptions for **read** access to the assets are managed by asset owners.

**Note**
Access management for the AWS Glue Data Catalog assets using the AWS Lake Formation LF-TBAC method is not supported.
Support for cross-Region sharing of assets in AWS Glue Data Catalog is not supported.

Once a subscription request to managed AWS Glue Data Catalog assets is approved, Amazon DataZone automatically adds these assets to all the existing data lake environments in the project. Amazon DataZone then grants and manages access to the approved AWS Glue Data Catalog tables on your behalf through AWS Lake Formation. For the subscriber project, assets that are granted appear in the AWS Glue Data Catalog as resources in your account. You can then use Amazon Athena to query the tables.

**Note**
If a new data lake environment is added to the project after the subscribed AWS Glue Data Catalog assets have been automatically added to the existing data lake environments, you have to manually add these subscribed AWS Glue Data Catalog assets to this new data lake environment. You can do this by choosing the **Add grant** option in the **Data** tab of the project's overview page in the Amazon DataZone data portal.

For Amazon DataZone to be able to grant access to AWS Glue Data Catalog tables, the following conditions must be met.
+ The AWS Glue table must be Lake Formation-managed since Amazon DataZone grants access by managing Lake Formation permissions.
+ The **Manage access role** for the data lake environment used to publish the AWS Glue Data Catalog table must have the following Lake Formation permissions:
  + `DESCRIBE` and `DESCRIBE GRANTABLE` permissions on the AWS Glue database that contains the published table.
  + `DESCRIBE`, `SELECT`, `DESCRIBE GRANTABLE`, `SELECT GRANTABLE` permissions in Lake Formation on the published table itself.

For more information, see [Granting and revoking permissions on catalog resources](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-permissions.html) in the *AWS Lake Formation Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
