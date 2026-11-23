---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/live-migration.html
---

# Atlas Live Migration Service

The [Atlas Live Migration Service](https://www.mongodb.com/cloud/atlas/migrate) initiates an initial copy of the data from the source database (only MongoDB databases), monitors for any subsequent changes, and ensures synchronization until it's time to cut over to MongoDB Atlas. Throughout this process, applications can maintain their normal read and write operations on the source database. When you're ready to perform the cutover, the connection string in the application is updated from the source database to the Atlas cluster, which completes the migration.

A typical migration workflow consists of the following steps:

## Step 1. Prepare
<a name="step-1.-prepare.6b32a1fe-99ef-55ce-9b95-a1e2678b6262"></a>
+ Assess the current MongoDB data size and workload. For instructions, see [Identify Application Workload](https://www.mongodb.com/docs/manual/data-modeling/schema-design-process/identify-workload/) in the MongoDB documentation.
+ Determine the size of the Atlas cluster on AWS.
+ Prepare for migration and cutover plans.

## Step 2. Deploy
<a name="step-2.-deploy.2bcf6471-16d2-5a63-bc20-fc82914c89c7"></a>
+ Set up a new environment on AWS for the MongoDB Atlas cluster, based on the sizing you determined in step 1.
+ Configure network access. For instructions, see [Configure IP Access List Entries](https://www.mongodb.com/docs/atlas/security/ip-access-list/#configure-ip-access-list-entries) in the MongoDB documentation.
+ Configure security for the destination cluster. For instructions, see [Configure Security Features for Clusters](https://www.mongodb.com/docs/atlas/setup-cluster-security/#configure-security-features-for-clusters) in the MongoDB documentation.

## Step 3. Migrate
<a name="step-3.-migrate.6654e663-d22b-5e10-9494-f7557ea18731"></a>
+ Configure the source and destination in the Atlas Live Migration Service.
+ Run the migration.
+ Cut over to MongoDB Atlas on AWS.

For more information about this migration option, see [Migrate a self-hosted MongoDB environment to MongoDB Atlas on AWS.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud.html)

### For MongoDB 6.0.8 and later
<a name="for-mongodb-6.0.8-and-later.470989d8-abbf-5236-9961-2800c70e0702"></a>

If both your source and destination clusters are running MongoDB 6.0.8 or a later version, you can use a guided live migration option (pull or push) to migrate your data from a source cluster to an Atlas MongoDB cluster:
+ [Live migration (pull)](https://www.mongodb.com/docs/atlas/setup-cluster-security/#configure-security-features-for-clusters)
+ [Live migration (push)](https://www.mongodb.com/docs/atlas/import/c2c-push-live-migration/#std-label-c2c-push-live-migration)

### For earlier MongoDB versions
<a name="for-earlier-mongodb-versions.bed7d0d8-b9e8-541b-9315-91df5c65c8b1"></a>

To migrate MongoDB versions earlier than 6.0.8, use one of the migration strategies discussed in the [MongoDB documentation](https://www.mongodb.com/docs/atlas/import/#earlier-mongodb-versions--live-migrate-to-atlas).
