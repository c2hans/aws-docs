---
source_url: https://docs.aws.amazon.com/datazone/latest/userguide/redshift-manage-access-role.html
---

# AmazonDataZoneRedshiftAccess-<region>-<domainId>
<a name="redshift-manage-access-role"></a>

The `AmazonDataZoneRedshiftAccess-<region>-<domainId>` role has the `AmazonDataZoneRedshiftManageAccessRolePolicy` attached. This role grants Amazon DataZone permissions to publish Amazon Redshift data to the catalog. It also gives Amazon DataZone permissions to grant access or revoke access to Amazon Redshift or Amazon Redshift Serverless published assets in the catalog.

The default `AmazonDataZoneRedshiftAccess-<region>-<domainId>` role has the following inline permissions policy attached:

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

The default `AmazonDataZoneRedshiftManageAccessRole<timestamp>` has the following trust policy attached:

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "datazone.amazonaws.com"
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
