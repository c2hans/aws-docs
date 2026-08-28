---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide-delete-models.html
---

# Delete models from a private hub
<a name="jumpstart-curated-hubs-admin-guide-delete-models"></a>

You can delete models from a private hub used by your organization by specifying the model ARN in the `hub.delete_model_reference()` method. This removes access to the model from the private hub.

```
hub.delete_model_reference({{model-name}})
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
