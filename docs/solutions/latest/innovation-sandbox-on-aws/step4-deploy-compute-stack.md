---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/step4-deploy-compute-stack.html
---

# Step 4: Deploy the Compute stack
<a name="step4-deploy-compute-stack"></a>

In this step, you deploy the compute resources required for the ISB application.

**Important**
Ensure that you are logged in using the **Hub** account for deploying the Compute stack.

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and choose the button to launch the `Compute` stack CloudFormation template.

 [![Launch Stack](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?&templateURL=https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-Compute.template&redirectId=ImplementationGuide)

The template launches in the US East (N.Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box, and choose **Next**.

1. On the **Specify stack** details page, enter a stack name for your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the AWS Identity and Access Management User Guide.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Namespace</b> </td><td> {{myisb}} </td><td>Use the same namespace from the Account Pool stack deployment of Innovation Sandbox. For example, <b>myisb</b>.</td></tr>
  <tr><td> <b>Org Management Account Id</b> </td><td> {{&lt;Requires input&gt;}} </td><td>The AWS Account Id of the Organization Management account where the AccountPool stack is deployed.</td></tr>
  <tr><td> <b>IDC Account Id</b> </td><td> {{&lt;Requires input&gt;}} </td><td>The AWS Account Id where the IAM Identity Center is configured.</td></tr>
  <tr><td> <b>Allow Listed IP Ranges</b> </td><td>0.0.0.0/1,128.0.0.0/1</td><td>Comma separated list of CIDR ranges that allow access to the API.</td></tr>
  <tr><td> <b>Use Stable Tagging</b> </td><td>Yes</td><td>Automatically use the most up to date and secure account cleaner image up until the next minor release.<br /> <b>Note</b>: Selecting 'No' will pull the image as originally released, without any security updates.</td></tr>
  <tr><td> <b>Accept Solution Terms of Use</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Solution’s terms of use statement for review. The solution will not deploy unless you enter <b>Accept</b> in the parameter field.</td></tr>
  <tr><td> <b>Custom Domain Name</b> </td><td> {{&lt;Optional&gt;}} </td><td>A single fully-qualified domain to serve the solution on (for example, {{isb.example.com}}). If empty, the CloudFront distribution URL is used. No wildcards, scheme, or path. To attach this domain (with TLS) to the CloudFront distribution, also provide <b>Custom Domain Certificate ARN</b>. If you front the solution with your own edge or proxy, set this to your public domain and leave the certificate ARN empty. For details, refer to <a href="custom-domain.md">Configure a custom domain</a>.</td></tr>
  <tr><td> <b>Custom Domain Certificate ARN</b> </td><td> {{&lt;Optional&gt;}} </td><td>The ARN of an existing AWS Certificate Manager (ACM) certificate in the <code>us-east-1</code> Region that covers the <b>Custom Domain Name</b> (a wildcard certificate is supported). Provide this to serve the domain on the CloudFront distribution. Leave empty if you terminate TLS on your own edge or proxy.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, review and choose to acknowledge the messages under Capabilities and transforms, and choose **Next**.

1. On the **Review and create** page, review and confirm the settings.

1. Choose **Submit** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation Console in the Status column. You should receive a **CREATE\_COMPLETE** status in approximately 60 minutes.

**Note**
New deployments of Innovation Sandbox on AWS start with maintenance mode turned **ON**. Only Innovation Sandbox Admin users can use the web application until an Admin completes the post-deployment configuration and turns maintenance mode off. For more information, see [Post-deployment configuration tasks](post-deployment-configuration-tasks.md) and [Managing maintenance mode](administrator-guide.md#maintenance-mode).
