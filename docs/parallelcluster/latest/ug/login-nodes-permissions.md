---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/login-nodes-permissions.html
---

# Permissions required to run the login nodes pool
<a name="login-nodes-permissions"></a>

In order to manage the login nodes pool the cluster administrator must have the following additional permissions:

```
            - Action:
              - iam:CreateServiceLinkedRole
              - autoscaling:DeleteAutoScalingGroup
              - autoscaling:DeleteLifecycleHook
              - autoscaling:Describe*
              - autoscaling:PutLifecycleHook
              - autoscaling:UpdateAutoScalingGroup
              - elasticloadbalancing:CreateListener
              - elasticloadbalancing:CreateTargetGroup
              - elasticloadbalancing:DeleteListener
              - elasticloadbalancing:DeleteLoadBalancer
              - elasticloadbalancing:DeleteTargetGroup
              - elasticloadbalancing:Describe*
              - elasticloadbalancing:ModifyLoadBalancerAttributes
            Resource: '*'
            Condition:
              ForAllValues:StringEquals:
                aws:TagKeys: [ "parallelcluster:cluster-name" ]
            - Action:
              - autoscaling:CreateAutoScalingGroup
              - autoscaling:DeleteTags
              - autoscaling:CreateOrUpdateTags
              - elasticloadbalancing:AddTags
              - elasticloadbalancing:CreateLoadBalancer
              - elasticloadbalancing:RemoveTags
              - elasticloadbalancing:ModifyTargetGroup
            Resource: '*'
            Effect: Allow
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
