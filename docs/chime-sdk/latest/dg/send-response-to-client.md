---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/send-response-to-client.html
---

# Sending a response to the client for the Amazon Chime SDK
<a name="send-response-to-client"></a>

Once you create the meeting and attendee resources, the server application should encode and send the meeting and attendee objects back to the client application. The client needs those pieces of information to bootstrap the Amazon Chime SDK client library for JavaScript, and enable an attendee to join the meeting successfully from a web or Electron based application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
