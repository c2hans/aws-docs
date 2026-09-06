---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/update-resource-set.html
---

# Update a resource set
<a name="update-resource-set"></a>

The following is an example of a request to update a resource set, and the response.

This updates the resource set so that the resources each reference a cell. Note that the resources field is replaced in its entirety, so we specify the ResourceArns.

```
aws route53-recovery-readiness --region us-west-2 update-resource-set \
			--resource-set-name sample-resource-set \
			--resource-set-type AWS::EC2::Volume \
			--resources ResourceArn="arn:aws:ec2:us-west-2:888888888888:volume/vol-014869e6063ed547b",ReadinessScopes=\[arn:aws:route53-recovery-readiness::888888888888:cell/test-cell\] \
			ResourceArn="arn:aws:ec2:ap-southeast-1:888888888888:volume/vol-0bc095e048255a901",ReadinessScopes=\[arn:aws:route53-recovery-readiness::888888888888:cell/test-cell-2\]
```

```
{
    "ResourceSetArn": "arn:aws:route53-recovery-readiness::888888888888:resource-set/sample-resource-set",
    "ResourceSetName": "sample-resource-set",
    "Resources": [
        {
            "ReadinessScopes": [
                "arn:aws:route53-recovery-readiness::888888888888:cell/test-cell"
            ],
            "ResourceArn": "arn:aws:ec2:us-west-2:888888888888:volume/vol-014869e6063ed547b"
        },
        {
            "ReadinessScopes": [
                "arn:aws:route53-recovery-readiness::888888888888:cell/test-cell-2"
            ],
            "ResourceArn": "arn:aws:ec2:ap-southeast-1:888888888888:volume/vol-0bc095e048255a901"
        }
    ],
    "Tags": {}
}
```
