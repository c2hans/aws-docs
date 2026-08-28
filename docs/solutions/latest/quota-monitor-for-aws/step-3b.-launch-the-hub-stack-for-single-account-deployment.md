---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/step-3b.-launch-the-hub-stack-for-single-account-deployment.html
---

# Step 3b. Launch the hub stack for single account deployment
<a name="step-3b.-launch-the-hub-stack-for-single-account-deployment"></a>

1. Sign in to the AWS Management Console and select the button to launch the `quota-monitor-hub-no-ou.template` CloudFormation template.

    [![launch button](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fquota-monitor-for-aws%2Flatest%2Fquota-monitor-hub-no-ou.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch the solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
You can launch this template in any AWS Region.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box, and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameter for the template and modify it as necessary. This solution uses the following default values.

| Parameter | Default | Description |
| --- | --- | --- |
|  **Email Notification**  |  *<Optional input>*  | Provide an email address to receive alert notifications. |
|  **Slack Notification**  |  `No`  | Choose `Yes` if you want to receive Slack notifications for quota utilization alerts. |
|  **Report OK Notifications**  |  `No`  | Whether to save the `OK` notiﬁcations in the summary table on the hub account. |

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template will create IAM resources.

1. Choose **Create stack** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation Console in the **Status** column. You should see a status of CREATE\_COMPLETE in approximately five minutes.

1. After the stack deploys, update the `/QuotaMonitor/Accounts` Systems Manager Parameter Store with list of targeted accounts. Once the parameter is updated:
   + The `helper` Lambda function updates the permissions on the centralized EventBridge bus so that all monitored accounts can send their quota utilization events to the primary account.
   + You can deploy `quota-monitor-ta-spoke` and `quota-monitor-sq-spoke` templates in the monitored accounts manually. Refer to [Step 6: Launch the spoke stacks](step-6.-launch-the-spoke-stacks-optional.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quota Monitor for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
