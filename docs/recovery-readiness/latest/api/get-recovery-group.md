---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/get-recovery-group.html
---

# Get a recovery group
<a name="get-recovery-group"></a>

The following is an example of a request to get a recovery group, and the response.

```
aws route53-recovery-readiness --region us-west-2 get-recovery-group \
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
