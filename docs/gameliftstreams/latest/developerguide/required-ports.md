---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/required-ports.html
---

# Required ports
<a name="required-ports"></a>

 To integrate Amazon GameLift Streams, ensure that your network infrastructure has the necessary ports open and accessible. The following is a list of the ports you should plan to have open on your network to communicate with Amazon GameLift Streams.

| Port | Protocol | Purpose |
| --- | --- | --- |
| 443 | (HTTPS) TCP | AWS APIs, including Amazon GameLift Streams |
| 33435-33465 | UDP | Web RTC |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
