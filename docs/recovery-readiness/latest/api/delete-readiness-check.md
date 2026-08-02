---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/delete-readiness-check.html
---

# Delete a readiness check
<a name="delete-readiness-check"></a>

The following is an example of a request to delete a readiness check. Note that there is no response on success when you delete a readiness check.

```
aws route53-recovery-readiness --region us-west-2 delete-readiness-check \
			--readiness-check-name ebs-volume-readiness
```
