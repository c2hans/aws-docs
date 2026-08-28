---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-policy-readonly-v2.html
---

# IAM managed policy for read-only access (v2 managed default policy) for Amazon EMR
<a name="emr-managed-policy-readonly-v2"></a>

To grant read-only privileges to Amazon EMR, attach the **AmazonEMRReadOnlyAccessPolicy\_v2** managed policy. This default managed policy replaces the [`AmazonElasticMapReduceReadOnlyAccess`](emr-managed-policy-readonly.md) managed policy. The content of this policy statement is shown in the following snippet. Compared with the `AmazonElasticMapReduceReadOnlyAccess` policy, the `AmazonEMRReadOnlyAccessPolicy_v2` policy does not use wildcard characters for the `elasticmapreduce` element. Instead, the default v2 policy scopes the allowable `elasticmapreduce` actions.

**Note**
You can also use the AWS Management Console link [`AmazonEMRReadOnlyAccessPolicy_v2`](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonEMRReadOnlyAccessPolicy_v2) to view the policy.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "ElasticMapReduceActions",
      "Effect": "Allow",
      "Action": [
        "elasticmapreduce:DescribeCluster",
        "elasticmapreduce:DescribeEditor",
        "elasticmapreduce:DescribeJobFlows",
        "elasticmapreduce:DescribeSecurityConfiguration",
        "elasticmapreduce:DescribeStep",
        "elasticmapreduce:DescribeReleaseLabel",
        "elasticmapreduce:GetBlockPublicAccessConfiguration",
        "elasticmapreduce:GetManagedScalingPolicy",
        "elasticmapreduce:GetAutoTerminationPolicy",
        "elasticmapreduce:ListBootstrapActions",
        "elasticmapreduce:ListClusters",
        "elasticmapreduce:ListEditors",
        "elasticmapreduce:ListInstanceFleets",
        "elasticmapreduce:ListInstanceGroups",
        "elasticmapreduce:ListInstances",
        "elasticmapreduce:ListSecurityConfigurations",
        "elasticmapreduce:ListSteps",
        "elasticmapreduce:ListSupportedInstanceTypes",
        "elasticmapreduce:ViewEventsFromAllClustersInConsole"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Sid": "ViewMetricsInEMRConsole",
      "Effect": "Allow",
      "Action": [
        "cloudwatch:GetMetricStatistics"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
