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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-readiness` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
