---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/delete-safety-rule.html
---

# Delete a safety rule
<a name="delete-safety-rule"></a>

The following is an example of a request to delete a safety rule. Deleting a safety rule doesn't return a response.

```
aws route53-recovery-control-config --region us-west-2 delete-safety-rule \
			--safety-rule-arn arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/safetyrule/333333444444
```
