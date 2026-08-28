---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/theme-alias-operations.html
---

# Theme alias operations
<a name="theme-alias-operations"></a>

A *theme alias* is a reference to a version of a theme. For example, suppose that you create the theme alias `{{exampleAlias}}` for version 1 of the theme `exampleTheme`. You can use the theme alias {{`exampleAlias`}} to reference version 1 of theme exampleTheme in a `DescribeTheme` API operation, as in the following example.

**Example**

```
aws quicksight describe-theme
    --aws-account-id {{AWSACCOUNTID}}
    --theme-id {{exampleThemeID}}
    --alias-name {{exampleAlias}}
```

With theme alias operations, you can perform actions on Quick Sight theme aliases. For more information, see the following API operations.

**Topics**
+ [CreateThemeAlias](create-theme-alias.md)
+ [DeleteThemeAlias](delete-theme-alias.md)
+ [DescribeThemeAlias](describe-theme-alias.md)
+ [ListThemeAliases](list-theme-aliases.md)
+ [UpdateThemeAlias](update-theme-alias.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
