---
source_url: https://docs.aws.amazon.com/amazonswf/latest/awsflowguide/awsflow-basics-data-exchange-workflows-application.html
---

# AWS Flow Framework Basic Concepts: Data Exchange Between Applications and Workflow Executions
<a name="awsflow-basics-data-exchange-workflows-application"></a>

A workflow entry point method can have one or more parameters, which allows the workflow starter to pass initial data to the workflow. It can also useful to provide additional data to the workflow during execution. For example, if a customer changes their shipping address, you could notify the order-processing workflow so that it can make appropriate changes.

Amazon SWF allows workflows to implement a *signal* method, which allows applications such as the workflow starter to pass data to the workflow at any time. A signal method can have any convenient name and parameters. You designate it as a signal method by including it in your workflow interface definition, and applying a `@Signal` annotation to the method declaration.

The following example shows an order processing workflow interface that declares a signal method, `changeOrder`, which allows the workflow starter to change the original order after the workflow has started.

```
@Workflow
@WorkflowRegistrationOptions(defaultExecutionStartToCloseTimeoutSeconds = 300)
public interface WaitForSignalWorkflow {
    @Execute(version = "1.0")
    public void placeOrder(int amount);
    @Signal
    public void changeOrder(int amount);
}
```

The framework's annotation processor creates a workflow client method with the same name as the signal method and the workflow starter calls the client method to pass data to the workflow. For an example, see [AWS Flow Framework Recipes](https://aws.amazon.com/code/2535278400103493)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
