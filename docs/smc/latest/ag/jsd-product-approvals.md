---
source_url: https://docs.aws.amazon.com/smc/latest/ag/jsd-product-approvals.html
---

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html).

# Jira Service Management Approvals for Products in Service Catalog Portfolios
<a name="jsd-product-approvals"></a>

The AWS Service Management Connector for Jira Service Management enables administrators to configure approvals for products at the portfolio level. All products in a portfolio that contain approval permissions require approval, so AWS and Jira administrators might need to collaborate on the Service Catalog portfolio structure.

**To configure the approval process**

1. Choose **AWS Accounts**.

1. Choose **Manage** on the AWS account for which you want to configure portfolio approvals.

1. In the **Permission to approve** column, choose **Add groups** for the portfolios that require product approvals.

1. Select **Require approval for provisioning**.

1. Under **Permission to approve**, choose **Add group**.

1. Choose **Save**.

**Note**
If a portfolio only has a group associated with **Permissions to request**, products in the portfolio immediately provision when you submit the product request.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Management Connector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query smc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
