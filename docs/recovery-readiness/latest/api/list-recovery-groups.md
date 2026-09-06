---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/list-recovery-groups.html
---

# List recovery groups
<a name="list-recovery-groups"></a>

The following is an example of a request to list the recovery groups in an account, and the response.

```
aws route53-recovery-readiness --region us-west-2 list-recovery-groups
```

```
{
    "RecoveryGroups": [
        {
            "Cells": [
                "arn:aws:route53-recovery-readiness::888888888888:cell/test-cell",
                "arn:aws:route53-recovery-readiness::888888888888:cell/test-cell-2"
            ],
            "RecoveryGroupArn": "arn:aws:route53-recovery-readiness::888888888888:recovery-group/test-recovery-group",
            "RecoveryGroupName": "test-recovery-group",
            "Tags": {}
        }
    ]
}
```
