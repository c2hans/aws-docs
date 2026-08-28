---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-ui-customize-instances-images.html
---

# Hide instance types and images in the Amazon SageMaker Studio UI
<a name="studio-updated-ui-customize-instances-images"></a>

**Important**
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the updated Studio experience. For information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md).

This topic shows how to hide Amazon SageMaker AI instance types and images displayed in the Amazon SageMaker Studio user interface (UI). For information on the Studio UI, see [Amazon SageMaker Studio UI overview](studio-updated-ui.md).

When you hide SageMaker AI instance types and images:
+ The impacted users will not be able to view the hidden resources in the Studio UI.
+ The impacted users will not be able to run or create a new space with the hidden configurations.
+ Any currently running spaces for the impacted users will not be effected.
+ When an impacted user attempts to run a space with the hidden resources, they will be notified that the relevant resources have been disabled by the administrator.

**Note**
If, instead of *hiding*, you would like to *restrict* the instance types available to users through an AWS Identity and Access Management policy, see:
[Can I limit the type of instances that data scientists can launch for training jobs in SageMaker AI?](https://repost.aws/questions/QUd77APmdHTx-2FZCvZfS6Qg/can-i-limit-the-type-of-instances-that-data-scientists-can-launch-for-training-jobs-in-sagemaker) in AWS re:Post.
[Limiting instances types on Amazon SageMaker AI via IAM policy](https://stackoverflow.com/questions/76426316/limiting-instances-types-on-aws-sagemaker-via-iam-policy) in StackOverflow.

The customize Studio UI feature is not available in Amazon SageMaker Studio Classic.

You can customize the Studio UI on a domain level and a user level:
+ Customization on a domain level sets the default for all users in the domain.
+ Customization on a user level will take priority over the domain level settings.

Use the following topics to learn more on the different customization levels and how to apply them.

**Topics**
+ [Hide instance types and images on a domain level](studio-updated-ui-customize-instances-images-domain.md)
+ [Hide instance types and images on a user level](studio-updated-ui-customize-instances-images-user.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
