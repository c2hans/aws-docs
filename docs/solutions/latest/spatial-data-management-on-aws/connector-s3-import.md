---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-s3-import.html
---

# Importing Files from Amazon S3

You can use the Amazon S3 Import connector to browse a source bucket, select files or folders, and import them into SDMA without downloading and re-uploading through the portal. SDMA copies the selected files into your library using AWS Deadline Cloud and verifies integrity during the transfer. When the job completes, the imported files appear as a new asset in your project.

Filters, `output` blocks, `${…​}` variables, and `$temp` values work the same way for every connector type. For more information, see [Trigger Filters](connector-configuration.md#trigger-filters), [Output Routing](connector-configuration.md#output-routing), [Variable Substitution](connector-configuration.md#variable-substitution), and [Intermediate State with $temp Variables](connector-configuration.md#temp-variables).

## Overview
<a name="s3-import-overview"></a>

The Amazon S3 Import connector is initially created during deployment as a disabled connector named **S3 Import**. To use it, an administrator configures the source bucket credentials, associates the connector with an asset template, and enables it. You can then select **Import from S3** when creating an asset.

## Prerequisites
<a name="s3-import-prerequisites"></a>

SDMA needs an IAM role to access the source S3 bucket. Create a role in the account that owns the bucket, then store its ARN in the SDMA secret.

### Step 1: Create an IAM Role in the Source Account
<a name="s3-import-role-setup"></a>

Create a role that grants read access to the source bucket. The role name **must** start with `SpatialDataManagementContentDerivation-`.

 **Permissions policy:**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetObject",
        "s3:GetBucketLocation"
      ],
      "Resource": [
        "arn:aws:s3:::<source-bucket-name>",
        "arn:aws:s3:::<source-bucket-name>/*"
      ]
    }
  ]
}
```

 **Trust policy:**

The role must trust the SDMA roles that will assume it at runtime. There are two callers:
+ The **connector invocation Lambda** assumes the role when browsing the bucket in the portal.
+ The **S3 Import Deadline queue worker** assumes the role when copying files during the import job.

Find these ARNs in your SDMA deployment:

```bash
# Connector invocation Lambda role (for bucket browsing)
aws lambda get-function \
  --function-name SpatialDataManagement-ConnectorInvocationFunction \
  --query 'Configuration.Role' --output text

# S3 Import Deadline queue role (for file copy jobs)
aws iam list-roles \
  --query "Roles[?contains(RoleName,'S3ImportDeadlineQueue')].Arn" --output text
```

Add these ARNs as trusted principals:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "<connector-invocation-role-arn>",
          "<s3-import-deadline-queue-role-arn>"
        ]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

### Step 2: Update the Secrets Manager Secret
<a name="s3-import-secret"></a>

SDMA creates a secret named `SpatialDataManagementContentSecret-S3ImportConnector-<suffix>` during deployment with placeholder values. Update it with the role ARN from Step 1.

You can find the secret ARN in the Secrets Manager console (filter by prefix `SpatialDataManagementContentSecret-`) or in the connector configuration.

Update the secret value to the following JSON structure:

```json
{
  "authType": "assumeRole",
  "roleArn": "arn:aws:iam::<source-account-id>:role/SpatialDataManagementContentDerivation-<your-suffix>",
  "region": "<source-bucket-region>"
}
```

**Note**
If the source bucket is in the same account as SDMA, use the same account ID. The role still needs the `SpatialDataManagementContentDerivation-` prefix.

### Step 3: Configure VPC Endpoint Access (Cross-Account Only)
<a name="s3-import-vpc-endpoint"></a>

If the source bucket is in a **different** AWS account, you must allowlist that account on the S3 VPC endpoint policy. Set the `S3ImportSourceAccountIds` CloudFormation parameter during deployment:

```bash
# Single account
--parameters S3ImportSourceAccountIds=111122223333

