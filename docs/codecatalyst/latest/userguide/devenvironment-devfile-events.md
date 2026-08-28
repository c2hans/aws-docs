---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-devfile-events.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Devfile events
<a name="devenvironment-devfile-events"></a>

Currently, CodeCatalyst only supports `postStart` events in your devfile. For more information, see [postStartObject](https://devfile.io/docs/2.0.0/adding-event-bindings#post-start-object) in the Devfile.io documentation.

The following example shows you how to add `postStart` event bindings in your devfile.

```
commands:
  - id: executescript
    exec:
      component: test
      commandLine: "./projects/devfiles/script.sh"
  - id: updateyum
    exec:
      component: test
      commandLine: "yum -y update --security"
events:
  postStart:
    - updateyum
    - executescript
```

After startup, your Dev Environment will execute the specified `postStart` commands in the order they are defined. If a command fails, the Dev Environment will continue running and the execution output is stored in the logs under `/aws/mde/logs`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
