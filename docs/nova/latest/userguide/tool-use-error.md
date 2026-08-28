---
source_url: https://docs.aws.amazon.com/nova/latest/userguide/tool-use-error.html
---

# Reporting an error
<a name="tool-use-error"></a>

There are some instances where the parameters selected by Amazon Nova can cause an external error. It can be beneficial then to communicate this back to Amazon Nova so the request can be modified and retried. To notify about errors, still return a tool result but modify the status to report the error and share the exception message.

Here is an example that reports an error status message:

```
tool_result_message = {
    "role": "user",
    "content": [
        {
            "toolResult": {
                "toolUseId": tool["toolUseId"],
                "content": [{"text": "A validation exception occured on field: sample.field"}],
                "status": "error"
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
