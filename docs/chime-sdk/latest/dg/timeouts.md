---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/timeouts.html
---

# Understanding timeouts and retries for the Amazon Chime SDK PTSN audio service
<a name="timeouts"></a>

The PSTN audio service interacts with AWS Lambda functions synchronously. Applications wait 5 seconds for AWS Lambda functions to respond before retrying an invocation. If no response is received after 20 second the PSTN Audio service will issue a [hang up](unexpected-hangups.md). When a function returns an error with one of the 4*XX* status codes, then by default the SIP media application only retries the invocation once. If you run out of retries, calls terminate with the `480 Unavailable` error code. For more information about AWS Lambda errors, see [Troubleshoot invocation issues in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-invocation.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
