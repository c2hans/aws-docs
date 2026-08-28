---
source_url: https://docs.aws.amazon.com/datazone/latest/userguide/bootstraprole.html
---

# AmazonDataZoneProvisioningRole-<domainAccountId>
<a name="bootstraprole"></a>

The `AmazonDataZoneProvisioningRole-<domainAccountId>` has the `AmazonDataZoneRedshiftGlueProvisioningPolicy` attached. This role grants Amazon DataZone the permissions required to interoperate with AWS Glue and Amazon Redshift.

The default `AmazonDataZoneProvisioningRole-<domainAccountId>` has the following trust policy attached:

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
            "aws:SourceAccount": "{{domain_account}}"
        }
      }
    }
  ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
