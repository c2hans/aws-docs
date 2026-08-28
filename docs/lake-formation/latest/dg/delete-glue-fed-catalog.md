---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/delete-glue-fed-catalog.html
---

# Deleting a federated catalog
<a name="delete-glue-fed-catalog"></a>

 You can delete the federated catalogs that you created in the AWS Glue Data Catalog using the `glue:DeleteCatalog` operation or the AWS Lake Formation console.

**To delete a federated catalog (console)**

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. In the navigation pane, choose **Catalogs** under **Data Catalog**.

1. Choose the catalog that you want to delete from the catalogs list.

1. Choose **Delete** from **Actions**.

1. Choose **Drop** to confirm and the federated catalog will be deleted from the Data Catalog.
![The delete catalog confirmation.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/delete-fed-catalog.png)

**To delete a federated catalog (CLI)**
+

  ```
  aws glue delete-catalog
    --catalog-id {{123456789012:catalog name}}
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
