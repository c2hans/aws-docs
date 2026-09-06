---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/delete-recovery-group.html
---

# Delete a recovery group
<a name="delete-recovery-group"></a>

The following is an example of a request to delete a recovery group. Note that there is no response on success when you delete a recovery group.

```
aws route53-recovery-readiness --region us-west-2 delete-recovery-group \
			--recovery-group-name test-recovery-group
```
