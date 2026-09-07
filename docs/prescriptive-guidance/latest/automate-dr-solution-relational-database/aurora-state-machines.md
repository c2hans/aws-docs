---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/aurora-state-machines.html
---

# Aurora states and Step Functions state machines
<a name="aurora-state-machines"></a>

This section covers the process and state machines specific to failing over and failing back Amazon Aurora clusters. The clusters are configured as a global database.

**Note**
For the demonstration purposes, this example uses Aurora MySQL-Compatible Edition. You can use similar steps for Aurora PostgreSQL-Compatible Edition.

## Steady state
<a name="aurora-steady-state"></a>

In the steady state, an Amazon Aurora MySQL-Compatible global database (`dr-globaldb-cluster-mysql`) has been created with two DB clusters. The first DB cluster (`db-cluster-01`) has been created in the primary AWS Region (`us-east-1`) to serve the read/write workload. The second DB cluster (`db-cluster-02`)** **has been created in the secondary Region (`us-west-2`) to server the read-only workload.

In addition to providing the DR solution, you can reduce the load on your primary DB cluster by routing read queries from your applications to the secondary DB cluster. Each of these clusters contains one database instance called `dbcluster-01-use1-instance-1` and `dbcluster-02-usw2-instance-2`, respectively.

## Event state
<a name="aurora-event-state"></a>

By using an Amazon Aurora global database, you can plan for and recover from disaster fairly quickly. Recovery from disaster is typically measured using values for recovery time objective (RTO) and recovery point objective (RPO). For more information, see [Using switchover or failover in an Amazon Aurora global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html).

With an Aurora global database, there are two different approaches to failover:
+ Switchover (managed planned failover)
+ Failover (manual unplanned failover, or *detach and promote*)

### Switchover
<a name="switchover.394d0acf-cf8e-55d2-9990-f262e6047bd4"></a>

Switchover is intended for controlled environments, such as operational maintenance and other planned operational procedures. By using a managed planned failover, you can relocate the primary DB cluster of your Aurora global database to one of the secondary Regions. Because switchover waits until the secondary DB clusters are synchronized with the primary database, RPO is 0 (no data loss). To learn more, see [Performing switchovers for Amazon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-disaster-recovery.managed-failover).

The `dr-orchestrator-stepfunction-FAILOVER` state machine is invoked during the* event state* to switch your primary cluster over to your chosen secondary Region (`us-west-2`).

To perform the switchover, do the following:

1. Sign in to the AWS Management Console.

1. Change the Region to the DR Region (`us-west-2`).

1. Navigate to **Services**, and choose **Step Functions**.

1. Navigate to the `dr-orchestrator-stepfunction-FAILOVER` state machine.

1. Choose **Start execution**, and enter the following JSON code in the `Input - optional` section:

   ```
   {
     "StatePayload": [
       {
         "layer": 1,
         "resources": [
           {
             "resourceType": "PlannedFailoverAurora",
             "resourceName": "Switchover (planned failover) of Amazon Aurora global databases (MySQL)",
             "parameters": {
               "GlobalClusterIdentifier": "!Import dr-globaldb-cluster-mysql-global-identifier",
               "DBClusterIdentifier": "!Import dr-globaldb-cluster-mysql-cluster-identifier"
             }
           }
         ]
       }
     ]
   }
   ```

1. The `dr-orchestrator-stepfunction-FAILOVER` state machine reads the resource type as `PlannedFailoverAuroraMySQ`L, and it calls the `dr-orchestrator-stepfunction-planned-Aurora-failover` state machine to fail over the Aurora global database.
![State machine diagram for PlannedFailoverAurora.](https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/cb26c179-db96-47df-8954-08a605642e6d.jpeg)

1. The `dr-orchestrator-stepfunction-planned-Aurora-failover` state machine performs the following steps to switch over the Aurora MySQL-Compatible global database role.
![State machine diagram of checking failover status.](https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/ddd4ea6e-9c1e-4148-9a11-ae5106887ec7.jpeg)
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/aurora-state-machines.html)

1. Navigate to the Amazon RDS console. Under **Status**, the values for the Aurora global database will change from **Available** to **Switching over** or **Modifying**.

1. After the `dr-orchestrator-stepfunction-planned-Aurora-failover` state machine is completed, it sends a success token back to the `dr-orchestrator-stepfunction-FAILOVER` state machine.
![State machine diagram showing that the success token was sent.](https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/0ce403c7-fcfa-4d0b-960e-27dd439d8b5c.jpeg)

1. The `dr-orchestrator-stepfunction-FAILOVER` state machine is completed.
![State machine diagram showing that the state machine is completed.](https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/a0ed8be8-c8d8-4cd3-9101-8c02588d394a.jpeg)

