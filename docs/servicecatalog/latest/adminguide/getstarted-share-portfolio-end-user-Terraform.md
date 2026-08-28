---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-share-portfolio-end-user-Terraform.html
---

# Step 8: Share portfolio with end user
<a name="getstarted-share-portfolio-end-user-Terraform"></a>

The AWS Service Catalog administrator can distribute portfolios with end user accounts using either account-to-account sharing or AWS Organizations sharing. In this tutorial, you are sharing your portfolio with the organization from the administrator account (hub account), which is also the management account of the Organization.

**To share the portfolio from the admin hub account**

1. Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/).

1. On the **Portfolios** page, select the S3 bucket portfolio. In the **Actions** menu, choose **Share**.

1. Choose **AWS Organizations**, and then filter into your organizational structure.

1. In the **AWS Organization** pane, choose the end user account (spoke account).

   You can also select a **Root node** to share the portfolio with the entire organization, a **parent Organizational Unit (OU)**, or a **child OU** within your organization based on your organization structure. For more information, review [Sharing a Portfolio](catalogs_portfolios_sharing_how-to-share.md).

1. In the **Share settings** pane, choose **Principal sharing**.

1. Choose **Share**.

After successfully sharing the portfolio with end users, the next step is to verify the end user experience and provision the Terraform product.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
