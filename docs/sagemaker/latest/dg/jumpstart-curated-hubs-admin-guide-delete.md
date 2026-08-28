---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide-delete.html
---

# Delete a private hub
<a name="jumpstart-curated-hubs-admin-guide-delete"></a>

You can delete a private hub from your admin account. Before deleting a private hub, you must first remove any content in that hub. Delete hub contents and hubs with the following commands:

```
# List the model references in the private hub
response = hub.list_models()
models = response["hub_content_summaries"]
while response["next_token"]:
    response = hub.list_models(next_token=response["next_token"])
    models.extend(response["hub_content_summaries"])

# Delete all model references in the hub
for model in models:
    hub.delete_model_reference(model_name=model.get('HubContentName'))

# Delete the private hub
hub.delete()
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
