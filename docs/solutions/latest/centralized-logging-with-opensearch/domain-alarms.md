---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/domain-alarms.html
---

# Domain alarms
<a name="domain-alarms"></a>

Amazon OpenSearch Service provides a set of [recommended CloudWatch alarms](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cloudwatch-alarms.html) to monitor the health of Amazon OpenSearch Service domains. Centralized Logging with OpenSearch helps you to create the alarms automatically, and send a notification to your email (or SMS) via Amazon SNS.

## Create alarms
<a name="create-alarms"></a>

### (Option 1) Using the Centralized Logging with OpenSearch console
<a name="option-1-using-the-centralized-logging-with-opensearch-console"></a>

1. Log in to the Centralized Logging with OpenSearch console.

1. In the navigation pane, under **Domains**, choose **OpenSearch domains**.

1. Select the domain from the table.

1. Under **General configuration**, choose **Enable** at the **Alarms label**.

1. Enter the Email.

1. Choose the alarms that you want to create and adjust the settings if necessary.

1. Choose **Create**.

### (Option 2) Using the CloudFormation stack
<a name="option-2-using-the-cloudformation-stack-1"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - Alarms* solution in the AWS Cloud.

1. Log in to the AWS Management Console and select the button to launch the AWS CloudFormation template. [https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fcentralized-logging-with-opensearch%2Flatest%2FAlarmForOpenSearch.template](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fcentralized-logging-with-opensearch%2Flatest%2FAlarmForOpenSearch.template)

You can also [download the template](https://s3.amazonaws.com/solutions-reference/centralized-logging-with-opensearch/latest/AlarmForOpenSearch.template) as a starting point for your own implementation. . To launch the stack in a different AWS Region, use the Region selector in the console navigation bar. . On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**. . On the **Specify stack details** page, assign a name to your stack. . Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.

\+

| Parameter | Default | Description |
| --- | --- | --- |
| Endpoint |  {{<Requires input>}}  | The endpoint of the OpenSearch domain, for example, `vpc-your_opensearch_domain_name-xcvgw6uu2o6zafsiefxubwuohe.us-east-1.es.amazonaws.com`. |
| DomainName |  {{<Requires input>}}  | The name of the OpenSearch domain. |
| Email |  {{<Requires input>}}  | The notification email address. Alarms will be sent to this email address via Amazon SNS. |
| ClusterStatusRed |  `Yes`  | Whether to enable alarm when at least one primary shard and its replicas are not allocated to a node. |
| ClusterStatusYellow |  `Yes`  | Whether to enable alarm when at least one replica shard is not allocated to a node. |
| FreeStorageSpace |  `10`  | Whether to enable alarm when a node in your cluster is down to the free storage space you entered in GiB. We recommend setting it to 25% of the storage space for each node. 0 means that the alarm is disabled. |
| ClusterIndexWritesBlocked |  `1`  | Index writes blocked error occurs for >= x times in 5 minutes, 1 consecutive time. Input 0 to disable this alarm. |
| UnreachableNodeNumber |  `3`  | Nodes minimum is < x for 1 day, 1 consecutive time. 0 means that the alarm is disabled. |
| AutomatedSnapshotFailure |  `Yes`  | Whether to enable alarm when an automated snapshot failed. AutomatedSnapshotFailure maximum is >= 1 for 1 minute, 1 consecutive time. |
| CPUUtilization |  `Yes`  | Whether to enable alarm when sustained high usage of CPU occurred. CPUUtilization or WarmCPUUtilization maximum is >= 80% for 15 minutes, 3 consecutive times. |
| JVMMemoryPressure |  `Yes`  | Whether to enable alarm when JVM RAM usage peak occurred. JVMMemoryPressure or WarmJVMMemoryPressure maximum is >= 80% for 5 minutes, 3 consecutive times. |
| MasterCPUUtilization |  `Yes`  | Whether to enable alarm when sustained high usage of CPU occurred in master nodes. MasterCPUUtilization maximum is >= 50% for 15 minutes, 3 consecutive times. |
| MasterJVMMemoryPressure |  `Yes`  | Whether to enable alarm when JVM RAM usage peak occurred in master nodes. MasterJVMMemoryPressure maximum is >= 80% for 15 minutes, 1 consecutive time. |
| KMSKeyError |  `Yes`  | Whether to enable alarm when the AWS KMS encryption key is disabled. KMSKeyError is >= 1 for 1 minute, 1 consecutive time. |
| KMSKeyInaccessible |  `Yes`  | Whether to enable alarm when the AWS KMS encryption key has been deleted or has revoked its grants to OpenSearch Service. KMSKeyInaccessible is >= 1 for 1 minute, 1 consecutive time. |

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 5 minutes.

Once you have created the alarms, a confirmation email will be sent to your email address. You must choose the **Confirm** link in the email.

Go to the CloudWatch Alarms page by choosing the **General configuration > Alarms > CloudWatch Alarms** link on the Centralized Logging with OpenSearch console, and the link location is shown as follows:

 **General configuration screen.**

![image31](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image31.png)

Make sure that all the alarms are in **OK** status because you might have missed the notification if the alarms have changed its status before subscription.

**Note**
The alarm will not send an Amazon SNS notification to your email address if triggered before subscription. We recommend you check the alarms status after enabling the OpenSearch alarms. If you see any alarm, which is in **In Alarm** status, you should fix that issue first.

## Delete alarms
<a name="delete-alarms"></a>

1. Log in to the Centralized Logging with OpenSearch console.

1. In the navigation pane, under **Domains**, choose **OpenSearch domains**.

1. Select the domain from the table.

1. Choose the **Alarms** tab.

1. Choose the **Delete**.

1. On the confirmation prompt, choose **Delete**.
