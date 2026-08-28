---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/update-project-profile.html
---

# Update project profiles
<a name="update-project-profile"></a>

 Complete the following procedure to update a project profile for your domain.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) and use the region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose an existing domain where you want to update a project profile.

1. Choose the **Project profiles** tab and then choose the project profile that you want to update. You can choose the All capabilities project profile, the Generative AI application development project profile, the SQL analytics project profile, or your custom project profile.

1. In the project profile details page, choose **Edit**.

1. You can make changes to the project profile description, default Tooling blueprint deployment settings, including systems manager configuration parameters, the Tooling blueprint parameters, and notes for project owners. Here you can also choose between default storage and Git storage.

   Once you're done making updates, choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
