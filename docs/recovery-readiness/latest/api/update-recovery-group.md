---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/update-recovery-group.html
---

# Update a recovery group
<a name="update-recovery-group"></a>

The following is an example of a request to update a recovery group to add two cells, and the response.

```
aws route53-recovery-readiness --region us-west-2 update-recovery-group \
			--recovery-group-name test-recovery-group \
			--cells arn:aws:route53-recovery-readiness::888888888888:cell/test-cell arn:aws:route53-recovery-readiness::888888888888:cell/test-cell-2
```

```
{
    "Cells": [
        "arn:aws:route53-recovery-readiness::888888888888:cell/test-cell",
        "arn:aws:route53-recovery-readiness::888888888888:cell/test-cell-2"
    ],
    "RecoveryGroupArn": "arn:aws:route53-recovery-readiness::888888888888:recovery-group/test-recovery-group",
    "RecoveryGroupName": "test-recovery-group",
    "Tags": {}
}
```
