---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/launch-the-stack.html
---

# Launch the stack
<a name="launch-the-stack"></a>

Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 20 minutes

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and select the button to launch the `video-on-demand-on-aws` AWS CloudFormation template.

    [![Video on Demand solution launch button](https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fvideo-on-demand-on-aws%2Flatest%2Fvideo-on-demand-on-aws.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch this solution in a different AWS Region, use the region selector in the console navigation bar.
**Note**
This solution uses AWS Elemental MediaConvert and AWS Elemental MediaPackage, which are not available in all AWS Regions. You must launch this solution in a Region that supports these services. For the most current service availability by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box, and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, refer to [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Notification Email Address</b> </td><td> {{&lt;Requires input&gt;}} </td><td>A valid email address to receive Amazon SNS notifications.</td></tr>
  <tr><td> <b>Workflow Trigger</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Choose <code>VideoFile</code> to ingest source videos only; choose <code>MetadataFile</code> to ingest metadata files and source videos.</td></tr>
  <tr><td> <b>Archive Source Content</b> </td><td> <code>false</code> </td><td>Choose <code>GLACIER</code> to activate an Amazon S3 lifecycle policy on the source bucket to move applicable files to Amazon S3 Glacier after seven days, DEEP_ARCHIVE to move to Glacier Deep Archive.</td></tr>
  <tr><td> <b>Enable SNS</b> </td><td> <code>true</code> </td><td>Choose <code>true</code> receive SNS notifications for the ingest and pushlish workflows. Choose <code>false</code> to only receive error messages.</td></tr>
  <tr><td> <b>Enable SQS</b> </td><td> <code>true</code> </td><td>Choose <code>true</code> to deploy an SQS queue for publishing messages.</td></tr>
  <tr><td> <b>Enable Frame Capture</b> </td><td> <code>false</code> </td><td>Choose <code>true</code> to create thumbnails for each AWS Elemental MediaConvert output.</td></tr>
  <tr><td> <b>Accelerated Transcoding</b> </td><td> <code>PREFERRED</code> </td><td>Choose <code>PREFERRED</code> to activate Accelerated Transcoding for supported file types (recommended), ENABLE to apply to all encoding jobs.</td></tr>
  <tr><td> <b>Enable MediaPackage</b> </td><td> <code>false</code> </td><td>Choose <code>true</code> to activate AWS Elemental MediaPackage as part of the workflow.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template will create IAM resources.

1. Choose **Submit** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a `CREATE_COMPLETE` status in approximately 20 minutes.

   After the stack is created, Amazon SNS sends three subscription notifications to the admin email address with links to activate encoding, publishing, and error notification.

1. In the subscription notification emails, select each link to activate SNS notifications.

**Note**
In addition to the AWS Lambda functions that create solution resources and trigger the ingest and publishing processes, this solution includes the `custom-resource` Lambda function, which runs only during initial configuration or when resources are updated or deleted.
When running this solution, the `custom-resource` Lambda function is inactive. However, do not delete the function as it is necessary to manage associated resources.
