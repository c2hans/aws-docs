---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-s3.html
---

# Amazon S3 connector
<a name="connector-s3"></a>

The Amazon S3 connector is a multi-purpose primitive that can publish structured metadata to S3 buckets, derive metadata from S3-hosted CSV or JSON files, and serve reference data from S3 files as selectable field values during template authoring.

Step types: `s3PutObject`, `s3DeleteObject`

## Roles
<a name="s3-roles"></a>

| Role | Description |
| --- | --- |
| Publisher | Writes structured JSON metadata to an S3 bucket when asset lifecycle events occur. Use `s3PutObject` to create objects and `s3DeleteObject` to remove them. |
| Metadata lookup | Reads a CSV or JSON file from S3, matches records to SDMA files or assets by a key field, and writes matched values as metadata attributes. Uses the `s3Lookup` operation in the lookup-derivation model. |
| Field provider for templates | Serves values from an S3-hosted CSV or JSON file as selectable options in the Spatial Data Portal during template authoring and metadata entry. Uses the connector-level `fieldMappings` \+ `s3Config` shorthand without triggers. |
| Step type | Participates in multi-step triggers alongside other step types. An `s3PutObject` step can write metadata to S3 as one step in a larger workflow that also calls REST APIs, invokes Lambda functions, or sends EventBridge events. |

## Prerequisites
<a name="s3-prerequisites"></a>

1. Identify or create the target S3 bucket.

