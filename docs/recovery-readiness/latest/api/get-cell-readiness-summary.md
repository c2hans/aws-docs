---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/get-cell-readiness-summary.html
---

# Check the readiness of a cell
<a name="get-cell-readiness-summary"></a>

The following is an example of a request to check cell readiness, and the response.

```
aws route53-recovery-readiness --region us-west-2 get-cell-readiness-summary \
			--cell-name test-cell
```

```
{
    "Readiness": "READY",
    "ReadinessChecks": [
        {
            "Readiness": "READY",
            "ReadinessCheckName": "ebs-volume-readiness"
        }
    ]
}
```
