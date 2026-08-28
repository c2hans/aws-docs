---
source_url: https://docs.aws.amazon.com/datazone/latest/userguide/AmazonDataZoneSageMakerManageAccessRole.html
---

# AmazonDataZoneSageMakerManageAccessRole-<region>-<domainId>
<a name="AmazonDataZoneSageMakerManageAccessRole"></a>

The `AmazonDataZoneSageMakerManageAccessRole` role has the `AmazonDataZoneSageMakerAccess`, the `AmazonDataZoneRedshiftManageAccessRolePolicy`, and the `AmazonDataZoneGlueManageAccessRolePolicy` attached. This role grants Amazon DataZone permissions to publish and manage subscriptions for data lake, data warehouse, and Amazon Sagemaker assets.

The `AmazonDataZoneSageMakerManageAccessRole` role has the following inline policy attached:

------
#### [ JSON ]

****

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid": "RedshiftSecretStatement",
         "Effect":"Allow",
         "Action":"secretsmanager:GetSecretValue",
         "Resource":"*",
         "Condition":{
            "StringEquals":{
               "secretsmanager:ResourceTag/AmazonDataZoneDomain":"{{domainId}}"
            }
         }
      }
   ]
}
```

------

The `AmazonDataZoneSageMakerManageAccessRole` role has the following trust policy attached:

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "DatazoneTrustPolicyStatement",
      "Effect": "Allow",
      "Principal": {
        "Service":  ["datazone.amazonaws.com",
                   "sagemaker.amazonaws.com"]
      },
      "Action": "sts:AssumeRole",
      "Condition": {
            "StringEquals": {
            "aws:SourceAccount": "111122223333"
            },
            "ArnEquals": {
            "aws:SourceArn": "arn:aws:datazone:us-east-1:111122223333:domain/dzd-12345"
            }
        }
    }
]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
