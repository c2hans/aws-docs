---
source_url: https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-run-workflows.html
---

# Running workflows in Amazon SWF
<a name="swf-dev-run-workflows"></a>

After the coordination logic and the activities have been designed, you register these components as workflow and activity types with Amazon SWF. During registration, you specify a name, a version, and default configuration values for each type.

Only registered workflow and activity types can be used with Amazon SWF. In the e-commerce example, you would register the CustomerOrder workflow type and the VerifyOrder, ChargeCreditCard, ShipOrder, and RecordCompletion activity types.

After registering your workflow type, you can run it as often you like. A *workflow execution* is a running instance of a workflow.

A workflow execution can be started by any process or application, even another workflow execution. In the e-commerce example, a new workflow execution is started with each customer order. The type of application that initiates the workflow depends on how the customer places the order. The workflow could be initiated by a web site or mobile application or by a customer service representative using an internal company application.

With Amazon SWF, you can associate an identifier—called a `workflowId`—with your workflow executions, so you can integrate your existing business identifiers into your workflow. In the e-commerce example, each workflow execution might be identified using the customer invoice number.

In addition to the identifier that you provide, Amazon SWF associates a unique system-generated identifier—a `runId`—with each workflow execution. Amazon SWF allows only one workflow execution with this identifier to run at any given time; although you can have multiple workflows executions of the same workflow type, each workflow execution has a distinct `runId`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
