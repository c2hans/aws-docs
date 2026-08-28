---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/step-3a.-launch-the-hub-stack-for-aws-organizations.html
---

# Step 3a. Launch the hub stack for AWS Organizations
<a name="step-3a.-launch-the-hub-stack-for-aws-organizations"></a>

This CloudFormation template deploys the Quota Monitor for AWS into your primary account.

**Note**
This template must be launched in a member account of your Organizations that is registered as delegated administrator for StackSets.
You are responsible for the cost of the AWS services used while running this solution. Review the [Cost](cost.md) section for more details. For full details, refer to the pricing webpage for each AWS service you will be using in this solution.

1. Sign in to the AWS Management Console and select the button to launch the `quota-monitor-hub.template` CloudFormation template.

    [![launch button](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fquota-monitor-for-aws%2Flatest%2Fquota-monitor-hub.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
You can launch this template in any AWS Region.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/step-3a.-launch-the-hub-stack-for-aws-organizations.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Create stack** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation Console in the **Status** column. You should see a status of CREATE\_COMPLETE in approximately five minutes.

1. In the subscription notification email, select the **SubscribeURL** link to turn on Amazon SNS email notifications.
   + Customizing SageMaker and Amazon Connect services monitoring \*

Because monitoring SageMaker and Amazon Connect services can incur high costs, this solution allows you to enable or disable monitoring for these services at the hub template level. This setting applies to all spoke accounts in your deployment.

To change these settings:

1. Update the hub stack in CloudFormation.

1. Modify the **SageMaker Monitoring** and **Connect Monitoring** parameters as needed.

1. Apply the stack update.

**Note**
Changing these parameters during a stack update affects all spoke accounts. If you leave them unchanged, the existing monitoring customizations in the spoke accounts remain intact.
For spoke account-specific customization, you can modify the monitoring status in their Service DynamoDB table after deployment. The table includes entries for each service, such as SageMaker and Amazon Connect, with a **Monitored** field that can be set to `true` or `false`.

**Important**
Steps 4a and 4b are critical for the solution to function correctly. Without updating these, the solution won’t know which accounts, OUs, or Regions to monitor.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quota Monitor for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
