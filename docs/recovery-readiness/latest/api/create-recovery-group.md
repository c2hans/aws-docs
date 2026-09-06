---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/create-recovery-group.html
---

# Create a recovery group
<a name="create-recovery-group"></a>

The following is an example of a request to list the cells in an account, and the response.

```
aws route53-recovery-readiness --region us-west-2 create-recovery-group \
			--recovery-group-name test-recovery-group
```

```
{
    "Cells": [],
    "RecoveryGroupArn": "arn:aws:route53-recovery-readiness::888888888888:recovery-group/test-recovery-group",
    "RecoveryGroupName": "test-recovery-group",
    "Tags": {}
}
```
