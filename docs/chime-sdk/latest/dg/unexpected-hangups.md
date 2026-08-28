---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-hangups.html
---

# Debugging unexpected hangups in the Amazon Chime SDK PTSN audio service
<a name="unexpected-hangups"></a>

Complete the following troubleshooting actions if you experience unexpected hangups or error messages with AWS Lambda functions for the PSTN audio service:
+ Verify that your AWS Lambda policy grants the `lambda:InvokeFunction` permission to the [voiceconnector.chime.amazonaws.com](http://voiceconnector.chime.amazonaws.com/) service principal.
+ Check the logs for your AWS Lambda function to ensure that it's being successfully invoked.
+ If the logs show incoming events and returned actions, verify that you don't return a hangup action in when the AWS Lambda function is invoked.
+ Check the CloudWatch logs for your SIP media application. The following table lists some of the messages you may encounter.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-hangups.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
