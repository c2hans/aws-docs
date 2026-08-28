---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/list-themes.html
---

# ListThemes
<a name="list-themes"></a>

Use the `ListThemes` operation to list all the themes in the current AWS account.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-themes
    --aws-account-id {{AWSACCOUNTID}}
    --type {{QUICKSIGHT}}
    --page-size {{10}}
    --max-items {{100}}
```

------

For more information about the `ListThemes` operation, see [ListThemes](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListThemes.html) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
