---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/step-7.-configure-notifications-optional.html
---

# Step 7. Configure notifications (optional)
<a name="step-7.-configure-notifications-optional"></a>

Follow these steps to configure and mute specific notifications for the Quota Monitor solution.

1. Open the [AWS Systems Manager console](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Parameter Store**.

   --Or--

   If the AWS Systems Manager home page opens first, choose the menu icon (![Horizontal black and white striped pattern forming a simple geometric design.](http://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/image4.png)) to open the navigation pane, and then choose **Parameter Store**.

1. On the **My parameters** tab, select the check box next to the parameter to update.

1. Choose **Edit**. Update the **Value**. The value should be comma-separated with no spaces The schema is `ServiceCode[:QuotaCode|QuotaName|Resource]`. Quotas matching that pattern will be muted such that no notification will be sent to the Amazon SNS topic or the Slack web hook. The following is an example:

   ```
   /QuotaMonitor/NotificationConfiguration: ec2:L-1216C47A,ec2:Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances,dynamodb,logs:*,geo:L-05EFD12D.
   ```

   In this example, the following items occur:
   + The quotas `L-1216C47A` and `Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances` from Amazon EC2 are muted.
   + All quotas from the DynamoDB are muted.
   + All quotas from the service logs are muted.
   + The quota `L-05EFD12D` from the service geo is muted.

1. Choose **Save changes**.
**Note**
You can get the values for the service code, quota code, quota name or resource from the notification email or slack message.

## Muting Specific Notifications
<a name="muting-specific-notifications"></a>

If you receive notifications for quotas that are not useful or have very low limits, you can mute these notifications to avoid unnecessary alerts. As an example, this guide will walk you through the process of muting notifications for the `StartAutomationExecution` API in SSM, which has a limit of 1, using the Quota Monitor solution.

 **Identify the Quota to Mute:** The quota in question is Transactions per second (TPS) for the `StartAutomationExecution` API with the limit code `L-99469188`.

 **Update the Notification Configuration:** Follow the steps above to edit the **/QuotaMonitor/NotificationConfiguration** parameter and add `SSM:L-99469188` to the list.

### Identifying Quotas with Limit 1
<a name="identifying-quotas-with-limit-1"></a>

Service quotas in AWS set a limit of 1 for certain resources to provide highly available and reliable service to all customers. These limits are designed to protect customers from unintentional spend and excessive provisioning. There are two ways to identify which quotas have a limit of 1:

 **1. Check the ServiceQuotas Table:** Go to the `SQQuotaTable` DynamoDB table and see the `Value` column for quotas, then sort it.

 **2. Run a Script:** Run this script from our [Github](https://github.com/aws-solutions/quota-monitor-for-aws/blob/main/scripts/listQuotasWithLimitOne.ts) repo to get the list of quotas which have a limit of 1.
