---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/lakehouse-analytics-starter-package.html
---

# Lakehouse Analytics Starter Package
<a name="lakehouse-analytics-starter-package"></a>

The Lakehouse Analytics Starter Package deploys a complete analytics lakehouse: S3 data lake, Glue cataloging and ETL, data quality enforcement, Athena and Redshift querying, and QuickSight BI — end-to-end with a single deploy command.

 **Lakehouse Analytics starter kit architecture**

![Lakehouse Analytics starter kit — S3 storage with Glue ETL and Athena/Redshift/QuickSight consumption.](https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/images/lakehouse_analytics.png)

This architecture is particularly effective when:

1. Data flows through ingestion, processing, quality validation, and consumption layers.

1. Analytics are consumed via Athena, Redshift, and QuickSight.

1. Data quality enforcement and ETL workflows are required.

1. You want a validated, end-to-end reference across the six data-foundations capabilities plus governance.

## Storage and Governance Components
<a name="storage-and-governance-components"></a>
+  **Data Lake** - S3 raw and transformed buckets, KMS-encrypted
+  **Glue Catalog** - KMS-encrypted Data Catalog with automated schema discovery
+  **Lake Formation Settings** - Configured for IAM-delegated access with governance mode
+  **IAM Roles** - `data-admin`, `data-user`, `glue-etl` with least-privilege policies
+  **Audit** - Encrypted S3 audit bucket and CloudTrail audit trail

## DataOps Domain Components
<a name="dataops-domain-components-4"></a>
+  **DataOps Project** - Sample Glue database with Lake Formation grants
+  **Glue Crawler** - Catalogs data in the transformed bucket
+  **Glue ETL Job** - Sample PySpark transformation script
+  **Glue Data Quality** - Rulesets, DQ evaluation job, and workflow that runs DQ after the crawler

## Consumption Components
<a name="consumption-components"></a>
+  **Athena Workgroup** - SQL querying over the data lake
+  **Redshift Cluster** - Multi-AZ with cross-region snapshot copy
+  **QuickSight Account** - Resource-access service role, VPC connection, `readers` and `authors` groups
+  **QuickSight Data Sources** - Over Athena and Redshift

## Deployment Instructions
<a name="deployment-instructions-6"></a>

### Manual CLI Deploy Method
<a name="manual-cli-deploy-method-4"></a>

#### Prerequisites
<a name="prerequisites-9"></a>

Before deploying the Lakehouse Analytics Starter Package using the CLI method, verify you have:

1. AWS CLI configured with appropriate credentials

1. Node.js 22.x or later and npm/npx 10.x or later installed

1. AWS CDK bootstrapped in your target account and region

1. A VPC with at least 3 subnets across 3 Availability Zones (required for Redshift multi-AZ and QuickSight VPC connection)

1. A QuickSight subscription (records the identity region used by group and folder permissions)

#### Deployment Steps
<a name="deployment-steps-8"></a>

 **Step 1: Clone the MDAA repository**

```
git clone https://github.com/aws/modern-data-architecture-accelerator.git &&
cd modern-data-architecture-accelerator
```

 **Step 2: Configure your deployment**
+ Copy the starter kit files:

```
cp -r starter_kits/lakehouse_analytics my_lakehouse
cd my_lakehouse
```
+ Edit `mdaa.yaml` to set:

```
organization: <your-unique-org-name>
context:
  vpc_id: <your vpc id>
  subnet_id_1: <your subnet id 1>
  subnet_id_2: <your subnet id 2>
  subnet_id_3: <your subnet id 3>
  notification_email: <your email>
  vpc_cidr: <vpc cidr>
  backup_region: <region for Redshift snapshot copy>
  qs_identity_region: <region where QuickSight was subscribed>
```
+ Review the commented-out CDK Nag suppression blocks in `governance/roles.yaml`.

 **Step 3: Deploy the solution**

```
npx @aws-mdaa/cli ls
npx @aws-mdaa/cli synth
npx @aws-mdaa/cli deploy
```

 **Step 4: Verify deployment**
+ Verify the S3 buckets, Glue database and crawler, Redshift cluster, Athena workgroup, and QuickSight data sources have been created.

## Usage Instructions
<a name="usage-instructions-6"></a>

The deploy creates the `readers` and `authors` QuickSight groups and grants them access, but does not add members. Add your QuickSight user to a group before data sources become visible.

1.  **Load sample data and run the pipeline** — See the `USAGE.md` in the starter kit directory for instructions on loading sample data, running the crawler, and executing the Glue ETL and DQ workflow.

1.  **Query with Athena** — Use the Athena workgroup created by the deployment against the sample database.

1.  **Query Redshift** — Connect via the QuickSight data source or `redshift-data` API using the roles configured by the starter kit.

1.  **Build dashboards in QuickSight** — Use the Athena and Redshift data sources under **Datasets → New dataset → FROM EXISTING DATA SOURCES**.

For more detailed information, refer to the README.md and USAGE.md files in the starter\_kits/lakehouse\_analytics directory of the MDAA repository.
