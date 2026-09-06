---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/get-recovery-group-readiness-summary.html
---

# Check the readiness of a recovery group
<a name="get-recovery-group-readiness-summary"></a>

The following is an example of a request to check a recovery group readiness, and the response.

For this example, we have configured a readiness check and resource set at the level of the recovery group (creation not shown), and now retrieve readiness of the recovery group itself.

```
aws route53-recovery-readiness --region us-west-2 get-recovery-group-readiness-summary \
			--recovery-group-name test-recovery-group
```

```
{
    "Readiness": "READY",
    "ReadinessChecks": [
        {
            "Readiness": "READY",
            "ReadinessCheckName": "ddb-table-readiness"
        }
    ]
}
```
