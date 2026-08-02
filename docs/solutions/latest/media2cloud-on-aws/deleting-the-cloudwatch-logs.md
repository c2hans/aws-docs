---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/deleting-the-cloudwatch-logs.html
---

# Deleting the CloudWatch Logs
<a name="deleting-the-cloudwatch-logs"></a>

 This solution retains the CloudWatch Logs if you decide to delete the AWS CloudFormation stack to prevent against accidental data loss. After uninstalling the solution, you can manually delete the logs if you do not need to retain the data. Follow these steps to delete the CloudWatch Logs.

1.  Sign in to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1.  Choose **Log Groups** from the left navigation pane.

1.  Locate the log groups created by the solution.

1.  Select one of the log groups.

1.  Choose **Actions** and then choose **Delete**.

 Repeat the steps until you have deleted all the solution log groups.
