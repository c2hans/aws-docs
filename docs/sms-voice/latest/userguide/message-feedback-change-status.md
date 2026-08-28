---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/message-feedback-change-status.html
---

# Change a message feedback status record in AWS End User Messaging SMS
<a name="message-feedback-change-status"></a>

Once you have a signal that a customer has received your message you have to provide feedback for the message by using [PutMessageFeedback](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_PutMessageFeedback.html) or [put-message-feedback](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/put-message-feedback.html). If the message feedback status record isn't updated after one hour it is automatically set to `FAILED` but the CloudWatch metrics are not updated until you set the record as `RECEIVED` or `FAILED`. We recommend that you have a timer to set message feedback status record to `FAILED` if you don't received a signal from your customer.

At the command line, enter the following command:

```
aws pinpoint-sms-voice-v2 --region '{{us-east-1}}' put-message-feedback --message-feedback-status {{Status}} --message-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
+ Replace {{us-east-1}} with the AWS Region that your origination identity is stored in.
+ Replace {{Status}} with `RECEIVED` or `FAILED`.
+ Replace {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} with message id.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
