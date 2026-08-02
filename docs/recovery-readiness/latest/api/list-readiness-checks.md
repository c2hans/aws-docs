---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/list-readiness-checks.html
---

# List readiness checks
<a name="list-readiness-checks"></a>

The following is an example of a request to list the readiness checks in an account, and the response.

```
aws route53-recovery-readiness --region us-west-2 list-readiness-checks
```

```
{
    "ReadinessChecks": [
        {
            "ReadinessCheckArn": "arn:aws:route53-recovery-readiness::888888888888:readiness-check/ebs-volume-readiness",
            "ReadinessCheckName": "ebs-volume-readiness",
            "ResourceSet": "sample-resource-set",
            "Tags": {}
        }
    ]
}
```
