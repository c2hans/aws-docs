---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-deploy.html
---

# Step 7: Grant end users access to the portfolio
<a name="getstarted-deploy"></a>

Now that you have created a portfolio and added a product, you are ready to grant access to end users.

**Prerequisites**
If you haven't created an IAM group for the endusers, see [Grant permissions to AWS Service Catalog end users](getstarted-iamenduser.md).

**To provide access to the portfolio**

1. On the portfolio details page, choose the **Access** tab.

1. Choose **Grant access**.

1. On the **Groups** tab, select the checkbox for the IAM group for the end users.

1. Choose **Add Access**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
