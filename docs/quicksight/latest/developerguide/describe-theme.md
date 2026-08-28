---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-theme.html
---

# DescribeTheme
<a name="describe-theme"></a>

Use the `DescribeTheme` operation to describe a theme. To use this operation, you need the ID of the theme that you want to describe. You can use the `ListThemes` operation to list all themes and their corresponding theme IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-theme
    --aws-account-id {{AWSACCOUNTID}}
    --theme-id {{THEMEID}}
    --version-number {{1}}
    --alias-name {{ALIAS}}
```

------

The parameter value for `alias-name` can be `$LATEST`.

For more information about the `DescribeTheme` operation, see [DescribeTheme](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeTheme.html) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
