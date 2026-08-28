---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/dr-orchestrator-framework-overview.html
---

# DR Orchestrator Framework overview
<a name="dr-orchestrator-framework-overview"></a>

DR Orchestrator Framework provides a one-click solution to orchestrate and automate cross-Region DR for AWS databases. It uses [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) to perform the required steps during the failover and failback. The Step Functions state machines provide the basis for decision making within the orchestrator design. The API operations for performing a failover or failback actions are coded into Lambda functions that are called from within the state machine. The Lambda functions run [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) APIs to interact with AWS databases.

DR Orchestrator Framework contains two main state machines that correspond to the failover and failback phases.

For Amazon RDS, the failover phase promotes a cross-Region RDS read replica into a standalone DB instance. For Amazon Aurora, when the primary Region is down during a rare, unexpected outage, its writer node isn't available. Replication between the writer node and the secondary clusters stops. You must detach the secondary cluster from the global database and promote it as a standalone cluster. Applications can connect and send write traffic to the standalone cluster. You can use this same process to [switch over](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html) the primary DB cluster of the global database to the secondary Regions.  Use this approach for controlled scenarios such as the following:
+ Operational maintenance
+ Planned operational procedures
+ Promotion of an Amazon ElastiCache (Redis OSS) secondary cluster as your new primary cluster

The failback phase establishes live replication of data between a live primary Region and a new secondary Region.

It's critical to understand that DR Orchestrator applies to databases only. All the applications that reference these databases and are in the same Region might need a separate, tandem failover solution. After the databases fail over to the secondary Region, the applications need to be updated to connect to the new database instances, which will serve as the data source.

## The failover process
<a name="failover-process"></a>

To perform a failover, run the `DR Orchestrator FAILOVER` state machine. At this stage, a secondary database is already present in the secondary Region, either as a read replica (Amazon RDS) or as a secondary cluster (Amazon Aurora). When you run the `DR Orchestrator FAILOVER` state machine,  it promotes the secondary database to become the primary.

### DR Orchestrator FAILOVER architecture
<a name="dr-orchestrator-failover-architecture.80effa33-21f9-54b0-aa5e-463b469c4fb9"></a>

The following diagram shows the concepts of the failover process for Amazon Aurora when using DR Orchestrator. Amazon Aurora and Amazon ElastiCache use the same workflow but with different state machines and Lambda functions.

