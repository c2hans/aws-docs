---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/get-cell.html
---

# Get a cell
<a name="get-cell"></a>

The following is an example of a request to get a cell, and the response.

```
aws route53-recovery-readiness --region us-west-2 getF-cell \
			--cell-name test-cell
```

```
{
    "CellArn": "arn:aws:route53-recovery-readiness::888888888888:cell/test-cell",
    "CellName": "test-cell",
    "Cells": [],
    "ParentReadinessScopes": [],
    "Tags": {}
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-readiness` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
