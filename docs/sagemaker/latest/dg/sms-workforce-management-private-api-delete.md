---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private-api-delete.html
---

# Delete a private workforce
<a name="sms-workforce-management-private-api-delete"></a>

You can only have one private workforce in each AWS Region. You may want to delete your private workforce in an AWS Region when:
+ You want to create a workforce using a new Amazon Cognito user pool.
+ You have already created a private workforce using Amazon Cognito and you want to create a workforce using your own OpenID Connect (OIDC) Identity Provider (IdP).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
