---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/launch-the-stack.html
---

# Launch the stack
<a name="launch-the-stack"></a>

Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

If you previously deployed MCS in the same account, confirm that your previous stack uninstalled successfully. Follow the steps described in the [Uninstall the solution](uninstall-the-solution.md) and [Troubleshooting](troubleshooting.md) and sections to disable the MCS modules and de-register the Third-Party modules.

 **Time to deploy:** Approximately 7-10 minutes

1. Sign into [AWS Management Console](https://aws.amazon.com/console) and select the button to launch `ModularCloudStudioOnAwsStack.template` CloudFormation template. [![Launch solution](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=modular-cloud-studio&templateURL=https://solutions-reference.s3.amazonaws.com/modular-cloud-studio-on-aws/latest/ModularCloudStudioOnAwsStack.template?redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different Region, use the Region selector in the console navigation bar.
**Note**
This solution is not currently available in all AWS Regions. You must launch this solution in an AWS Region where the solution is available. See [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions) for more information.

1. On the **Create stack** page, verify that the correct template URL is in the **Amazon S3 URL** text box and choose **Next.**

1. On the **Specify stack details** page, assign a name to your solution stack. For information about naming character limitations, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the *AWS Identity and Access Management User Guide*.

1. Under **Parameters**, review the parameters for this solution template and modify them as necessary. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/launch-the-stack.html)

1. Select **Next**

1. On the **Configure stack options** page, ensure that 10 or fewer tags are configured. You can auto-apply these main solution stack tags to all the modules. You can also review and remove them when you deploy each module.

1. Choose **Next**.

1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template creates IAM resources.

1. Choose **Next**.

1. Choose Submit to deploy the stack. You can view the status of the stack in the AWS CloudFormation console in the Status column. You should receive a CREATE\_COMPLETE status in approximately 7 minutes.

1. After the stack in CloudFormation is successfully created, select the stack that you created. Then navigate to the **Outputs** tab and find the MCS web console URL defined in **CloudFrontURL**.

1. You will receive an email with a temporary password to access the MCS web console. You must reset the password on your first login following the prompt. If you haven’t received an email after the stack deployment is completed, check your spam folder.

1. You can add MCS web console users by navigating to the MCS user pool in the [Amazon Cognito console](https://console.aws.amazon.com/cognito/), and clicking **Create user** under Users from the left navigation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
