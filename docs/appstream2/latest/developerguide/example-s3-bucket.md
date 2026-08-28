---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/example-s3-bucket.html
---

# Example: WorkSpaces Applications Application Amazon S3 bucket policy cross-service confused deputy prevention
<a name="example-s3-bucket"></a>

When you store data in an Amazon S3 bucket, the bucket might be exposed to confused deputy issues. This can leave data such as Elastic fleets, app blocks, setup scripts, application icons, and session scripts vulnerable to malicious actors.

To prevent confused deputy issues, you can specify the `aws:SourceAccount` condition or the `aws:SourceArn` condition in the Amazon S3 bucket policy for `ELASTIC-FLEET-EXAMPLE-BUCKET`.

The resource policies below show how to prevent the confused deputy problem with either of the following:
+ The `aws:SourceAccount` with your AWS account ID
+ The global condition context key `aws:SourceArn`

WorkSpaces Applications currently doesn't support confused deputy prevention for application icons. The service only supports VHD files and setup scripts. If you try to add additional conditions for application icons, the icons won't be displayed to end users.

In the following example, the bucket policy only allows WorkSpaces Applications Elastic fleet resources in the owner's account to access `ELASTIC_FLEET_EXAMPLE_BUCKET`.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "ConfusedDeputyPreventionExamplePolicy",
            "Effect": "Allow",
            "Principal": {
                "Service": "appstream.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::{{ELASTIC-FLEET-EXAMPLE-BUCKET}}/vhd-folder/*",
                "arn:aws:s3:::{{ELASTIC-FLEET-EXAMPLE-BUCKET}}/scripts/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{your AWS account ID}}"
                }
            }
        },
        {
            "Sid": "AllowRetrievalPermissionsToS3AppIconsForAppStream",
            "Effect": "Allow",
            "Principal": {
                "Service": "appstream.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::{{ELASTIC-FLEET-EXAMPLE-BUCKET}}/app-icons/*"
        }
    ]
}
```

------

You can also use the `aws:SourceArn` condition to limit resource access for specific resources.

**Note**
If you don’t know the full ARN of a resource, or you want to specify multiple resources, use the `aws:SourceArn` global context condition key with wildcards (\*) for the unknown portions of the ARN.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "ConfusedDeputyPreventionExamplePolicy",
            "Effect": "Allow",
            "Principal": {
                "Service": "appstream.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::{{ELASTIC-FLEET-EXAMPLE-BUCKET}}/vhd-folder/*",
                "arn:aws:s3:::{{ELASTIC-FLEET-EXAMPLE-BUCKET}}/scripts/*"
            ],
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:appstream:{{us-east-1}}:{{111122223333}}:app-block/*"
                }
            }
        },
        {
            "Sid": "AllowRetrievalPermissionsToS3AppIconsForAppStream",
            "Effect": "Allow",
            "Principal": {
                "Service": "appstream.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::{{ELASTIC-FLEET-EXAMPLE-BUCKET}}/app-icons/*"
        }
    ]
}
```

------

You can use the `aws:SourceArn` and `aws:SourceAccount` conditions to limit the resource access for specific resources and accounts.

**Note**
If you don’t know the full ARN of a resources, or if you want to specify multiple resources, use the `aws:SourceArn` global context condition key with wildcards (\*) for the unknown portions of the ARN.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "ConfusedDeputyPreventionExamplePolicy",
            "Effect": "Allow",
            "Principal": {
                "Service": "appstream.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::{{ELASTIC-FLEET-EXAMPLE-BUCKET}}/vhd-folder/*",
                "arn:aws:s3:::{{ELASTIC-FLEET-EXAMPLE-BUCKET}}/scripts/*"
            ],
            "Condition": {
                "ArnLike": {
                "aws:SourceArn": "arn:aws:appstream:{{us-east-1}}:{{111122223333}}:app-block/*"
                },
                "StringEquals": {
                    "aws:SourceAccount": "{{your AWS account ID}}"
                }
            }
        },
        {
            "Sid": "AllowRetrievalPermissionsToS3AppIconsForAppStream",
            "Effect": "Allow",
            "Principal": {
                "Service": "appstream.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::{{ELASTIC-FLEET-EXAMPLE-BUCKET}}/app-icons/*"
        }
    ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
