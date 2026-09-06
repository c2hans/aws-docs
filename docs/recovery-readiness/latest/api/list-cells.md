---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/list-cells.html
---

# List cells for an account
<a name="list-cells"></a>

The following is an example of a request to list the cells in an account, and the response.

```
aws route53-recovery-readiness --region us-west-2 list-cells
```

```
{
    "Cells": [
        {
            "CellArn": "arn:aws:route53-recovery-readiness::888888888888:cell/test-cell",
            "CellName": "test-cell",
            "Cells": [],
            "ParentReadinessScopes": [],
            "Tags": {}
        }
    ]
}
```
