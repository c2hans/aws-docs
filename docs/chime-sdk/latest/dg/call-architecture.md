---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/call-architecture.html
---

# Learn about using Amazon Chime SDK PSTN audio service call legs
<a name="call-architecture"></a>

The PSTN audio service can operate on one or more call legs. For example, you have a single call leg when you record or deliver a voice mail, and you have multiple call legs when you join an Amazon Chime SDK meeting.

The following diagram shows the flow of a single-leg call.

![Diagram of the architecture of a single call leg.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/single-leg-architecture.png)

The following diagram shows the architecture of a multi-leg call.

![Diagram of the architecture of a multi-leg call.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/multi-leg-architecture.png)

The following diagram shows the flow of a multi-leg bridged call.

![Diagram of the architecture of a multi-leg bridged call.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/Multi-Leg-Architecture-w-Bridge.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
