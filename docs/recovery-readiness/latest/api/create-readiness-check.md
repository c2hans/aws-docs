---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/create-readiness-check.html
---

# Create a readiness check
<a name="create-readiness-check"></a>

The following is an example of a request to create a readiness check for an Amazon EBS volume, and the response.

```
aws route53-recovery-readiness --region us-west-2 create-readiness-check \
			--readiness-check-name ebs-volume-readiness \
			--resource-set-name sample-resource-set
```

```
{
    "ReadinessCheckArn": "arn:aws:route53-recovery-readiness::888888888888:readiness-check/ebs-volume-readiness",
    "ReadinessCheckName": "ebs-volume-readiness",
    "ResourceSet": "sample-resource-set",
    "Tags": {}
}
```
