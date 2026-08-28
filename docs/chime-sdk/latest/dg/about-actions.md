---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/about-actions.html
---

# Understanding Amazon Chime SDK PSTN audio service actions
<a name="about-actions"></a>

In the PSTN audio service, SIP media applications trigger AWS Lambda functions. In turn, the AWS Lambda functions can return a list of instructions known as *actions*. An action is an item that you want to run on a leg of a phone call, such as sending or receiving digits, joining a meeting, and so on. Actions can also return data, so you can think of actions as objects with data fields. For more information about the actions invoked by the PSTN audio service, see [Understanding telephony events for Amazon Chime SDK PSTN audio service](pstn-invocations.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
