---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-vpce-iam-policy.html
---

# Using Amazon S3 VPC Endpoints for WorkSpaces Applications Features
<a name="managing-network-vpce-iam-policy"></a>

When you enable Application Settings Persistence or Home folders on a stack, WorkSpaces Applications uses the VPC you specify for your fleet to provide access to Amazon Simple Storage Service (Amazon S3) buckets. For Elastic fleets, WorkSpaces Applications will use the VPC to access the Amazon S3 bucket containing applications assigned to the fleet's app block. To enable WorkSpaces Applications access to your private S3 endpoint, attach the following custom policy to your VPC endpoint for Amazon S3. For more information about private Amazon S3 endpoints, see [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html) and [Endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html) in the *Amazon VPC User Guide*.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "Allow-AppStream-to-access-S3-buckets",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:sts::{{111122223333}}:assumed-role/AmazonAppStreamServiceAccess/AppStream2.0"
            },
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:GetObjectVersion",
                "s3:DeleteObjectVersion"
            ],
            "Resource": [
                "arn:aws:s3:::appstream2-36fb080bb8-*",
                "arn:aws:s3:::appstream-app-settings-*",
                "arn:aws:s3:::appstream-logs-*"
            ]
        },
        {
            "Sid": "Allow-AppStream-ElasticFleetstoRetrieveObjects",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::{{bucket-with-application-or-app-block-objects}}/*",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalServiceName": "appstream.amazonaws.com"
                }
            }
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
