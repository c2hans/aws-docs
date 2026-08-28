---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-resourceupdate.html
---

# AWS Service Catalog Tag Update Constraints
<a name="constraints-resourceupdate"></a>

**Note**
AWS Service Catalog does not support tag update constraints for Terraform Open Source products.

With tag update constraints, AWS Service Catalog administrators can allow or disallow end users to update tags on resources associated with a provisioned product. If tag updating is allowed, then new tags associated with the product or portfolio will be applied to provisioned resources during a provisioned product update.

**To enable tag updates to a product**

1. Open the Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/).

1. Choose the portfolio that contains the product you want to update.

1. Choose the **Constraints** tab and choose **Add constraints**.

1. Under **Constraint type**, choose **Tag Update**.

1. Choose the product from **Product**, then choose **Continue**.

1. On the **Tag Updates page**, select **Enable Tag Updates**.

1. Choose **Submit**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