On the console, the role of the **Secondary cluster** (`dbcluster-02`) is now **Primary cluster**, and the cluster is ready to serve read/write workloads. The role of the original primary cluster (`dbcluster-01`) is now listed as **Secondary cluster**.

### Manual unplanned failover
<a name="manual-unplanned-failover.8cbf2ab7-7054-5508-a712-7267eda63bc4"></a>

On rare occasions, your Aurora global database might experience an unexpected outage in its primary AWS Region. If this happens, your primary Aurora DB cluster and its writer node aren't available, and the replication between the primary cluster and the secondaries ceases. To minimize both downtime (RTO) and data loss (RPO), work quickly to perform a cross-Region failover and reconstruct your Aurora global database. For more information, see [Recovering an Amazon Aurora global database from an unplanned outage](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-failover).

Performing an unplanned failover requires you to detach your secondary cluster from the Aurora global database. Before you perform the unplanned failover, stop application writes on your primary Aurora DB cluster. After the failover is completed successfully, reconfigure the application to write to the new primary DB cluster. This approach helps prevent data loss. It also helps avoid data inconsistencies if the primary writer node comes back online during the failover process.

To perform the unplanned failover, call the `dr-orchestrator-stepfunction-FAILOVER` state machine. For this example, the **Secondary cluster** (`db-cluster-02`*)*** **is in the DR Region (`us-west-2`) in the steady state.

To perform the failover, do the following:

1. Sign in to the console.

1. Change the Region to the DR Region (`us-west-2`).

1. Navigate to **Services**, and choose **Step Functions**.

1. Navigate to the `dr-orchestrator-stepfunction-FAILOVER` state machine.

1. Choose **Start execution**, and enter the following JSON code in the `Input - optional` section, using `UnPlannedFailoverAurora` as the `resourceType`*:*

   ```
   {
     "StatePayload": [
       {
         "layer": 1,
         "resources": [
           {
             "resourceType": "UnPlannedFailoverAurora",
             "resourceName": "Performing unplanned failover for Amazon Aurora global databases (MySQL)",
             "parameters": {
               "GlobalClusterIdentifier": "!Import dr-globaldb-cluster-mysql-global-identifier",
               "DBClusterIdentifier": "!Import dr-globaldb-cluster-mysql-cluster-identifier",
               "ClusterRegion": "!Import dr-globaldb-cluster-mysql-cluster-region"
             }
           }
         ]
       }
     ]
   }
   ```

1. The `dr-orchestrator-stepfunction-FAILOVER` state machine reads the resource type as `UnPlannedFailoverAuroraMySQL` and calls the task `Detach Cluster from Global Database` from the `dr-orchestrator-stepfunction-unplanned-Aurora-failover` state machine.
![State machine diagram with resource type UnPlannedFailoverAurora.](https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/1c19cf09-ea29-4e88-9ef9-310782b2bcd2.jpeg)

1. The `Detach Cluster from Global Database` task detaches (removes) the secondary cluster from the global database.
![State machine diagram for detaching the cluster and sending the success token.](https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/c52a0349-b6ae-4c9e-bba6-950e3234b2a1.jpeg)

1. The secondary cluster (`dbcluster-02`) is promoted to become a standalone cluster, and it can serve read/write workloads.

1. The `dr-orchestrator-stepfunction-FAILOVER` state machine is completed.
![State machine diagram showing the task as completed.](https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/12eabdf4-df07-4a81-ae2a-99c1c80a38b0.jpeg)

1. The secondary cluster (`dbcluster-02`) is detached from the Aurora global database, and it becomes a standalone cluster to serve the read/writer workload.

1. Reconfigure your application to send all write operations to this new standalone Aurora DB cluster by using its new cluster endpoint.

## Failback
<a name="aurora-failback"></a>

A failback returns your database to the original (or new) primary location after a disaster (or a scheduled event) is resolved. When the unplanned outage has been resolved, you might want to add your former primary Region back to the Aurora global database. You must first delete the existing DB cluster from the former primary Region, create a new DB cluster from the new primary Region, and then use the managed planned failover process to switch over the new cluster's role.

This can be considered as a planned activity that you can perform during off-peak hours or on a weekend.

You must manually [modify the Amazon Aurora DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Modifying.html) and disable the `DeletionProtection`** **before you run the `DR Orchestrator FAILBACK` state machine from the former primary Region (`us-east-1`) because it was created with `DeletionProtection`.

DR Orchestrator Framework uses the `dr-orchestrator-stepfunction-FAILBACK`  state machine to automate the steps to delete the existing cluster and create a new cluster in the former primary Region.

To disable `DeletionProtection`, do the following:

1. Sign in to the console.

1. Change the Region to the former primary Region (`us-east-1`).

1. Navigate to the Amazon RDS console, select the cluster name (`dbcluster-01`), and choose **Modify**.

