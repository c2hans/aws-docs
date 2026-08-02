---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/update-readiness-check.html
---

# Update a readiness check
<a name="update-readiness-check"></a>

The following is an example of a request to update a readiness check, and the response.

```
aws route53-recovery-readiness --region us-west-2 update-readiness-check \
			--readiness-check-name ebs-volume-readiness \
			--resource-set-name some-other-resource-set
```

```
{
    "ReadinessCheckArn": "arn:aws:route53-recovery-readiness::888888888888:readiness-check/ebs-volume-readiness",
    "ReadinessCheckName": "ebs-volume-readiness",
    "ResourceSet": "some-other-resource-set",
    "Tags": {}
}
```
