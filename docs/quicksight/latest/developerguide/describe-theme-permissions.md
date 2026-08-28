---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-theme-permissions.html
---

# DescribeThemePermissions
<a name="describe-theme-permissions"></a>

Use the `DescribeThemePermissions` operation to describe the read and write permissions for a theme. To use this operation, you need the ID of the theme that you want to describe. You can use the `ListThemes` operation to list all themes and their corresponding theme IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-theme-permissions
    --aws-account-id {{AWSACCOUNTID}}
    --theme-id {{THEMEID}}
```

------

For more information about the `UpdateThemePermissions` operation, see [UpdateThemePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateThemePermissions.html) in the*Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
