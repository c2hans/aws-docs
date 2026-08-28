---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-analysis.html
---

# DeleteAnalysis
<a name="delete-analysis"></a>

Use the `DeleteAnalysis` API operation to delete an analysis from Amazon Quick Sight for a specified user. To use this operation, you need the ID of the analysis that you want to delete. The analysis ID is part of the analysis URL in Quick Sight. You can also use the `ListAnalyses` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-analysis
    --aws-account-id {{555555555555}}
    --analysis-id {{{{ANALYSISID}}}}
```

------

For more information about the `DeleteAnalysis` API operation, see [DeleteAnalysis](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteAnalysis.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
