---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_ConnectAction.html
---

# ConnectAction
<a name="API_ConnectAction"></a>

When included in a receipt rule, this action parses the received message and starts an email contact in Amazon Connect on your behalf.

**Note**
When you receive emails, the maximum email size (including headers) is 40 MB. Additionally, emails may only have up to 10 attachments. Emails larger than 40 MB or with more than 10 attachments will be bounced.

We recommend that you configure this action via Amazon Connect.

## Contents
<a name="API_ConnectAction_Contents"></a>

 ** IAMRoleARN **
 The Amazon Resource Name (ARN) of the IAM role to be used by Amazon Simple Email Service while starting email contacts to the Amazon Connect instance. This role should have permission to invoke `connect:StartEmailContact` for the given Amazon Connect instance.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w-]+:iam::[0-9]+:role/[\w-]+`
Required: Yes

 ** InstanceARN **
The Amazon Resource Name (ARN) for the Amazon Connect instance that Amazon SES integrates with for starting email contacts.
For more information about Amazon Connect instances, see the [Amazon Connect Administrator Guide](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-instances.html)
Type: String
Pattern: `arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9-]{1}:[0-9]{1,20}:instance/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## See Also
<a name="API_ConnectAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/ConnectAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/ConnectAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/ConnectAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
