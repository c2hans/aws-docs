---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/create-theme-alias.html
---

# CreateThemeAlias
<a name="create-theme-alias"></a>

The `CreateThemeAlias` operation creates a theme alias for a theme. To use this operation, you need the ID of the theme that you want to create an alias for. You can use the `ListThemes` operation to list all themes and their corresponding theme IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight
    --aws-account-id {{AWSACCOUNTID}}
    --theme-id {{THEMEID}}
    --alias-name {{ALIAS}}
    --theme-version-number {{VERSION}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight create-theme-alias
    --cli-input-json file://{{create-theme-alias}}.json
```

------

For more information about the `CreateThemeAlias` operation, see [CreateThemeAlias](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateThemeAlias) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
