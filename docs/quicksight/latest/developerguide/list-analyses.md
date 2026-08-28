---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/list-analyses.html
---

# ListAnalyses
<a name="list-analyses"></a>

Use the `ListAnalyses` API operation to list Amazon Quick Sight analyses that exist in the specified AWS account. Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-analyses
    --aws-account-id {{555555555555}}
    --page-size {{10}}
    --max-items {{10}}
```

------

For more information about the `ListAnalyses` API operation, see [ListAnalyses](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListAnalyses.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
