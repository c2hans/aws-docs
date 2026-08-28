---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

With AWS Step Functions, you can create workflows, also called *state machines*, to build distributed applications, automate processes, orchestrate microservices, and create data and machine learning pipelines.

Through the Step Functions API, you can create, list, update, and delete state machines, activities, and other data types. You can start, stop, and redrive your state machines. Your activity workers can send task success, heartbeat, and failure responses.

With API calls, you can also manage other aspects of your workflow, such as tags, versions, and aliases.

For more information about developing solutions with Step Functions, see the * [AWS Step Functions Developer Guide](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) *.

**Important**
If you use the Step Functions API actions using AWS SDK integrations, make sure the API actions are in camel case and parameter names are in Pascal case. For example, you might use Step Functions API action `startSyncExecution` and specify its parameter as `StateMachineArn`.

This document was last published on August 28, 2026.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
