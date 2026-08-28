---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-template-alais.html
---

# DeleteTemplateAlias
<a name="delete-template-alais"></a>

Use the `DeleteTemplateAlias` operation to delete the item that the specified template alias points to. If you provide a specific alias, you delete the version of the template that the alias points to. To use this operation, you need the ID of the template that is using the alias you want to delete. You can use the `ListTemplates` operation to list all templates and their corresponding template IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-template-alias
    --aws-account-id {{AWSACCOUNTID}}
    --template-id {{TEMPLATEID}}
    --alias-name {{ALIAS}}
```

------

For more information about the `DeleteTemplateAlias` operation, see [DeleteTemplateAlias](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteTemplateAlias) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
