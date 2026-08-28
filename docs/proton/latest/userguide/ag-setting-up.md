---
source_url: https://docs.aws.amazon.com/proton/latest/userguide/ag-setting-up.html
---

End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October 7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure will remain intact. For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# Setting up
<a name="ag-setting-up"></a>

Complete the tasks in this section so that you can create and register service and environment templates. You need these to deploy environments and services with AWS Proton.

**Note**
We're offering AWS Proton at no additional expense. You can create, register, and maintain service and environment templates at no charge. You can also count on AWS Proton to self-manage its own operations, such as storage, security, and deployment. The only expenses that you incur while using AWS Proton are the following.
Costs of deploying and using AWS Cloud resources that you instructed AWS Proton to deploy and maintain for you.
Costs of maintaining an AWS CodeStar connection to your code repository.
Costs of maintaining an Amazon S3 bucket, if you use a bucket to provide inputs to AWS Proton. You can avoid these costs if you switch to [Template sync configurations](ag-template-sync-configs.md) using Git repositories for your [Template bundles](ag-template-authoring.md#ag-template-bundles).

**Topics**
+ [Setting up with IAM](ag-setting-up-iam.md)
+ [Setting up with AWS Proton](setting-up-for-service.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
