---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/create-template-alias.html
---

# CreateTemplateAlias
<a name="create-template-alias"></a>

Use the `CreateTemplateAlias` operation to create a template alias for a template. To use this operation, you need the ID of the template that you want to create an alias for. You can use the `ListTemplates` operation to list all templates and their corresponding template IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight create-template-alias
    --aws-account-id {{AWSACCOUNTID}}
    --template-id {{TEMPLATEID}}
    --alias-name {{ALIAS}}
    --template-version-number {{VERSION}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight create-template-alias
    --cli-input-json file://{{createtemplatealias}}.json
```

------

For more information about the `CreateTemplateAlias` operation, see [CreateTemplateAlias](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateTemplateAlias) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
