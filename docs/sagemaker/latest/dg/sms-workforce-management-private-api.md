---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-private-api.html
---

# Private workforce management using the Amazon SageMaker API
<a name="sms-workforce-management-private-api"></a>

You can use Amazon SageMaker API operations to manage, update, and delete your private workforce. For each API operation listed on the following topics, you can find a list of supported language-specific SDKs and their documentation in the **See Also** section of the API documentation.

**Topics**
+ [Find your workforce name](sms-workforce-management-private-api-name.md)
+ [Restrict worker access to tasks to allowable IP addresses](sms-workforce-management-private-api-cidr.md)
+ [Enable a dual-stack workforce](sms-workforce-management-private-api-dualstack.md)
+ [Update OIDC Identity Provider workforce configuration](sms-workforce-management-private-api-update.md)
+ [Delete a private workforce](sms-workforce-management-private-api-delete.md)

To delete a private workforce, use the [`DeleteWorkforce`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteWorkforce.html) API operation. If you have any work teams associated with your workforce, you must delete those work teams before you delete your workforce. You can delete a private work team using the `[DeleteWorkteam](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteWorkteam.html)` operation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
