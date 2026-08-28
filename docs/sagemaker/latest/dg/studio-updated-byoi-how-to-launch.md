---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-byoi-how-to-launch.html
---

# Launch a custom image in Studio
<a name="studio-updated-byoi-how-to-launch"></a>

After you have attached a custom image to your Amazon SageMaker AI domain, the image becomes available to the users in the domain. Use the following instructions to launch an application with the custom image.

**Note**
If you have attached a custom image to your SageMaker Unified Studio project, you will need to launch the application from within SageMaker Unified Studio. For more information, see [Launch your custom image](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/byoi-launch-custom-image.html) in the *Amazon SageMaker Unified Studio User Guide*.

1. Launch Amazon SageMaker Studio. For instructions, see [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. If not done so already, expand the **Applications** section.

1. Choose the application from the **Applications** section. If you do not see the application available, the application may be hidden from you. In this case, contact your administrator.

1. To create a space, choose **\+ Create {{application}} space** and follow the instructions to create the space.

   To choose an existing space, choose the link name of the space you want to open.

1. Under **Image**, choose the image you want to use.

   If the **Image** dropdown is unavailable, you may need to stop your space. Choose **Stop space** to do so.

1. Confirm the settings for the space and choose **Run space**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
