---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/list-template-versions.html
---

# ListTemplateVersions
<a name="list-template-versions"></a>

Use the `ListTemplateVersions` operation to list all the versions of the templates in the current Quick Sight account. To use this operation to list the versions of a template, you need that template's ID. You can use the `ListTemplates` operation to list all templates and their corresponding template IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-template-versions
    --aws-account-id {{AWSACCOUNTID}}
    --template-id {{TEMPLATEID}}
    --page-size {{10}}
    --max-items {{100}}
```

------

For more information about the `ListTemplateVersions` operation, see [ListTemplateVersions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListTemplateVersions.html) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
