---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/delete-resource-set.html
---

# Delete a resource set
<a name="delete-resource-set"></a>

The following is an example of a request to delete a resource set. Note that there is no response on success when you delete a resource set.

```
aws route53-recovery-readiness --region us-west-2 delete-resource-set \
			--resource-set-name sample-resource-set
```
