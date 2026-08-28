---
source_url: https://docs.aws.amazon.com/amazonswf/latest/awsflowguide/daemontasks.html
---

# Daemon Tasks
<a name="daemontasks"></a>

The AWS Flow Framework for Java allows the marking of certain tasks as `daemon`. This allows you to create tasks that do some background work that should get canceled when all other work is done. For example, a health monitoring task should be canceled when the rest of the workflow is complete. You can accomplish this by setting the `daemon` flag on an asynchronous method or an instance of `TryCatchFinally`. In the following example, the asynchronous method `monitorHealth()` is marked as `daemon`.

```
public class MyWorkflowImpl implements MyWorkflow {
  MyActivitiesClient activitiesClient = new MyActivitiesClientImpl();

  @Override
  public void startMyWF(int a, String b) {
    activitiesClient.doUsefulWorkActivity();
    monitorHealth();
  }

  @Asynchronous(daemon=true)
  void monitorHealth(Promise<?>... waitFor) {
    activitiesClient.monitoringActivity();
  }
}
```

In the above example, when `doUsefulWorkActivity` completes, `monitoringHealth` will be automatically canceled. This will in turn cancel the whole execution branch rooted at this asynchronous method. The semantics of cancellation are the same as in `TryCatchFinally`. Similarly, you can mark a `TryCatchFinally` daemon by passing a Boolean flag to the constructor.

```
public class MyWorkflowImpl implements MyWorkflow {
    MyActivitiesClient activitiesClient = new MyActivitiesClientImpl();

    @Override
    public void startMyWF(int a, String b) {
        activitiesClient.doUsefulWorkActivity();
        new TryFinally(true) {
            @Override
            protected void doTry() throws Throwable {
                activitiesClient.monitoringActivity();
            }

            @Override
            protected void doFinally() throws Throwable {
                // clean up
            }
        };
    }
}
```

A daemon task started within a `TryCatchFinally` is scoped to the context it is created in—that is, it will be scoped to either the `doTry()`, `doCatch()`, or `doFinally()` methods. For example, in the following example the startMonitoring asynchronous method is marked daemon and called from `doTry()`. The task created for it will be canceled as soon as the other tasks (`doUsefulWorkActivity` in this case) started within `doTry()` are complete.

```
public class MyWorkflowImpl implements MyWorkflow {
    MyActivitiesClient activitiesClient = new MyActivitiesClientImpl();

    @Override
    public void startMyWF(int a, String b) {
        new TryFinally() {
            @Override
            protected void doTry() throws Throwable {
                activitiesClient.doUsefulWorkActivity();
                startMonitoring();
            }

            @Override
            protected void doFinally() throws Throwable {
                // Clean up
            }
        };
    }

    @Asynchronous(daemon = true)
    void startMonitoring(){
      activitiesClient.monitoringActivity();
    }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
