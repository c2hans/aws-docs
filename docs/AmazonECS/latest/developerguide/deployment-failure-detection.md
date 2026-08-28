---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-failure-detection.html
---

# Amazon ECS deployment failure detection
<a name="deployment-failure-detection"></a>

Amazon ECS provides two methods for detecting deployment failures:
+ Deployment Circuit Breaker
+ CloudWatch Alarms

You can configure both methods to automatically roll back failed deployments to the last known good state.

Consider the following:
+ Both methods only support rolling update deployment and blue/green deployment types.
+ When both methods are used, either can trigger deployment failure.
+ The rollback method requires a previous deployment in COMPLETED state.
+ EventBridge events are generated for deployment state changes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