![Architecture diagram of the cross-Region failover process.](http://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/0a87461a-8e51-44b3-b2a9-78ac8640d403.png)

1. The `DR Orchestrator FAILOVER` state machine reads the input JSON parameters.

1. Based on the `resourceType`** **parameter, the state machine calls other  state machines: `Promote RDS Read Replica`, `Failover Aurora Cluster`, or `Failover ElastiCache`. If more than one resource is passed in the input, these state machines run in parallel.

1. The `Failover Aurora Cluster`** **state machine calls Lambda functions in each of the following three steps.

1. The `Resolve imports`** **Lambda function resolves `"! import <export-variable-name>"` with the actual values from the `App-Stack` AWS CloudFormation template.

1. The** **`Failover Aurora Cluster`** **Lambda function** **promotes the read replica as a standalone DB instance.

1. The** **`Check Failover Status` Lambda function checks the status of the promoted DB instance. After the status is **AVAILABLE**, the Lambda function sends a success token back to the calling state machine and completes.

1. You can redirect your applications to the standalone database in the DR Region (`us-west-2`), which is now the primary database.

## The failback process
<a name="failback-process"></a>

After your former primary Region (`us-east-1`) is up again, you can fail back to it, so that the database in `us-east-1` becomes the primary again. To start the failback, run the `DR Orchestrator FAILBACK` state machine. As the name indicates, this state machine starts replicating changes in your new primary Region (`us-west-2`) back to the former primary Region (`us-east-1`), which acts as the current secondary.

After replication is established between the two Regions, you can initiate the failback. To failback and return to your original primary Region (`us-east-1`), run the `DR Orchestrator FAILOVER` state machine in the current secondary Region (`us-east-1`) to promote it to the primary Region.

### DR Orchestrator FAILBACK architecture
<a name="dr-orchestrator-failback-architecture.98f72d8c-e3bd-5078-b3e9-070353725666"></a>

The following diagram shows the concepts of the failback process for Amazon Aurora when using DR Orchestrator.

![Architecture diagram of the cross-Region failback process.](http://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/0f870212-9fa8-49fe-bbaf-8f0507bae1b5.png)

1. Before beginning failback, take a manual DB snapshot to use when performing root cause analysis (RCA).

   Also, disable the `DeletionProtection` for the Aurora cluster in the previous primary Region (`us-east-1`).

1. The `DR Orchestrator FAILBACK` state machine reads the input JSON parameters.

1. Based on the `resourceType`, the `DR Orchestrator FAILBACK` state machine calls the `Create Aurora Secondary DB Cluster`** **state machine.

1. The `Create Aurora Secondary DB Cluster`** **state machine calls Lambda functions in each of the following five steps.

1. The `Resolve import`** **Lambda function resolves `"! import <export-variable-name>"` with the actual values from the `App-Stack` CloudFormation template.

1. The `Delete DB Instance`** **Lambda function deletes the former primary instance.

1. The `Check DB instance status`** **Lambda function checks the `Delete DB Instance status` until the DB is deleted.

1. The `Create Read Replica` Lambda** **function creates a read replica in the secondary Region from the DB instance that's in the new primary Region.

1. The `Check DB instance status`** **Lambda function checks the read replica DB instance status. When the status is **AVAILABLE**, the Lambda function sends a success token back to the calling state machine, which is completed.

## DR Orchestrator FAILOVER
<a name="dr-orchestrator-failover"></a>

Use the `DR Orchestrator FAILOVER` state machine in the DR event when the primary Region (`us-east-1`) is down or during planned events such as operational maintenance.

The function can be called to fail over single or multiple databases in parallel.

![State machine diagram showing failover for different resource types.](http://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/bd15b16b-e388-477c-9cd3-ea6a23aaeab3.jpeg)

The state machine accepts parameters in the JSON format as shown in the following code:

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

### Parameter details
<a name="parameter-details.1d506d63-81d7-550f-b59b-463f77b6dad3"></a>

The following table shows the parameters used by the `DR Orchestrator FAILOVER` state machine.

|
|
| Parameter name | Description | Expected values |
| --- |--- |--- |
| `layer` (required: number) | The processing sequence. All the resources defined in layer 1 must be run before the layer 2 resources are run. | 1 or 2, and so on |
| resources (required: array of dictionary) | All the resources within a single layer run in parallel. | <pre>{<br />"resourceType":"String",<br />"resourceName":"String",<br />"parameters":{<br />"<param1>":"<!Import cft-output-1">,<br />....<br />}</pre> |
| `resourceType` (required: string) | Type of the resource to identify the resource | `PromoteRDSReadReplica` or `FailoverElastiCacheCluster` |
| `resourceName` (optional: string) | To identify which application portfolio these resources belong to | `Promote RDS for MySQL Read Replica` |
| parameters (required: array of dictionary) | List of parameters required to fail over or fail back the AWS database | <pre>{<br />"<param1>":"<!Import cft-output-1>",<br />"<param2>":"<!Import cft-output-2>",<br />}</pre> |

## DR Orchestrator FAILBACK
<a name="dr-orchestrator-failback"></a>

Use the `DR Orchestrator FAILBACK` state machine after the DR event, when the former primary Region (`us-east-1`) is up. You can create the [read replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.Create) for Amazon RDS in the former primary Region from the new primary Region (`us-west-2`) to be compliant with your DR strategy. Because this is a planned event, you can schedule this activity over the weekend or during off-peak business hours with an estimated downtime.

![State machine diagram showing the resource types for failback.](http://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/82105c06-f621-48a2-81b7-1deda944f9e7.jpeg)

The state machine accepts parameters in the JSON format as shown in the following code:

```
{
  "StatePayload": [
    {
      "layer": 1,
      "resources": [
        {
          "resourceType": "CreateRDSReadReplica",
          "resourceName": "Create RDS for MySQL Read Replica",
          "parameters": {
            "RDSInstanceIdentifier": "!Import rds-mysql-instance-identifier",
            "TargetClusterIdentifier": "!Import rds-mysql-instance-global-arn",
            "SourceRDSInstanceIdentifier": "!Import rds-mysql-instance-source-identifier",
            "SourceRegion": "!Import rds-mysql-instance-SourceRegion",
            "MultiAZ": "!Import rds-mysql-instance-MultiAZ",
            "DBInstanceClass": "!Import rds-mysql-instance-DBInstanceClass",
            "DBSubnetGroup": "!Import rds-mysql-instance-DBSubnetGroup",
            "DBSecurityGroup": "!Import rds-mysql-instance-DBSecurityGroup",
            "KmsKeyId": "!Import rds-mysql-instance-KmsKeyId",
            "BackupRetentionPeriod": "7",
            "MonitoringInterval": "60",
            "StorageEncrypted": "True",
            "EnableIAMDatabaseAuthentication": "True",
            "DeletionProtection": "True",
            "CopyTagsToSnapshot": "True",
            "AutoMinorVersionUpgrade": "True",
            "Port": "!Import rds-mysql-instance-DBPortNumber",
            "MonitoringRoleArn": "!Import rds-mysql-instance-RDSMonitoringRole"
          }
        }
      ]
    }
  ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