1. Under **Deletion protection**, clear the **Enable deletion protection** check box, and choose **Continue**.

1. Choose **Apply immediately**, and then choose **Modify cluster**.

The `DR Orchestrator FAILBACK` state machine is invoked during the failback process from the former primary Region (`us-east-1`).

To perform the failback, do the following:

1. Sign in to the console.

1. Change the Region to the former primary Region (`us-east-1`).

1. Navigate to **Services**, and then choose **Step Functions**.

1. Navigate to the `DR Orchestrator FAILBACK` state machine.

1. Choose **Start execution**, and enter the following JSON code in the `Input - optional` section:

   ```
    {
     "StatePayload": [
       {
         "layer": 1,
         "resources": [
           {
             "resourceType": "CreateAuroraSecondaryDBCluster",
             "resourceName": "To create secondary Aurora MySQL Global Database Cluster",
             "parameters": {
               "GlobalClusterIdentifier": "!Import dr-globaldb-cluster-mysql-global-identifier",
               "DBClusterIdentifier": "!Import dr-globaldb-cluster-mysql-cluster-identifier",
               "DBClusterName": "!Import dr-globaldb-cluster-mysql-cluster-name",
               "SourceDBClusterIdentifier": "!Import dr-globaldb-cluster-mysql-source-cluster-identifier",
               "DBInstanceIdentifier": "!Import dr-globaldb-cluster-mysql-instance-identifier",
               "Port": "!Import dr-globaldb-cluster-mysql-port",
               "DBInstanceClass": "!Import dr-globaldb-cluster-mysql-instance-class",
               "DBSubnetGroupName": "!Import dr-globaldb-cluster-mysql-subnet-group-name",
               "VpcSecurityGroupIds": "!Import dr-globaldb-cluster-mysql-vpc-security-group-ids",
               "Engine": "!Import dr-globaldb-cluster-mysql-engine",
               "EngineVersion": "!Import dr-globaldb-cluster-mysql-engine-version",
               "KmsKeyId": "!Import dr-globaldb-cluster-mysql-KmsKeyId",
               "SourceRegion": "!Import dr-globaldb-cluster-mysql-source-region",
               "ClusterRegion": "!Import dr-globaldb-cluster-mysql-cluster-region",
               "BackupRetentionPeriod": "7",
               "MonitoringInterval": "60",
               "StorageEncrypted": "True",
               "EnableIAMDatabaseAuthentication": "True",
               "DeletionProtection": "True",
               "CopyTagsToSnapshot": "True",
               "AutoMinorVersionUpgrade": "True",
               "MonitoringRoleArn": "!Import rds-mysql-instance-RDSMonitoringRole"
             }
           }
         ]
       }
     ]
   }
   ```

1. The `DR Orchestrator FAILBACK` state machine reads the resource type as `CreateAuroraSecondaryDBCluster`, and it calls the  `dr-orchestrator-stepfunction-create-Aurora-Secondary-cluster` state machine.
![State machine diagram showing the resource type as CreateAuroraSecondaryCluster.](https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/65548afd-0f76-4e40-9b64-713ae437de3d.jpeg)

1. The `dr-orchestrator-stepfunction-create-Aurora-Secondary-cluster` state machine deletes the existing cluster (`dbcluster-01`) from the former primary Region (`us-east-1`).
![State machine diagram of deleting the existing cluster from the global database.](https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/77bb12f6-fd30-48f1-b96f-85375abda316.jpeg)

1. After the cluster (`dbcluster-01`) is deleted, the state machine creates a new cluster (`dbcluster-01`) along with the DB instance, and it joins the Aurora global database as the secondary cluster to serve read-only workloads.
![State machine diagram showing creation of the secondary database cluster.](https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/b8dbf389-12b1-4ca0-adaf-eeb3f4bc251a.jpeg)

1. After the secondary cluster is available, the `dr-orchestrator-stepfunction-create-Aurora-Secondary-cluster` state machine is completed, and it sends a success token back to the `DR Orchestrator Failback` state machine.
![State machine showing the success token sent.](https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/4e78f743-2187-4f89-a610-d944ccc34849.jpeg)

1. The `dr-orchestrator-stepfunction-FAILBACK` state machine is completed.
![State machine diagram of CreateAuroraSecondaryDBCluster completed.](https://docs.aws.amazon.com/prescriptive-guidance/latest/automate-dr-solution-relational-database/images/guide-img/d246ab63-9f04-4f98-b5ad-efa34d559323/images/6e9c19bf-886e-4784-80ea-dcaf6372f92f.jpeg)

1. You can verify the Aurora global database on the Amazon RDS console.

If you want to relocate the primary DB cluster to `us-east-1` then you can follow the steps mentioned in the [Switchover](#aurora-event-state) section.
