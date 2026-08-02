---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/create-cell.html
---

# Create a cell
<a name="create-cell"></a>

The following is an example of a request to create a cell, and the response.

```
aws route53-recovery-readiness --region us-west-2 create-cell \
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
