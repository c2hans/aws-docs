---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor-use-lifecycle-configurations-studio-detach.html
---

# Detach lifecycle configurations in Studio
<a name="code-editor-use-lifecycle-configurations-studio-detach"></a>

To detach lifecycle configurations for Code Editor, you can use either the console or the AWS CLI. For steps on detaching lifecycle configurations from the Studio console, see [Detach lifecycle configurations](jl-lcc-delete.md).

To detach a lifecycle configuration using the AWS CLI, remove the desired lifecycle configuration from the list of lifecycle configurations attached to the resource. Then pass the list as part of the respective command:
+ [update-user-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-user-profile.html)
+ [update-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html)

For example, the following command removes all lifecycle configurations for the Code Editor application attached to the domain.

```
aws sagemaker update-domain --domain-id {{domain-id}} \
--default-user-settings '{
"CodeEditorAppSettings": {
  "LifecycleConfigArns":
    []
  }
}'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