1. Create an IAM role:
   +  **Role name** must start with `SpatialDataManagementContentPublisher-` (publish connectors) or `SpatialDataManagementContentDerivation-` (derive connectors).
   +  **Trust policy** must allow the SDMA connector invocation Lambda to assume it:

     ```
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Principal": {
             "AWS": [
               "<CONNECTOR_INVOCATION_ROLE_ARN>",
               "<ASYNC_CONNECTOR_INVOCATION_ROLE_ARN>"
             ]
           },
           "Action": "sts:AssumeRole"
         }
       ]
     }
     ```

     Replace `<CONNECTOR_INVOCATION_ROLE_ARN>` and `<ASYNC_CONNECTOR_INVOCATION_ROLE_ARN>` with the execution role ARNs of the connector invocation Lambda functions in your SDMA deployment.

     If you have AWS CLI access, you can find these values by running:

     ```
     aws lambda get-function \
       --function-name SpatialDataManagement-ConnectorInvocationFunction \
       --query 'Configuration.Role' --output text

     aws lambda get-function \
       --function-name SpatialDataManagement-ConnectorInvocationAsyncFunction \
       --query 'Configuration.Role' --output text
     ```

     Alternatively, in the [Lambda console](https://console.aws.amazon.com/lambda/), open the `SpatialDataManagement-ConnectorInvocationFunction` and `SpatialDataManagement-ConnectorInvocationAsyncFunction` functions and find the role name for each under **Configuration** > **Permissions**. Use these names to construct the full ARNs (for example, `arn:aws:iam::<ACCOUNT_ID>:role/<CONNECTOR_INVOCATION_ROLE_NAME>`).
   +  **Permissions policy** — scope to the specific bucket and operations needed:
     + For publish: `s3:PutObject` (and `s3:DeleteObject` if using delete triggers).
     + For derive/lookup: `s3:GetObject` on the source file.

## Using S3 as a publisher
<a name="s3-as-publisher"></a>

A publish connector writes structured JSON to an S3 bucket when asset events occur. This is useful for feeding data lakes, downstream processing pipelines, or any system that consumes structured data from S3.

### Example: publish asset metadata to S3 on create or update
<a name="_example-publish-asset-metadata-to-s3-on-create-or-update"></a>

```
{
  "defaultStepConfig": {
    "stepType": "s3PutObject",
    "s3Config": {
      "bucketName": "<TARGET_BUCKET>",
      "securityConfig": {
        "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentPublisher-S3Archive",
        "type": "AssumeRole"
      }
    }
  },
  "fieldMappings": [
    { "source": "asset.assetId", "target": "assetId" },
    { "source": "asset.assetName", "target": "name" },
    { "source": "asset.metadataAttributes.site_code", "target": "siteCode" }
  ],
  "triggers": [
    {
      "description": "Publish asset metadata to S3 on create or update",
      "resources": ["asset"],
      "events": ["create", "update"],
      "steps": [
        {
          "s3Config": {
            "objectKey": "assets/${project.projectId}/${asset.assetId}.json"
          },
          "payload": {
            "format": "json",
            "fields": ["assetId", "name", "siteCode"]
          }
        }
      ]
    }
  ]
}
```

The `objectKey` supports `${variable}` substitution, so each asset gets its own S3 object organized by project. The `payload.fields` array selects which mapped fields to include — only `assetId`, `name`, and `siteCode` are written, even though the connector could map more fields.

## Using S3 for metadata lookup
<a name="s3-as-lookup"></a>

An S3 derive connector reads a CSV or JSON file from S3 and matches records to SDMA files or assets. This is the bulk metadata enrichment pattern — upload a spreadsheet of metadata once, and every asset created under the template gets its files enriched automatically.

### Example: enrich file metadata from a CSV
<a name="_example-enrich-file-metadata-from-a-csv"></a>

```
{
  "s3Config": {
    "bucketName": "<SOURCE_BUCKET>",
    "region": "us-west-2",
    "csvOptions": { "delimiter": ",", "hasHeader": true },
    "objectKey": "scan_metadata.csv",
    "securityConfig": {
      "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentDerivation-S3Lookup",
      "type": "AssumeRole"
    }
  },
  "fieldMappings": [
    { "source": "qc_status", "target": "file.qc_status" },
    { "source": "processing_stage", "target": "file.processing_stage" },
    { "source": "operator_id", "target": "file.operator_id" },
    { "source": "scan_quality", "target": "file.scan_quality" }
  ],
  "triggers": [
    {
      "description": "Enrich files via CSV as they are uploaded",
      "resources": ["asset"],
      "events": ["uploadComplete", "onDemand"],
      "derivation": {
        "op": "s3Lookup",
        "applyTo": {
          "resource": "file",
          "scope": "all",
          "match": {
            "source": "file_name",
            "target": "file.path:basename"
          },
          "onNoMatch": "skip"
        }
      }
    }
  ]
}
```

The `match` block joins external records to SDMA files — here, matching the CSV’s `file_name` column against each file’s basename. The `fieldMappings` at the connector level define which CSV columns become which file metadata attributes.

For full details on the lookup-derivation model, `applyTo` matching, and CSV options, see [Metadata lookup and enrichment](connector-derivation.md).

## Using S3 as a field provider for templates
<a name="s3-as-field-provider"></a>

An S3 connector can serve values from a CSV or JSON file as selectable options in the Spatial Data Portal. When a template author defines a metadata attribute, the Portal queries the connector to populate dropdown lists, typeaheads, or cascading field selections.

This uses the connector-level `fieldMappings` \+ `s3Config` shorthand — no triggers, no `resources` block. The connector exists purely to provide reference data for template authoring and metadata entry.

### Example: serve site codes from a CSV for template authoring
<a name="_example-serve-site-codes-from-a-csv-for-template-authoring"></a>

```
{
  "s3Config": {
    "bucketName": "<REFERENCE_DATA_BUCKET>",
    "objectKey": "sites.csv",
    "csvOptions": { "delimiter": ",", "hasHeader": true },
    "securityConfig": {
      "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentDerivation-FieldProvider",
      "type": "AssumeRole"
    }
  },
  "fieldMappings": [
    { "source": "SITE_ID", "target": "asset.site_id" },
    { "source": "SITE_NAME", "target": "asset.site_name" }
  ]
}
```

This connector has no triggers — it does not run on lifecycle events. Its value is in what it exposes: the distinct values of `SITE_ID` and `SITE_NAME` from the CSV, presented as selectable options when users create or edit assets under templates that reference this connector.

Field mappings can include an `options` object to declare cascading dependencies between fields — for example, selecting a site ID can filter the available site names.

## Using S3 as a step type in multi-step triggers
<a name="s3-as-step-type"></a>

The `s3PutObject` and `s3DeleteObject` step types can participate in multi-step triggers alongside other step types. For example, a trigger might write metadata to S3, then invoke a Lambda function to post-process it:

```
"steps": [
  {
    "stepType": "s3PutObject",
    "s3Config": {
      "objectKey": "raw/${asset.assetId}.json"
    },
    "payload": {
      "format": "json",
      "fields": ["assetId", "name"]
    }
  },
  {
    "stepType": "lambdaInvoke",
    "lambdaConfig": {
      "functionArn": "arn:aws:lambda:<REGION>:<ACCOUNT_ID>:function:post-process"
    }
  }
]
```

## Configuration fields
<a name="s3-config-fields"></a>

### Connector-level fields
<a name="_connector-level-fields"></a>

| Field | Required | Description |
| --- | --- | --- |
|  `s3Config.bucketName`  | Yes | Target S3 bucket name. |
|  `s3Config.region`  | No | AWS Region of the S3 bucket. Defaults to the SDMA deployment region. |
|  `s3Config.securityConfig`  | Yes | Authentication configuration. Must use `AssumeRole` type. |
|  `s3Config.csvOptions.hasHeader`  | No | Whether the CSV has a header row. Defaults to `true`. |
|  `s3Config.csvOptions.delimiter`  | No | CSV delimiter character. Defaults to `,`. |

### Step-level fields
<a name="_step-level-fields"></a>

| Field | Required | Description |
| --- | --- | --- |
|  `s3Config.objectKey`  | Yes | S3 object key. Supports `${variable}` substitution. |
|  `s3Config.bucketName`  | No | Overrides the connector-level bucket for this step. |
|  `payload.format`  | No | Output format. Currently only `json` is supported. |
|  `payload.fields`  | No | Array of field names to include. If omitted, all mapped fields are included. |
