---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-s3-import.html
---

# Importing files from Amazon S3
<a name="connector-s3-import"></a>

You can use the Amazon S3 Import connector to browse a source bucket, select files or folders, and import them into SDMA without downloading and re-uploading through the portal. SDMA copies the selected files into your library using AWS Deadline Cloud and verifies integrity during the transfer. When the job completes, the imported files appear as a new asset in your project.

## Overview
<a name="s3-import-overview"></a>

The Amazon S3 Import connector is initially created during deployment as a disabled connector named **S3 Import**. To use it, an administrator configures the source bucket credentials, associates the connector with an asset template, and enables it. You can then select **Import from S3** when creating an asset.

## Prerequisites
<a name="s3-import-prerequisites"></a>

SDMA needs an IAM role to access the source S3 bucket. Create a role in the account that owns the bucket, then store its ARN in the SDMA secret.

### Step 1: Create an IAM role in the source account
<a name="s3-import-role-setup"></a>

Create a role that grants read access to the source bucket. The role name **must** start with `SpatialDataManagementContentDerivation-`.

 **Permissions policy:**

```
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
        "arn:aws:s3:::<SOURCE_BUCKET_NAME>",
        "arn:aws:s3:::<SOURCE_BUCKET_NAME>/*"
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

```
# Connector invocation Lambda role (for bucket browsing)
aws lambda get-function \
  --function-name SpatialDataManagement-ConnectorInvocationFunction \
  --query 'Configuration.Role' --output text

# S3 Import Deadline queue role (for file copy jobs)
aws iam list-roles \
  --query "Roles[?contains(RoleName,'S3ImportDeadlineQueue')].Arn" --output text
```

Add these ARNs as trusted principals:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "<CONNECTOR_INVOCATION_ROLE_ARN>",
          "<S3_IMPORT_DEADLINE_QUEUE_ROLE_ARN>"
        ]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

### Step 2: Update the Secrets Manager secret
<a name="s3-import-secret"></a>

SDMA creates a secret named `SpatialDataManagementContentSecret-S3ImportConnector-<suffix>` during deployment with placeholder values. Update it with the role ARN from Step 1.

You can find the secret ARN in the Secrets Manager console (filter by prefix `SpatialDataManagementContentSecret-`) or in the connector configuration.

Update the secret value to the following JSON structure:

```
{
  "authType": "assumeRole",
  "roleArn": "arn:aws:iam::<SOURCE_ACCOUNT_ID>:role/SpatialDataManagementContentDerivation-<YOUR_SUFFIX>",
  "region": "<SOURCE_BUCKET_REGION>"
}
```

**Note**
If the source bucket is in the same account as SDMA, use the same account ID. The role still needs the `SpatialDataManagementContentDerivation-` prefix.

### Step 3: Configure VPC endpoint access (cross-account only)
<a name="s3-import-vpc-endpoint"></a>

If the source bucket is in a **different** AWS account, you must allowlist that account on the S3 VPC endpoint policy. Set the `S3ImportSourceAccountIds` CloudFormation parameter during deployment:

```
# Single account
--parameters S3ImportSourceAccountIds=111122223333

