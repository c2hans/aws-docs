---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/get-readiness-check-status.html
---

# Check the status of an entire readiness check
<a name="get-readiness-check-status"></a>

The following is an example of a request to list the roll-up status for an entire readiness check, and the response.

```
aws route53-recovery-readiness --region us-west-2 get-readiness-check-status \
			--readiness-check-name ebs-volume-readiness
```

```
{
    "Readiness": "READY",
    "Resources": [
        {
            "LastCheckedTimestamp": "2021-01-07T00:53:39Z",
            "Readiness": "READY",
            "ResourceArn": "arn:aws:ec2:us-west-2:888888888888:volume/vol-014869e6063ed547b"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:53:39Z",
            "Readiness": "READY",
            "ResourceArn": "arn:aws:ec2:ap-southeast-1:888888888888:volume/vol-0bc095e048255a901"
        }
    ]
}
```
