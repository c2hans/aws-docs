---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/load-balancer-stickiness/options.html
---

# Which stickiness strategy is right for you?
<a name="options"></a>

Answering the following questions will help you determine your load balancer stickiness strategy.** **

**Are you using WebSockets?**
+ Yes: WebSockets are inherently sticky, so there is no need to use any strategy.
+ No: Continue to the next question.

**Are you planning a blue/green deployment?**
+ Yes: At the minimum, use target group stickiness, but continue to the next question.
+ No: Continue to the next question.

**Do you need some or all the traffic from a client to be routed to the same EC2 instance repeatedly?**
+ Yes: Continue to the next question.
+ No: You do not need to use sticky sessions.

**Do you want your application code or client to control the state attributes and duration by using cookies?**
+ Yes: Use application-based cookies to enable application-based sticky sessions.
+ No: Use load balancer generated cookies to enable duration-based sticky sessions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
