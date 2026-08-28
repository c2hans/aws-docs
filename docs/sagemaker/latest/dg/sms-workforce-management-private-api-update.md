---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private-api-update.html
---

# Update OIDC Identity Provider workforce configuration
<a name="sms-workforce-management-private-api-update"></a>

You may want to update a workforce created using your own OIDC IdP to specify a different authorization endpoint, token endpoint, or issuer. You can update any parameter found in `[OidcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OidcConfig.html)` using the [`UpdateWorkforce`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateWorkforce.html) operation.

**Important**
You can only update your OIDC IdP configuration when there are no work teams associated with your workforce. You can delete a private work team using the `[DeleteWorkteam](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteWorkteam.html)` operation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
