---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-analysis.html
---

# DescribeAnalysis
<a name="describe-analysis"></a>

Use the `DescribeAnalysis` API operation to view a summary of the metadata for an analysis for a specified user. To use this operation, you need the ID of the analysis that you want to describe. The analysis ID is part of the analysis URL in Quick Sight. You can also use the `ListAnalyses` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-analysis
    --analysis-id {{{{ANALYSISID}}}}
    --aws-account-id {{555555555555}}
```

------

For more information about the `DescribeAnalysis` API operation, see [DescribeAnalysis](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAnalysis.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
