---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-template.html
---

# DeleteTemplate
<a name="delete-template"></a>

Use the `DeleteTemplate` operation to delete a template. To use this operation, you need the ID of the template that you want to delete. You can use the `ListTemplates` operation to list all templates and their corresponding template IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-template
    --aws-account-id {{AWSACCOUNTID}}
    --template-id {{TEMPLATEID}}
```

------

For more information about the `DeleteTemplate` operation, see [DeleteTemplate](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteTemplate.html) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
