---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/next-steps.html
---

# Next steps
<a name="next-steps"></a>

You can use DR Orchestrator Framework to add an approval process before initiating the failover or failback activities. For example, while initiating the failover during a DR event, you  can add a state machine on top of `DR Orchestrator Failover` to send an [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/) notification through email. As soon as the approval is granted, the failover activity will start.

Application failover can also be integrated with DR Orchestrator Framework to switch the DNS entry and point applications to the new endpoint of the database instance or cluster.

You can use [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) tracing to obtain the failover duration for calculating the RTO. You can build a monitoring dashboard on top of X-Ray.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
