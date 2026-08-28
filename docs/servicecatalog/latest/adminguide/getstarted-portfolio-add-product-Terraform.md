---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-portfolio-add-product-Terraform.html
---

# Step 4: Add product to portfolio
<a name="getstarted-portfolio-add-product-Terraform"></a>

After creating a portfolio, you can add the HashiCorp Terraform product you created in Step 2.

**To add a product to a portfolio**

1.  Navigate to the **Products list** page.

1.  Select the Simple S3 bucket Terraform product you created in Step 2, and then choose **Actions**. From the drop down menu, choose **Add product to portfolio**. AWS Service Catalog displays the **Add Simple S3 bucket to portfolio** pane.

1. Select the S3 bucket portfolio, and then turn off **Create launch constraint**. You will create the launch constraint later in the tutorial.

1. Choose **Add product to portfolio**.

After successfully adding the product to the portfolio, AWS Service Catalog displays a confirmation banner on the Product list page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
