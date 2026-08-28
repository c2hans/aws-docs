---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-share-models.html
---

# Share Models
<a name="jumpstart-share-models"></a>

**Note**
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md).
Studio Classic is still maintained for existing workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md).

You can share JumpStart models through the Studio Classic UI directly from the **Launched JumpStart assets** page using the following procedure:

1. Open Amazon SageMaker Studio Classic and choose **Launched JumpStart assets** in the **JumpStart** section of the lefthand navigation pane.

1. Select the **Training jobs** tab to view the list of your model training jobs.

1. Under the **Training jobs** list, select the training job that you want to share. This opens the training job details page. You cannot share more than one training job at a time.

1. In the header for the training job, choose **Share**, and select **Share with my organization**.

For more information about sharing models with your organization, see [Shared Models and Notebooks](jumpstart-content-sharing.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
