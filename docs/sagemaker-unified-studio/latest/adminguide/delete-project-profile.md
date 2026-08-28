---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/delete-project-profile.html
---

# Delete project profiles
<a name="delete-project-profile"></a>

 Complete the following procedure to delete a project profile for your domain.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) and use the region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose an existing domain where you want to delete a project profile.

1. Choose the **Project profiles** tab and then choose the project profile that you want to delete. You can choose the All capabilities project profile, the Generative AI application development project profile, the SQL analytics project profile, or your custom project profile.

1. In the project profile details page, choose **Delete**.

   Confirm the action in the D**elete project profile** pop up window by typing the project profile name in the text field and choosing **Delete**.
**Note**
Deleting a project profile is final. Deletion removes the project profile and its blueprint deployment settings from Amazon SageMaker Unified Studio. It does not delete the blueprints used to create the blueprint deployment settings which make up this project profile.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
