---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/launch-the-stack.html
---

# Launch the stack
<a name="launch-the-stack"></a>

This automated AWS CloudFormation template deploys DeepRacer on AWS.

1. Sign in to the AWS Management Console and select the button to launch the CloudFormation template.

    [![Launch solution.](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/deepracer-on-aws/latest/deepracer-on-aws.template&redirectId=ImplementationGuide)

   Alternatively, you can [download the template](https://solutions-reference.s3.amazonaws.com/deepracer-on-aws/latest/deepracer-on-aws.template) as a starting point for your own implementation.

1. The template is launched in the US East (N. Virginia) region by default. To launch this solution in a different AWS region, use the region selector in the console navigation bar.
**Note**
This solution uses Amazon Cognito, which is currently available in specific AWS Regions only. Therefore, you must launch this solution in an AWS Region where Amazon Cognito is available. For the most current service availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.
**Important**
This solution provisions log groups that are set to be retained following stack deletion. If you have previously deployed DeepRacer on AWS, be sure to provide a unique stack name to prevent the deployment from failing due to log groups with the same name already existing.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>AdminEmail</b> </td><td> <i>&lt;Requires input&gt;</i> </td><td>Email address for the initial admin user. This user will be automatically added to the admin group.</td></tr>
  <tr><td> <b>CustomDomain</b> </td><td>&lt;Optional input&gt;</td><td>Custom domain URL for CORS allowlist (only if you have or plan to map a custom domain to CloudFront).</td></tr>
  <tr><td> <b>Namespace</b> </td><td> <i>&lt;Requires input&gt;</i> </td><td>The namespace for this deployment of DeepRacer. Lowercase alphanumeric characters of length between 3 and 12.</td></tr>
  <tr><td> <b>EmailDeliveryMethod</b> </td><td> <i>&lt;Requires input&gt;</i> </td><td>The delivery method to use for sending authentication emails, such as invitation emails and password resets. Options: <code>COGNITO</code> or <code>SES</code>. Default value: <code>COGNITO</code>. Amazon Cognito is the default option and requires no additional configuration, but is subject to a limit of 50 emails per day per account. For users requiring greater throughput, Amazon SES is recommended, but users must first complete the <a href="prerequisites.md">Prerequisites</a> in order to use that service.</td></tr>
  <tr><td> <b>SesVerifiedEmail</b> </td><td>&lt;Optional input&gt;</td><td>A verified email address to send authentication emails from. This is <b>required</b> if you selected <code>SES</code> as the <code>EmailDeliveryMethod</code>. This will be ignored if you selected <code>COGNITO</code> as the <code>EmailDeliveryMethod</code>, and can be left blank in that case.</td></tr>
  <tr><td> <b>SesIdentity</b> </td><td>&lt;Optional input&gt;</td><td>A verified SES domain used to authorize the email address for sending. Must be a domain, and must match the domain or be a parent domain of <code>SesVerifiedEmail</code>. If blank, defaults to the email address specified in <code>SesVerifiedEmail</code>. This is only relevant when <code>EmailDeliveryMethod</code> is <code>SES</code>. When using a domain identity, you must still provide <code>SesVerifiedEmail</code> as the sender address. For more information on domain identities, refer to <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html">Creating and verifying identities in Amazon SES</a>.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Be sure to check the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **Create stack** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately five minutes.
