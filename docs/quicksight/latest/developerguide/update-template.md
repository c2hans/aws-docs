---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/update-template.html
---

# UpdateTemplate
<a name="update-template"></a>

Use the `UpdateTemplate` operation to update a template from an existing Quick Sight analysis or another template.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight update-template
    --aws-account-id {{555555555555}}
    --template-id {{TEMPLATEID}}
    --source-entity {{SOURCEENTITY}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-template
    --cli-input-json file://{{updatetemplate}}.json
```

------

For more information about the `UpdateTemplate` operation, see [UpdateTemplate](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTemplate.html) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
