---
source_url: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-run-lambda-schedule.html
---

# Tutorial: Schedule a AWS Lambda function
<a name="eb-run-lambda-schedule"></a>

**Note**
Scheduled rules are a legacy feature of EventBridge.
EventBridge offers a more flexible and powerful way to create, run, and manage scheduled tasks centrally, at scale: EventBridge Scheduler. With EventBridge Scheduler, you can create schedules using cron and rate expressions for recurring patterns, or configure one-time invocations. You can set up flexible time windows for delivery, define retry limits, and set the maximum retention time for failed API invocations.
Scheduler is highly customizable, and offers improved scalability over scheduled rules, with a wider set of target API operations and AWS services. We recommend that you use Scheduler to invoke targets on a schedule.
For more information, see [Create a schedule](using-eventbridge-scheduler.md#using-eventbridge-scheduler-create) or the *[EventBridge Scheduler User Guide](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html)*.

This tutorial previously demonstrated how to invoke a Lambda function on a schedule using EventBridge scheduled rules. We now recommend using Amazon EventBridge Scheduler instead. EventBridge Scheduler offers improved scalability, a wider set of target API operations, flexible time windows, and built-in retry and dead-letter queue support.

For a complete walkthrough of scheduling a Lambda function using EventBridge Scheduler, see [Invoke a Lambda function on a schedule](https://docs.aws.amazon.com/lambda/latest/dg/with-eventbridge-scheduler.html) in the *AWS Lambda Developer Guide*.

For more information about EventBridge Scheduler, including how to create schedules using the console, AWS CLI, or SDKs, see the [Amazon EventBridge Scheduler User Guide](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html).

If you still need to use EventBridge scheduled rules, see [Creating a scheduled rule (legacy) in Amazon EventBridge](eb-create-rule-schedule.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
