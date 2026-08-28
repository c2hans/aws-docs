---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.html
---

# Creating an AMI from an Amazon EC2 Instance
<a name="tkv-create-ami-from-instance"></a>

You can create an Amazon Machine Image (AMI) with the AWS Toolkit for Visual Studio. For more detailed information about AMIs, see the [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/AMIs.html) topic in the *Amazon Elastic Compute Cloud for Windows Instances* User Guide.

 To create an AMI from an exiting Amazon EC2 instance, complete the following procedure.

**Creating an AMI from an existing Amazon EC2 instance**

1. From the AWS Toolkit Explorer, expand **Amazon EC2** and choose **Instances** to view a list of your existing instances.

1. Right-click the instance that you want to use as the basis for your AMI and choose **Create Image (ABS AMI)** to open the **Create Image** dialog window.

1. From the **Create Image** dialog window, add a name and a description for your image into the provided fields, then choose the **OK** button to continue.

1. The **Image Created** confirmation window opens in Visual Studio when the image is created, choose the **OK** button to continue.

To view your new AMI with the AWS Toolkit, expand **Amazon EC2** and double-click **AMIs** to open a window in the Visual Studio Editor payne that displays a list of your existing AMIs. If you don't see you new AMI in the list, choose the **Refresh** button located at the top of the AMI window.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-visual-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
