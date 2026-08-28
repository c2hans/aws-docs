---
source_url: https://docs.aws.amazon.com/panorama/latest/dev/panorama-appliance.html
---

End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

# Managing the AWS Panorama Appliance
<a name="panorama-appliance"></a>

The AWS Panorama Appliance is the hardware that runs your applications. You use the AWS Panorama console to register an appliance, update its software, and deploy applications to it. The software on the AWS Panorama Appliance connects to camera streams, sends frames of video to your application, and displays video output on an attached display.

After setting up your appliance or another [compatible device](gettingstarted-concepts.md#gettingstarted-concepts-devices), you register cameras for use with applications. You [manage camera streams](appliance-cameras.md) in the AWS Panorama console. When you deploy an application, you choose which camera streams the appliance sends to it for processing.

For tutorials that introduce the AWS Panorama Appliance with a sample application, see [Getting started with AWS Panorama](panorama-gettingstarted.md).

**Topics**
+ [Managing an AWS Panorama Appliance](appliance-manage.md)
+ [Connecting the AWS Panorama Appliance to your network](appliance-network.md)
+ [Managing camera streams in AWS Panorama](appliance-cameras.md)
+ [Manage applications on an AWS Panorama Appliance](appliance-applications.md)
+ [AWS Panorama Appliance buttons and lights](appliance-buttons.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
