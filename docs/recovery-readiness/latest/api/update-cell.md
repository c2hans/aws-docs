---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/update-cell.html
---

# Update a cell
<a name="update-cell"></a>

The following is an example of a request to update a cell, and the response.

You update a cell by updating its own Cells field. Note that the Cells field takes full Amazon Resource Names (ARNs), not a cell name. In this example, “testcell-child” already existed.

```
aws route53-recovery-readiness --region us-west-2 update-cell \
			--cell-name test-cell \
			--cells arn:aws:route53-recovery-readiness::888888888888:cell/test-cell-child
```

```
{
    "CellArn": "arn:aws:route53-recovery-readiness::888888888888:cell/test-cell",
    "CellName": "test-cell",
    "Cells": [
        "arn:aws:route53-recovery-readiness::888888888888:cell/test-cell-child"
    ],
    "ParentReadinessScopes": [],
    "Tags": {}
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-readiness` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
