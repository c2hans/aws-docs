---
source_url: https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-timers.html
---

# Timers in Amazon SWF
<a name="swf-dg-timers"></a>

With a timer, you can notify your decider when a certain amount of time has elapsed.

When responding to a decision task, the decider has the option to respond with a `StartTimer` decision. This decision specifies an amount of time after which the timer should fire. After the specified time has elapsed, Amazon SWF will add a `TimerFired` event to the workflow execution history and schedule a decision task. The decider can then use this information to inform further decisions. One common application for a timer is to delay the execution of an activity task. For example, a customer might want to take delayed delivery of an item.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
