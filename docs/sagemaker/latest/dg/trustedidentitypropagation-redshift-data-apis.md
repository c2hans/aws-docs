---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-redshift-data-apis.html
---

# Connect Studio JupyterLab notebooks to Redshift Data API with trusted identity propagation enabled
<a name="trustedidentitypropagation-redshift-data-apis"></a>

Amazon Redshift Data API enables you to interact with your Amazon Redshift clusters programmatically without managing persistent connections. When combined with trusted identity propagation, the Redshift Data API provides secure, identity-based access to your data warehouse, allowing you to run SQL queries and retrieve results while maintaining full audit trails of user activities. This integration is particularly valuable for data science workflows that require access to structured data stored in Redshift. The following page includes information and instructions on how to connect trusted identity propagation with Amazon SageMaker Studio to Redshift Data API.

To connect Studio to Redshift Data API with trusted identity propagation enabled, ensure you have completed the following setups:
+  [Setting up trusted identity propagation for Studio](trustedidentitypropagation-setup.md)
+  [Using Redshift Data API with trusted identity propagation](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-trusted-identity-propagation.html)
  + Ensure your execution role has relevant permissions for Redshift Data API. See [authorizing access](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api-access.html) for more information.
+  [Simplify access management with Amazon Redshift and AWS Lake Formation for users in an External Identity Provider](https://aws.amazon.com/blogs/big-data/simplify-access-management-with-amazon-redshift-and-aws-lake-formation-for-users-in-an-external-identity-provider/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
