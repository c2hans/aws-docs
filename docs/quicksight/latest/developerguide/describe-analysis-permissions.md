---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-analysis-permissions.html
---

# DescribeAnalysisPermissions
<a name="describe-analysis-permissions"></a>

Use the `DescribeAnalysisPermissions` API operation to view the read and write permissions for an analysis. To use this operation, you need the ID of the analysis whose permissions you want to view. The analysis ID is part of the analysis URL in Quick Sight. You can also use the `ListAnalyses` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-analysis-permissions
    --aws-account-id {{555555555555}}
    --analysis-id {{ANALYSISID}}
```

------

For more information about the `DescribeAnalysisPermissions` API operation, see [DescribeAnalysisPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAnalysisPermissions.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
