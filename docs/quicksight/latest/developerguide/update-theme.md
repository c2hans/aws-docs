---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/update-theme.html
---

# UpdateTheme
<a name="update-theme"></a>

Use the `UpdateTheme` operation to update a theme.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight update-theme
    --aws-account-id {{555555555555}}
    --theme-id {{THEMEID}}
    --base-theme-id {{BASETHEMEID}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-theme
    --cli-input-json file//:{{updatetheme}}.json
```

------

For more information about the `UpdateTheme` operation, see [UpdateTheme](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTheme.html) in the*Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
