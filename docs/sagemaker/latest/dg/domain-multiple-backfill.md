---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/domain-multiple-backfill.html
---

# Backfill domain tags
<a name="domain-multiple-backfill"></a>

You can improve resource filtering by adding domain tags to untagged resources. If you have resources that are not tagged, you can backfill them.

If you have created resources in a domain before 11/30/2022, those resources are not automatically tagged with the domain Amazon Resource Name (ARN) tag.

To accurately attribute resources to their respective domain, you must add the domain tag to existing resources using the AWS CLI, as follows.

1. Map all existing SageMaker AI resources and their respective ARNs to the domains that exist in your account.

1. Run the following command from your local machine to tag the resource with the ARN of the resource's respective domain. This must be repeated for every SageMaker AI resource in your account.

   ```
   aws resourcegroupstaggingapi tag-resources \
       --resource-arn-list arn:aws:sagemaker:{{region}}:{{account-id}}:space/{{domain-id}}/{{space-name}} \
       --tags sagemaker:domain-arn=arn:aws:sagemaker:{{region}}:{{account-id}}:domain/{{domain-id}}
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
