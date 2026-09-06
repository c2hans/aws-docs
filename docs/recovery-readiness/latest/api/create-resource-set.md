---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/create-resource-set.html
---

# Create a resource set
<a name="create-resource-set"></a>

The following is an example of a request to create a resource set with two Amazon EBS volumes, and the response.

```
aws route53-recovery-readiness --region us-west-2 create-resource-set \
			--resource-set-name sample-resource-set \
			--resource-set-type AWS::EC2::Volume \
			--resources ResourceArn="arn:aws:ec2:us-west-2:888888888888:volume/vol-014869e6063ed547b" \
			ResourceArn="arn:aws:ec2:ap-southeast-1:888888888888:volume/vol-0bc095e048255a901"
```

```
{
    "ResourceSetArn": "arn:aws:route53-recovery-readiness::888888888888:resource-set/sample-resource-set",
    "ResourceSetName": "sample-resource-set",
    "Resources": [
        {
            "ReadinessScopes": [],
            "ResourceArn": "arn:aws:ec2:us-west-2:888888888888:volume/vol-014869e6063ed547b"
        },
        {
            "ReadinessScopes": [],
            "ResourceArn": "arn:aws:ec2:ap-southeast-1:888888888888:volume/vol-0bc095e048255a901"
        }
    ],
    "Tags": {}
}
```
