---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/faq.html
---

# FAQ
<a name="faq"></a>

Find answers to questions about DR Orchestrator Framework for failover and failback.

## What are the RPO and RTO I can achieve using this approach?
<a name="q-1"></a>

For information about recovery time objective (RTO) and recovery point objective (RPO), see the guide [Disaster recovery strategy for databases on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-disaster-recovery/welcome.html).

## Is it mandatory to use AWS CloudFormation export variables?
<a name="q-2"></a>

No, you can directly pass the value of the Amazon Aurora global database or the Amazon RDS DB instance directly in the JSON format (for example: `-  "RDSInstanceIdentifier": "rds-mysql-instance"`).

## Can I use the DR Orchestrator FAILOVER workflow to fail over more than one AWS database?
<a name="q-3"></a>

Yes, you can pass more than one resource in the *input parameter *file to fail over more than one AWS database. The following code example shows failing over an Amazon RDS for MySQL read replica and an Amazon ElastiCache (Redis OSS) global datastore in parallel:

```
{
  "StatePayload": [
    {
      "layer": 1,
      "resources": [
        {
          "resourceType": "PromoteRDSReadReplica",
          "resourceName": "Promote RDS MySQL Read Replica",
          "parameters": {
            "RDSInstanceIdentifier": "!Import rds-mysql-instance-identifier",
            "TargetClusterIdentifier": "!Import rds-mysql-instance-global-arn"
          }
        },
        {
          "resourceType": "FailoverElastiCacheCluster",
          "resourceName": "Failover ElastiCache Cluster",
          "parameters": {
            "GlobalReplicationGroupId": "!Import demo-redis-cluster-global-replication-group-id",
            "TargetRegion": "!Import demo-redis-cluster-target-region",
            "TargetReplicationGroupId": "!Import demo-redis-cluster-target-replication-group-id"
          }
        }
      ]
    }
  ]
}
```

## How can I avoid the InvalidParameterCombination error when I run the DR Orchestrator FAILBACK state machine for Amazon RDS?
<a name="q-4"></a>

The full text of the error is:

`"errorMessage": "An error occurred (InvalidParameterCombination) when calling the DeleteDBInstance operation: Cannot delete protected DB Instance, please disable deletion protection and try again."`

To avoid the error, [modify the RDS instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html) by disabling `DeletionProtection`** **before you run the `DR Orchestrator FAILBACK` state machine.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
