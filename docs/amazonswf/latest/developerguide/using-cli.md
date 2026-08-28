---
source_url: https://docs.aws.amazon.com/amazonswf/latest/developerguide/using-cli.html
---

# Using the AWS CLI with Amazon Simple Workflow Service
<a name="using-cli"></a>

Many of the features of Amazon Simple Workflow Service can be accessed from the AWS CLI. The AWS CLI provides an alternative to using Amazon SWF with the AWS Management Console or in some cases, to programming with the Amazon SWF API and the AWS Flow Framework.

For example, you can use the AWS CLI to register a new workflow type:

```
aws swf register-workflow-type --domain {{MyDomain}} --name {{"MySimpleWorkflow"}} --workflow-version {{"v1"}}
```

You can also list your registered workflow types:

```
aws swf list-workflow-types --domain {{MyDomain}} --registration-status {{REGISTERED}}
```

The following shows an example of the default output in JSON:

```
{
    "typeInfos": [
        {
            "status": "REGISTERED",
            "creationDate": 1377471607.752,
            "workflowType": {
                "version": "v1",
                "name": "MySimpleWorkflow"
            }
        },
        {
            "status": "REGISTERED",
            "creationDate": 1371454149.598,
            "description": "MyDomain subscribe workflow",
            "workflowType": {
                "version": "v3",
                "name": "subscribe"
            }
        }
    ]
}
```

The Amazon SWF commands in AWS CLI provide the ability to start and manage workflow executions, poll for activity tasks, record task heartbeats, and more\! For a complete list of Amazon SWF commands, with descriptions of the available arguments and examples showing their use, see [Amazon SWF](https://docs.aws.amazon.com/cli/latest/reference/swf/index.html) commands in the *AWS CLI Command Reference*.

The AWS CLI commands follow the Amazon SWF API closely, so you can use the AWS CLI to learn about the underlying Amazon SWF API. You can also use your existing API knowledge to prototype code or perform Amazon SWF actions on the command line.

To learn more about the AWS CLI, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