# Multiple accounts (comma-separated)
--parameters S3ImportSourceAccountIds=111122223333,111222333444
```

This adds the external account(s) to the `aws:PrincipalAccount` condition on the S3 VPC endpoint, allowing the SDMA Lambda (running inside the VPC) to access buckets in those accounts.

If the source bucket is in the **same** account as SDMA, this parameter is not needed.

## Connector configuration
<a name="s3-import-configuration"></a>

The Amazon S3 Import connector is initially created with placeholder values. Update the connector configuration in the Spatial Data Portal under **Connectors** > **S3 Import** > **Edit**.

### Full configuration example
<a name="_full-configuration-example"></a>

```
{
  "schemaVersion": "1.0.0",
  "name": "S3 Import",
  "defaultStepConfig": {
    "stepType": "deadlineJob",
    "deadlineConfig": {
      "farmId": "<DEADLINE_FARM_ID>",
      "queueId": "<S3_IMPORT_QUEUE_ID>",
      "builtInTemplate": "s3_import_asset"
    }
  },
  "resources": {
    "s3ListObjects": {
      "discover": {
        "type": "s3ListObjects",
        "securityConfig": {
          "type": "SecretCredentials",
          "secretArn": "<YOUR_SECRET_ARN>",
          "assumeRoleArn": "<S3_IMPORT_CONNECTOR_OPS_ROLE_ARN>"
        },
        "buckets": [
          {
            "region": "<SOURCE_BUCKET_REGION>",
            "bucketName": "<SOURCE_BUCKET_NAME>"
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
            "SecretArn": "<YOUR_SECRET_ARN>",
            "AssumeRoleArn": "<S3_IMPORT_CONNECTOR_OPS_ROLE_ARN>",
            "SourceBucket": "<SOURCE_BUCKET_NAME>",
            "Region": "<SOURCE_BUCKET_REGION>",
            "TemplateId": "<ASSET_TEMPLATE_ID>",
            "CasRootPrefix": "SpatialDataManagementAssets"
          },
          "output": {
            "assets": [
              {
                "assetTemplateIds": ["<ASSET_TEMPLATE_ID>"],
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

### Configuration fields
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

### Queue and fleet recommendations
<a name="_queue-and-fleet-recommendations"></a>

The Amazon S3 Import connector uses a dedicated Deadline Cloud queue (`spatial-data-management-s3-import-queue`) that is separate from the default content derivation queue. This keeps import jobs isolated from format conversion, rendering, and other processing work. You can modify this queue’s fleet configuration in the AWS Deadline Cloud console based on your usage needs. Consider the following fleet configuration options:
+ Use a service-managed fleet for most use cases. It scales automatically based on import demand.
+ Use high-bandwidth instances (for example, `c5n` or `m5n` families) for high-throughput imports involving thousands of files or multi-GB transfers.
+ Configure workers with no large local disk requirement. The worker streams, hashes, and uploads each file before the next batch starts.

## Enabling the connector
<a name="s3-import-enable"></a>

After editing and saving the connector:

1. Navigate to **Connectors** in the Spatial Data Portal.

1. Open the **S3 Import** connector and toggle **Enabled** to on.

1. Navigate to **Asset Templates** and open the template you want to use for imported assets.

1. Under **Connector Associations**, add the S3 Import connector.

## Importing files from S3
<a name="s3-import-usage"></a>

1. Ensure the project uses an asset template associated with the Amazon S3 Import connector. For more information, see [Enabling the connector](#s3-import-enable).

1. Navigate to the project and select **Create Asset**.

1. Enter an asset name and other properties, and choose **Next**.

1. Select the **Import from S3** radio button.

1. Choose the S3 Import connector from the dropdown (auto-selected if only one exists).

1. Browse the source bucket and select files or folders. Review the selection and choose **Submit**.

1. The import job is submitted to AWS Deadline Cloud. If a Deadline Cloud Monitor URL is configured on the connector, a link appears for tracking job progress.

1. When the job completes, the asset appears in the project with all imported files.

## How it works
<a name="s3-import-how-it-works"></a>

When you submit an import, SDMA submits a job to AWS Deadline Cloud that copies the selected files from the source bucket into your library in the background. The connector verifies each file’s integrity during transfer and automatically deduplicates any files that already exist, rather than copying them again.

## Troubleshooting
<a name="s3-import-troubleshooting"></a>

| Symptom | Resolution |
| --- | --- |
| Bucket browser does not load or shows an error | Check the secret value. The `roleArn` must start with `SpatialDataManagementContentDerivation-`. Verify the role exists in the source account and has `s3:ListBucket` permission on the configured bucket. |
| Deadline job fails with "AccessDenied" on AssumeRole | The source account role’s trust policy is missing the S3 Import Deadline queue role. Add it to the trust policy principal list. |
| Deadline job fails with "AccessDenied" on GetObject | The source account role’s permissions policy does not include `s3:GetObject` on the source bucket. Add the permission. |
| Bucket browser shows empty | The role may have `s3:ListBucket` but the bucket policy may deny cross-account access. Check the bucket policy in the source account. |
| "Cannot determine CAS bucket" error | The `ASSET_BUCKET_NAME` environment variable is not set on the connector invocation Lambda. This is set automatically during deployment — redeploy if missing. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
