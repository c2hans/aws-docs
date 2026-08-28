---
source_url: https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-autoscaling.html
---

# Auto scaling with endpoints
<a name="comprehend-autoscaling"></a>

Instead of manually adjusting the number of inference units provisioned for your document classification endpoints and entity recognizer endpoints, you can use auto scaling to automatically set endpoint provisioning to fit your capacity needs.

There are two ways to use auto scaling to adjust the number of inference units provisioned for your endpoint:
+ [Target tracking](targettracking.md): Set auto scaling to adjust endpoint provisioning to fit capacity needs based on usage.
+ [Scheduled scaling](ScheduledScaling.md): Set auto scaling to adjust endpoint provisioning to fit capacity needs on a specified schedule.

You can set auto scaling only with the AWS Command Line Interface (AWS CLI). For more information about auto scaling, see [What is Application Auto Scaling?](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
