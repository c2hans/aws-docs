---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/iot-events-alarm-notification-requirements.html
---

# Requirements for alarm notifications in AWS IoT SiteWise
<a name="iot-events-alarm-notification-requirements"></a>

AWS IoT Events uses an AWS Lambda function in your AWS account to send alarm notifications. You must create this Lambda function in the same AWS Region as your alarms to enable alarm notifications. This Lambda function uses [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) to send text notifications and [Amazon Simple Email Service (Amazon SES)](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html) to send email notifications. When you create the AWS IoT Events alarm, you configure the protocols and settings that the alarm uses to send notifications.

**Note**
End of support notice: AWS ended support for AWS IoT Events. For more information, see [AWS IoT Events end of support](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-end-of-support.html).

AWS IoT Events provides an AWS CloudFormation stack template that you can use to create this Lambda function in your account. For more information, see [Alarm notification Lambda function](https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html) in the *AWS IoT Events Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
