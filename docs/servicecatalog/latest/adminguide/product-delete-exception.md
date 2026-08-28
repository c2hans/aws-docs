---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/product-delete-exception.html
---

# Resolving failed resource disassociations when deleting a product
<a name="product-delete-exception"></a>

If your prior attempt to [delete a product](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/productmgmt-delete.html) failed due to resource disassociation exceptions, review the list of exceptions and their resolutions below.

**Note**
If you closed the **Deleting products** window prior to receiving the failed resource disassociation message, you can follow steps one through three in the proceeding *Delete a product* section to open the window again.

**To resolve a failed resource disassociation**

In the **Delete product** window, review the Associations table **Status** column. Identify the failed resource disassociation exception and the suggested resolutions:

| Status exception type | Cause | Resolution |
| --- | --- | --- |
| Product prod-\*\*\*\* | AWS Service Catalog could not delete the product because the product still has associated TagOptions, budgets, at least one ProvisioningArtifact with associated actions, the product is still assigned to a Portfolio, the product has users, or the product has constraints.  | Attempt to delete the product again. |
| User: username is not authorized to perform: | The user attempting to delete the product does not have the necessary permissions to disassociate the product's resources.  | AWS Service Catalog recommends contacting your account administrator for more information about disassociating product resources you do not currently have permissions to disassociate.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
