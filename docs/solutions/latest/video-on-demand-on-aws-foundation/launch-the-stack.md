---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws-foundation/launch-the-stack.html
---

# Launch the stack
<a name="launch-the-stack"></a>

 Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 10 minutes

1.  Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and select the button to launch the `video-on-demand-on-aws-foundation.template` CloudFormation template. [![Launch button for the Video on Demand on AWS Foundation solution.](https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws-foundation/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?&templateURL=https://s3.amazonaws.com/solutions-reference/video-on-demand-on-aws-foundation/latest/video-on-demand-on-aws-foundation.template&redirectId=ImplementationGuide)

1.  The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
 This solution uses MediaConvert, which is available in specific AWS Regions only. Therefore, you must deploy this solution in a Region that supports this service. For the most current service availability by Region, refer to the [AWS Regional Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) List.

1.  On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next**.

1.  On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1.  Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th> Parameter </th><th> Default </th><th> Description </th></tr>
</thead>
<tbody>
  <tr><td><b> Notification Email Address </b></td><td>{{&lt;Requires input&gt;}}</td><td> A valid email address to receive Amazon SNS notifications. </td></tr>
</tbody>
</table>

1.  Select **Next**.

1.  On the **Configure stack options** page, choose **Next**.

1.  On the **Review and create** page, review and confirm the settings. Select the box acknowledging that the template creates IAM resources.

1.  Choose **Submit** to deploy the stack.

    You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 10 minutes.

    After the stack is created, Amazon SNS sends three subscription notifications to the admin email address with links to allow encoding, publishing, and error notifications.

1.  In the subscription notification emails, select each link to allow SNS notifications.
**Note**
 In addition to the Lambda functions that create solution resources and manage the workflow, this solution includes the `custom-resource` Lambda function, which runs only during initial configuration or when resources are updated or deleted.
 When running this solution, the `custom-resource` function is inactive. However, do not delete the function, since it is necessary to manage associated resources.