# Multiple accounts (comma-separated)
--parameters S3ImportSourceAccountIds=111122223333,111222333444
```

This adds the external account(s) to the `aws:PrincipalAccount` condition on the S3 VPC endpoint, allowing the SDMA Lambda (running inside the VPC) to access buckets in those accounts.

If the source bucket is in the **same** account as SDMA, this parameter is not needed.

## Connector Configuration
<a name="s3-import-configuration"></a>

The Amazon S3 Import connector is initially created with placeholder values. Update the connector configuration in the Spatial Data Portal under **Connectors** > **S3 Import** > **Edit**.

### Full Configuration Example
<a name="_full-configuration-example"></a>

```json
{
  "schemaVersion": "1.0.0",
  "name": "S3 Import",
  "defaultStepConfig": {
    "stepType": "deadlineJob",
    "deadlineConfig": {
      "farmId": "<deadline-farm-id>",
      "queueId": "<s3-import-queue-id>",
      "builtInTemplate": "s3_import_asset"
    }
  },
  "resources": {
    "s3ListObjects": {
      "discover": {
        "type": "s3ListObjects",
        "securityConfig": {
          "type": "SecretCredentials",
          "secretArn": "<your-secret-arn>",
          "assumeRoleArn": "<s3-import-connector-ops-role-arn>"
        },
        "buckets": [
          {
            "region": "<source-bucket-region>",
            "bucketName": "<source-bucket-name>"
          }
        ]
      }
    }
  },
  "triggers": [
    {
      "resources": ["project"],
      "events": ["onDemand"],
      "parameterDefinitions": {
        "assetName": { "type": "string", "required": true },
        "sourceKeys": { "type": "string", "required": true }
      },
      "steps": [
        {
          "description": "Write sourceKeys manifest to CAS",
          "stepType": "casPutObject",
          "payload": { "fields": ["parameters"] }
        },
        {
          "description": "Stream copy files from source to CAS",
          "stepType": "deadlineJob",
          "template": "template.yaml",
          "parameters": {
            "ManifestKey": "${$temp.objectKey}",
            "ManifestBucket": "${$temp.bucket}",
            "ManifestHash": "${$temp.contentHash}",
            "SecretArn": "<your-secret-arn>",
            "AssumeRoleArn": "<s3-import-connector-ops-role-arn>",
            "SourceBucket": "<source-bucket-name>",
            "Region": "<source-bucket-region>",
            "TemplateId": "<asset-template-id>",
            "CasRootPrefix": "SpatialDataManagementAssets"
          },
          "output": {
            "assets": [
              {
                "assetTemplateIds": ["<asset-template-id>"],
                "filter": { "fileNameRegex": "^assets\\.json$" }
              }
            ]
          }
        }
      ]
    }
  ]
}
```

### Configuration Fields
<a name="_configuration-fields"></a>

The following fields are pre-filled by SDMA during deployment and do not require manual configuration:
+  `defaultStepConfig.deadlineConfig.farmId` — Deadline Cloud farm ID
+  `defaultStepConfig.deadlineConfig.queueId` — S3 Import queue ID
+  `resources.s3ListObjects.discover.securityConfig.secretArn` — Secret ARN
+  `resources.s3ListObjects.discover.securityConfig.assumeRoleArn` — S3ImportConnectorOps role ARN
+  `deadlineJob` step > `parameters.SecretArn` — Same secret ARN (for Deadline worker)
+  `deadlineJob` step > `parameters.AssumeRoleArn` — Same ops role ARN (for Deadline worker)

The following fields require manual configuration:

| Field | Description |
| --- | --- |
|  `resources.s3ListObjects.discover.buckets[].bucketName`  | Name of the source S3 bucket to browse and import from. |
|  `resources.s3ListObjects.discover.buckets[].region`  | AWS Region of the source bucket. |
|  `deadlineJob` step > `parameters.SourceBucket`  | Same bucket name as above (used by the Deadline worker to read files). |
|  `deadlineJob` step > `parameters.Region`  | Same region as above. |
|  `deadlineJob` step > `parameters.TemplateId`  | The asset template ID to associate imported assets with. |
|  `deadlineJob` step > `output.assets[].assetTemplateIds`  | Same template ID as above (for output routing). |

### Queue and Fleet Recommendations
<a name="_queue-and-fleet-recommendations"></a>

An import is a network job. Every byte passes through the worker. The worker reads each file from the source bucket, and uploads it to your library unless your library already holds it. Network bandwidth sets how fast an import runs, so choose the fleet for bandwidth first.

The Amazon S3 Import connector uses a dedicated Deadline Cloud queue (`spatial-data-management-s3-import-queue`) that is separate from the default content derivation queue. The two queues share one service-managed fleet, `spatial-data-management-main-fleet`, which scales with demand. A change to that fleet in the AWS Deadline Cloud console applies to both queues. Consider the following fleet options:
+  **One import runs on one worker.** An import is a single task, so its speed is the network bandwidth of the one worker that runs it. A larger instance makes an import faster. More workers only let more imports run at the same time.
+  **Choose instance types for network bandwidth.** Use network-optimized types, such as the `c5n` or `m5n` families. Compare the network bandwidth that is listed for each size, not its vCPUs or memory. In a service-managed fleet, set the allowed instance types to the ones that you choose. The fleet also runs content derivation, so this changes the instances, and the cost, of derivation jobs too.
+  **Use large sizes.** Sizes of 4xlarge and smaller list an "up to" bandwidth that they hold only in short bursts. By default the fleet asks for workers with 16 vCPUs, which fall in that group. Larger sizes sustain the bandwidth that they list.
+  **Plan for twice the inbound traffic.** A file that is new to your library is read from the source twice, once to hash it and once to upload it. Inbound traffic is about twice the size of the new data. Inbound and outbound bandwidth are separate limits, and inbound is the one that limits an import.
+  **Keep the source bucket in the same Region as SDMA.** A source bucket in another Region is slower, and AWS bills the transfer.
+  **Check the job log.** The job prints its network rate (`net`) and CPU use (`cpu`) every minute. If `net` stays well below the instance’s listed bandwidth, raise `FileWorkers` and `PartConcurrency`. See [Tune an Import](#s3-import-tuning).
+  **Do not size for disk or memory.** Workers need no large local disk, because the job never writes file data to it. Memory only holds the parts that are in flight, and the settings in [Tune an Import](#s3-import-tuning) control that amount.

## Enabling the Connector
<a name="s3-import-enable"></a>

After editing and saving the connector:

1. Navigate to **Connectors** in the Spatial Data Portal.

1. Open the **S3 Import** connector and toggle **Enabled** to on.

1. Navigate to **Asset Templates** and open the template you want to use for imported assets.

1. Under **Connector Associations**, add the S3 Import connector.

## Importing Files from S3
<a name="s3-import-usage"></a>

1. Ensure the project uses an asset template associated with the Amazon S3 Import connector. For more information, see [Enabling the Connector](#s3-import-enable).

1. Navigate to the project and select **Create Asset**.

1. Enter an asset name and other properties, and choose **Next**.

1. Select the **Import from S3** radio button.

1. Choose the S3 Import connector from the dropdown (auto-selected if only one exists).

1. Browse the source bucket and select files or folders. Review the selection and choose **Submit**.

1. The import job is submitted to AWS Deadline Cloud. If a Deadline Cloud Monitor URL is configured on the connector, a link appears for tracking job progress.

1. When the job completes, the asset appears in the project with all imported files.

## How It Works
<a name="s3-import-how-it-works"></a>

When you submit an import, a job on AWS Deadline Cloud copies the selected files from the source bucket into your library in the background.
+ The job reads each file from the source bucket in ranges and hashes it first. If your library already holds a file with that hash, the job skips the upload.
+ Files that are not already in your library are copied. If a source file changes while the job copies it, the job rejects the file instead of storing a mismatch.
+ Several files copy at the same time, each in its own process. No file data is written to local disk.
+ Importing files that your library already holds is much faster than the first import, because nothing is uploaded.

### Tune an Import
<a name="s3-import-tuning"></a>

Three optional parameters on the `deadlineJob` step control how much work runs at once. Add them to the step’s `parameters`:

| Parameter | Default | Description |
| --- | --- | --- |
|  `FileWorkers`  |  `8`  | Files copied at the same time, one process each. |
|  `PartConcurrency`  |  `8`  | Ranged reads, and part uploads, in flight for each file. |
|  `PartSizeMiB`  |  `64`  | Size of each part, in MiB. |

Peak memory use is about 2 × `FileWorkers` × `PartConcurrency` × `PartSizeMiB`. At the defaults, that is 8 GiB. On workers with less memory, lower these values.

```json
"parameters": {
  "FileWorkers": "4",
  "PartConcurrency": "4",
  "PartSizeMiB": "32"
}
```

## Troubleshooting
<a name="s3-import-troubleshooting"></a>

| Symptom | Resolution |
| --- | --- |
| Bucket browser does not load or shows an error | Check the secret value. The `roleArn` must start with `SpatialDataManagementContentDerivation-`. Verify the role exists in the source account and has `s3:ListBucket` permission on the configured bucket. |
| Deadline job fails with "AccessDenied" on AssumeRole | The source account role’s trust policy is missing the S3 Import Deadline queue role. Add it to the trust policy principal list. |
| Deadline job fails with "AccessDenied" on GetObject | The source account role’s permissions policy does not include `s3:GetObject` on the source bucket. Add the permission. |
| Bucket browser shows empty | The role may have `s3:ListBucket` but the bucket policy may deny cross-account access. Check the bucket policy in the source account. |
| "Cannot determine CAS bucket" error | The `ASSET_BUCKET_NAME` environment variable is not set on the connector invocation Lambda. This is set automatically during deployment — redeploy if missing. |
