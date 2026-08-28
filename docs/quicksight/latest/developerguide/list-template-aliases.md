---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/list-template-aliases.html
---

# ListTemplateAliases
<a name="list-template-aliases"></a>

Use the `ListTemplateAliases` operation to list all the aliases of a template. To use this operation, you need the ID of the template that is using the aliases that you want to list. You can use the `ListTemplates` operation to list all templates and their corresponding template IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-template-aliases
    --aws-account-id {{AWSACCOUNTID}}
    --template-id {{TEMPLATEID}}
    --page-size {{10}}
    --max-items {{100}}
```

------

For more information about the `ListTemplateAliases` operation, see [ListTemplateAliases](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListTemplateAliases) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
