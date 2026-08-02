---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/get-readiness-check.html
---

# Get a readiness check
<a name="get-readiness-check"></a>

The following is an example of a request to get a readiness check, and the response.

```
aws route53-recovery-readiness --region us-west-2 get-readiness-check \
			--readiness-check-name ebs-volume-readiness
```

```
{
    "ReadinessCheckArn": "arn:aws:route53-recovery-readiness::888888888888:readiness-check/ebs-volume-readiness",
    "ReadinessCheckName": "ebs-volume-readiness",
    "ResourceSet": "sample-resource-set",
    "Tags": {}
}
```
