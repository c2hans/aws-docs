---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/step3-deploy-data-stack.html
---

# Step 3: Deploy the Data stack

In this step, you deploy the data resources required for the ISB application.

**Important**
Ensure that you are logged in using the **Hub** account for deploying the Data stack.

1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/) and choose the button to launch the `Data` stack CloudFormation template.

 [![Launch Stack](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?&templateURL=https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-Data.template&redirectId=ImplementationGuide)

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
  <tr><td> <b>SAML Metadata URL</b> </td><td> <i>(none)</i> </td><td>The metadata URL of the IAM Identity Center SAML 2.0 application you created in <a href="create-saml-app.md">Create a SAML 2.0 application</a>. Amazon Cognito uses this URL to federate authentication to IAM Identity Center. Required.</td></tr>
  <tr><td> <b>AWS Access Portal URL</b> </td><td> <i>(none)</i> </td><td>The IAM Identity Center access portal URL. The solution uses this to generate direct links to sandbox accounts in the web UI. Find it on the IAM Identity Center console <b>Dashboard</b> under <b>Settings summary</b>. If you change this value after deployment, update the Compute stack with a new <b>Force configuration update (optional)</b> value. For instructions, see <a href="#update-access-portal-url">Change the AWS access portal URL after deployment</a>.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, review and choose to acknowledge the messages under Capabilities and transforms, and choose **Next**.

1. On the **Review and create** page, review and confirm the settings.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation Console in the Status column. You should receive a **CREATE\_COMPLETE** status in approximately 60 minutes.

## Change the AWS access portal URL after deployment
<a name="update-access-portal-url"></a>

The Compute stack reads the **AWS Access Portal URL** from the Data stack when it deploys. After you change the URL, update both stacks:

1. Sign in to the Hub account, and open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Update the Data stack, and choose **Use existing template**.

1. Change **AWS Access Portal URL**.

1. Wait until the Data stack reaches `UPDATE_COMPLETE`.

1. Update the Compute stack and choose **Use existing template**. Preserve its other parameter values.

1. Set **Force configuration update (optional)** to any string different from its current value.

1. Wait until the Compute stack reaches `UPDATE_COMPLETE`.

1. Open the web UI, and confirm that the sandbox account links use the new access portal URL.

**Note**
The shared-configuration resolver can cache the previous Data stack configuration for up to five minutes. If the web UI still shows the previous URL, wait until five minutes have passed since the Compute update. Then update the Compute stack again with another new **Force configuration update (optional)** value.
