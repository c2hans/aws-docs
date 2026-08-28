---
source_url: https://docs.aws.amazon.com/smc/latest/ag/config-SC-portfolios-jsd.html
---

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html).

# Configuring Service Catalog portfolios in Jira
<a name="config-SC-portfolios-jsd"></a>

This section describes how to configure AWS Service Catalog portfolios within Jira.

Once your account or accounts are set up and connectivity is successful, use the **AWS Account** page to manage, for each account, which groups can access each portfolio in each Region. You can expand and collapse each Region and edit and add groups for each portfolio. Only users in the designated groups have access to those products. By default, no groups have access.

**Note**
At least one group must be associated to a Service Catalog portfolio for Jira Service Management end users to request AWS products.

**To provision products and portfolios**

1. Choose **AWS Accounts**.

1. Choose **Manage** for the AWS account in which you want to configure portfolios.

1. Under **Portfolios**, expand the Region associated with the account. Portfolios display under each Region.

1. In the **Permission to request** column, choose **Add groups** for the portfolios that you want to make visible in Jira Service Management. Select the group you want to see and request Service Catalog products.
**Note**
Because the AWS Service Management Connector for Jira Service Management allows Jira users to provision AWS products in the portfolios their groups have access to, and to control those provisioned products, users should maintain security in their Jira accounts.

1. If products in this portfolio do not require approvals, choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Management Connector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query smc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
