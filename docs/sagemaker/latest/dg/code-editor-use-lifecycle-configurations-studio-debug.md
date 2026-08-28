---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-use-lifecycle-configurations-studio-debug.html
---

# Debug lifecycle configurations in Studio
<a name="code-editor-use-lifecycle-configurations-studio-debug"></a>

To debug lifecycle configuration scripts for Code Editor, you must use Studio. For instructions about debugging lifecycle configurations in Studio, see [Debug lifecycle configurations](jl-lcc-debug.md). To find the logs for a specific application, search the log streams using the following format:

```
{{domain-id}}/{{space-name}}/{{CodeEditor}}/{{default}}/{{LifecycleConfigOnStart}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
