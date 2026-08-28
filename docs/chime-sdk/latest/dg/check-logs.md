---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/check-logs.html
---

# Checking the logs for the Amazon Chime SDK PTSN audio service
<a name="check-logs"></a>

If you're debugging a SIP media application, check the Cloudwatch logs for the AWS Lambda function associated with the application.

Next, check the logs associated with the SIP media application. As needed, you can configure the SIP media application for logging. For more information, see [Using SIP media applications](https://docs.aws.amazon.com/chime-sdk/latest/ag/use-sip-apps.html) in the *Amazon Chime SDK Administrator Guide*. If you enable logging, you can find the logs on Cloudwatch, in the `/aws/ChimeSipMediaApplicationSipMessages/{{<SIP-media-application-Id>}}` log group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
