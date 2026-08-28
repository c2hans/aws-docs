---
source_url: https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_aurora_provisioned_scaling.html
---

# Aurora provisioned scaling execution block sample policy
<a name="security_iam_region_switch_aurora_provisioned_scaling"></a>

 The following is a sample policy to attach if you add execution blocks to a Region switch plan for Aurora provisioned cluster scaling.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBInstances",
        "rds:DescribeDBClusters",
        "rds:DescribeGlobalClusters",
        "rds:CreateDBInstance",
        "rds:ModifyDBInstance"
      ],
      "Resource": [
        "arn:aws:rds:{{region}}:{{account-id}}:db:{{instance-name}}",
        "arn:aws:rds:{{region}}:{{account-id}}:cluster:{{cluster-name}}",
        "arn:aws:rds::{{account-id}}:global-cluster:{{global-cluster-name}}"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeOrderableDBInstanceOptions",
        "ec2:DescribeInstanceTypes"
      ],
      "Resource": "*"
    }
  ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query r53recovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
