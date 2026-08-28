---
source_url: https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_rds_switchover_read_replica.html
---

# Amazon RDS Switchover Read Replica execution block sample policy
<a name="security_iam_region_switch_rds_switchover_read_replica"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Amazon RDS Oracle read replica switchover.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBInstances",
        "rds:SwitchoverReadReplica",
        "rds:DescribePendingMaintenanceActions",
        "rds:ModifyDBInstance"
      ],
      "Resource": [
        "arn:aws:rds:{{region}}:{{account-id}}:db:{{instance-name}}"
      ]
    }
  ]
}
```

If you configure an ungraceful behavior (`promoteReadReplica`), add the following action to the policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBInstances",
        "rds:SwitchoverReadReplica",
        "rds:DescribePendingMaintenanceActions",
        "rds:PromoteReadReplica",
        "rds:ModifyDBInstance"
      ],
      "Resource": [
        "arn:aws:rds:{{region}}:{{account-id}}:db:{{instance-name}}"
      ]
    }
  ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query r53recovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
