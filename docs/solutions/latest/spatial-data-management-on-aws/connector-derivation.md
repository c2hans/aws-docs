---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-derivation.html
---

# Metadata lookup and enrichment
<a name="connector-derivation"></a>

Metadata lookup is a role that S3, REST API, and DynamoDB connectors can fill. When a derive connector includes a `derivation` block in its trigger configuration, it uses the lookup-derivation execution model: fetch records from an external data source, match them to SDMA files or assets by a key field, and write the matched values as governed metadata attributes.

This is how you automate bulk metadata enrichment. A domain expert defines the external data source, the matching rules, and the field mappings once on a connector. That connector is approved on a template. From that point on, every asset created under that template is automatically enriched — files are matched to external records, metadata is applied, and the asset record is updated with provenance showing where each value came from.

**Important**
Derive connectors use the IAM role prefix `SpatialDataManagementContentDerivation-` (not `SpatialDataManagementContentPublisher-` used by publish connectors). SDMA validates the role name prefix and tests role assumption when the connector is created.

## Create a derive connector with lookup
<a name="derivation-create"></a>

1. In the Spatial Data Portal, go to **Library settings** > **Connectors**.

1. Choose the **Derive content** tab.

1. Choose **Create deriver**.

1. Enter a connector name.

1. For **Connector type**, select the type that matches your data source:
   +  **Amazon S3 CSV file import** — for `s3Lookup` operations (S3 connector type)
   +  **Amazon DynamoDB import** — for `dynamodbLookup` operations (DynamoDB connector type)
   +  **REST API import** — for `restLookup` operations (REST connector type)

1. Paste the connector configuration JSON (see the operation sections below) into the JSON editor.

1. Choose **Create**.

The connector type you select determines the protocol and authentication model. The `derivation` block in the trigger configuration is what makes it a lookup connector — the same S3, DynamoDB, or REST connector type can also fill publish, resource provision, or content production roles depending on its configuration.

## Lookup operations
<a name="derivation-operations"></a>

The lookup-derivation model supports the following operations (used as the `derivation.op` value).

| Operation | Description |
| --- | --- |
|  `s3Lookup`  | Reads a CSV or JSON file from Amazon S3 and matches records to resources. Useful for bulk metadata import from spreadsheets or data exports. |
|  `restLookup`  | Calls a REST API endpoint and matches response records to resources. Useful for enriching metadata from external catalogs or databases. |
|  `dynamodbLookup`  | Performs a GetItem on an Amazon DynamoDB table and applies the result to a resource. Useful for single-record lookups by key. |

## Record matching
<a name="derivation-matching"></a>

The `applyTo` block controls how external records are matched to resources:
+  `resource` – The resource type to apply derived metadata to (`file` or `asset`).
+  `match.source` – The field in the external record used for matching (for example, `filename`).
+  `match.target` – The resource field to match against (for example, `file.path:basename`). Supports transforms: `:basename`, `:ext`, `:tolower`.
+  `onNoMatch` – Behavior when no match is found. Currently only `skip` (default) is supported, which continues to the next record.
+  `mappingPolicy` – Controls how derived attributes interact with existing attributes: `inherit` (default) or `override`.
+  `responseFieldMapping` – Maps external record fields to resource metadata attributes.

## Amazon S3 lookup
<a name="s3-lookup"></a>

The `s3Lookup` operation reads a file from S3 and parses it into records. It supports CSV and JSON content types.

### Prerequisites
<a name="s3-lookup-prerequisites"></a>

1. Upload the source data file (CSV or JSON) to an S3 bucket.

1. Create an IAM role with the following:
   +  **Role name** must start with `SpatialDataManagementContentDerivation-` (for example, `SpatialDataManagementContentDerivation-MyS3Lookup`).
   +  **Trust policy** must allow the SDMA solution account to assume it:

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
   +  **Permissions policy** must grant `s3:GetObject` on the source file:

     ```
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": "s3:GetObject",
           "Resource": "arn:aws:s3:::<YOUR_BUCKET_NAME>/metadata/*"
         }
       ]
     }
     ```

### CSV options
<a name="s3-lookup-csv-options"></a>

For CSV files, the following options are available in the trigger-level `derivation.s3Config.csvOptions`:
+  `hasHeader` – Whether the CSV has a header row. Defaults to `true`. When `true`, column names from the header are used as field names. When `false`, columns are indexed as `0`, `1`, `2`, and so on
+  `delimiter` – CSV delimiter character. Defaults to `,`.

### Example
<a name="s3-lookup-example"></a>

This example reads a CSV file from S3 and applies metadata to files based on filename matching:

```
{
  "s3Config": {
    "bucketName": "my-metadata-bucket",
    "securityConfig": {
      "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentDerivation-MyS3Lookup",
      "type": "AssumeRole"
    }
  },
  "triggers": [
    {
      "description": "Derive file metadata from CSV on asset creation",
      "resources": ["asset"],
      "events": ["create"],
      "derivation": {
        "op": "s3Lookup",
        "sourceContentType": "csv",
        "s3Config": {
          "objectKey": "metadata/${project.projectId}/attributes.csv"
        },
        "applyTo": {
          "resource": "file",
          "scope": "all",
          "match": {
            "source": "filename",
            "target": "file.path:basename"
          },
          "onNoMatch": "skip",
          "responseFieldMapping": [
            { "source": "department", "target": "file.department" },
            { "source": "classification", "target": "file.classification" }
          ]
        }
      }
    }
  ]
}
```

## REST API lookup
<a name="rest-lookup"></a>

The `restLookup` operation calls a REST API endpoint and parses the response into records. It supports GET and POST methods, query parameter substitution, and response filtering.

### Prerequisites
<a name="rest-lookup-prerequisites"></a>

1. Identify the REST API endpoint that returns the metadata to derive.

1. If using API key, token, or basic auth, store the credentials in AWS Secrets Manager.

1. Create an IAM role with the following:
   +  **Role name** must start with `SpatialDataManagementContentDerivation-` (for example, `SpatialDataManagementContentDerivation-MyRestLookup`).
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
   +  **Permissions policy** must grant access to the Secrets Manager secret (if using API key, token, or basic auth):

     ```
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": "secretsmanager:GetSecretValue",
           "Resource": "arn:aws:secretsmanager:<REGION>:<ACCOUNT_ID>:secret:<SECRET_NAME>"
         }
       ]
     }
     ```

### Example
<a name="rest-lookup-example"></a>

This example calls a REST API to look up file metadata from an external catalog by project ID:

```
{
  "restConfig": {
    "apiBase": "https://api.example.com/v1",
    "securityConfig": {
      "type": "ApiKey",
      "secretArn": "arn:aws:secretsmanager:<REGION>:<ACCOUNT_ID>:secret:<SECRET_NAME>",
      "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentDerivation-MyRestLookup"
    }
  },
  "triggers": [
    {
      "description": "Derive asset metadata from external catalog",
      "resources": ["asset"],
      "events": ["create"],
      "derivation": {
        "op": "restLookup",
        "restConfig": {
          "method": "GET",
          "path": "/records",
          "queryParams": {
            "projectId": "${project.projectId}"
          },
          "responseFilter": "data.items"
        },
        "applyTo": {
          "resource": "file",
          "scope": "all",
          "match": {
            "source": "filename",
            "target": "file.path:basename"
          },
          "responseFieldMapping": [
            { "source": "category", "target": "file.category" },
            { "source": "owner", "target": "file.owner" }
          ]
        }
      }
    }
  ]
}
```

The `responseFilter` field uses dot notation to extract a nested array from the API response (for example, `data.items` extracts the `items` array from `{ "data": { "items": […​] } }`).

## Amazon DynamoDB lookup
<a name="ddb-lookup"></a>

The `dynamodbLookup` operation performs a GetItem on a DynamoDB table and returns the item as a single record. It automatically deserializes DynamoDB attribute types (S, N, BOOL, M, L) to native values.

### Prerequisites
<a name="ddb-lookup-prerequisites"></a>

1. Create a DynamoDB table with the metadata to derive.

1. Create an IAM role with the following:
   +  **Role name** must start with `SpatialDataManagementContentDerivation-` (for example, `SpatialDataManagementContentDerivation-MyDynamoDBLookup`).
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
   +  **Permissions policy** must grant `dynamodb:GetItem` on the target table:

     ```
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": "dynamodb:GetItem",
           "Resource": "arn:aws:dynamodb:<REGION>:<ACCOUNT_ID>:table/<TABLE_NAME>"
         }
       ]
     }
     ```

### Partition key resolution
<a name="ddb-lookup-key-resolution"></a>

The partition key value can be resolved in two ways:
+  **Explicit** – Set `dynamodbConfig.partitionKeyValue` to a template string (for example, `${asset.assetId}`).
+  **From match config** – If `partitionKeyValue` is omitted, the value is derived from the `applyTo.match.target` field. For example, if `match.target` is `file.path:basename`, the file’s basename is used as the partition key value.

### Example
<a name="ddb-lookup-example"></a>

This example looks up file metadata from a DynamoDB table using the filename as the partition key:

```
{
  "dynamodbConfig": {
    "tableName": "file-metadata-table",
    "partitionKey": "filename",
    "region": "us-west-2",
    "securityConfig": {
      "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentDerivation-MyDynamoDBLookup",
      "type": "AssumeRole"
    }
  },
  "triggers": [
    {
      "description": "Derive file metadata from DynamoDB",
      "resources": ["asset"],
      "events": ["create"],
      "derivation": {
        "op": "dynamodbLookup",
        "dynamodbConfig": {
          "consistentRead": true
        },
        "applyTo": {
          "resource": "file",
          "scope": "all",
          "match": {
            "source": "filename",
            "target": "file.path:basename"
          },
          "responseFieldMapping": [
            { "source": "status", "target": "file.status" },
            { "source": "priority", "target": "file.priority" }
          ]
        }
      }
    }
  ]
}
```

**Note**
The `dynamodbConfig` at the trigger’s `derivation` level is merged with the connector-level `dynamodbConfig`. Use the trigger-level config to override specific fields like `consistentRead` per trigger.

## Copy fields
<a name="copy-fields"></a>

The `copyFields` configuration provides a shortcut for copying a set of fields from the external record to resource metadata using prefix-based matching. Instead of listing individual field mappings, you specify a source prefix and target prefix:

```
"copyFields": {
  "sourcePrefix": "metadata.",
  "targetPrefix": "file."
}
```

This copies all fields starting with `metadata.` from the external record to the resource, replacing the prefix with `file.`. For example, `metadata.classification` becomes `file.classification`.

## Record ID mapping
<a name="record-id-mapping"></a>

The `recordIdMapping` configuration stores the external record’s identifier as a metadata attribute on the matched resource:

```
"recordIdMapping": {
  "target": "file.external_id"
}
```

This writes the record’s key (from the external source) to the `external_id` attribute on the matched file.

## Configuration fields
<a name="derivation-config-fields"></a>

The following tables describe the configuration fields for the metadata derivation connector.

### Connector-level fields
<a name="_connector-level-fields"></a>

| Field | Required | Description |
| --- | --- | --- |
|  `s3Config.bucketName`  | Yes (for `s3Lookup`) | Target S3 bucket name. |
|  `s3Config.securityConfig`  | Yes (for `s3Lookup`) | Authentication configuration. Must use `AssumeRole` type. |
|  `restConfig.apiBase`  | Yes (for `restLookup`) | Base URL for the REST API. |
|  `restConfig.securityConfig`  | Yes (for `restLookup`) | Authentication configuration. Supports `ApiKey`, `TokenAuth`, and `BasicAuth` types. |
|  `dynamodbConfig.tableName`  | Yes (for `dynamodbLookup`) | DynamoDB table name. |
|  `dynamodbConfig.partitionKey`  | Yes (for `dynamodbLookup`) | Partition key attribute name. |
|  `dynamodbConfig.region`  | No | AWS Region of the DynamoDB table. |
|  `dynamodbConfig.securityConfig`  | Yes (for `dynamodbLookup`) | Authentication configuration. Must use `AssumeRole` type. |

### Trigger-level derivation fields
<a name="_trigger-level-derivation-fields"></a>

| Field | Required | Description |
| --- | --- | --- |
|  `derivation.op`  | Yes | Derivation operation: `s3Lookup`, `restLookup`, or `dynamodbLookup`  |
|  `derivation.sourceContentType`  | No | Content type of the source data. `csv` (default) or `json`. Applies to `s3Lookup`. |
|  `derivation.s3Config.objectKey`  | Yes (for `s3Lookup`) | S3 object key with `${variable}` substitution support. |
|  `derivation.s3Config.csvOptions.hasHeader`  | No | Whether the CSV has a header row. Defaults to `true`. |
|  `derivation.s3Config.csvOptions.delimiter`  | No | CSV delimiter character. Defaults to `,`. |
|  `derivation.restConfig.method`  | No | HTTP method for `restLookup`. Defaults to `GET`. |
|  `derivation.restConfig.path`  | Yes (for `restLookup`) | API path appended to connector-level `restConfig.apiBase`. |
|  `derivation.restConfig.queryParams`  | No | Query parameters with `${variable}` substitution support. |
|  `derivation.restConfig.responseFilter`  | No | Dot-notation path to extract records from the API response. |
|  `derivation.dynamodbConfig.partitionKeyValue`  | No | Partition key value template with `${variable}` support. If omitted, derived from `applyTo.match`. |
|  `derivation.dynamodbConfig.consistentRead`  | No | Use strongly consistent reads. Defaults to `false`. |
|  `derivation.applyTo.resource`  | Yes | Target resource type: `file` or `asset`. |
|  `derivation.applyTo.scope`  | No | Reserved. Currently all records are always processed regardless of this value. Defaults to `all`. |
|  `derivation.applyTo.match.source`  | Yes | External record field used for matching. |
|  `derivation.applyTo.match.target`  | Yes | Resource field to match against. Supports `:basename`, `:ext`, `:tolower` transforms. |
|  `derivation.applyTo.onNoMatch`  | No | Behavior on no match. Currently only `skip` (default) is supported. |
|  `derivation.applyTo.mappingPolicy`  | No | How derived attributes interact with existing ones: `inherit` (default) or `override`. |
|  `derivation.applyTo.responseFieldMapping`  | No | Field mappings from external record to resource metadata. |
|  `derivation.copyFields.sourcePrefix`  | No | Prefix to extract from external record fields. |
|  `derivation.copyFields.targetPrefix`  | No | Prefix to apply to target resource fields. |
|  `derivation.recordIdMapping.target`  | No | Resource field to store the external record ID (for example, `file.external_id`). |
|  `derivation.onError`  | No | Error handling: `fail` (default) or `record-and-continue`. |

## Error handling
<a name="derivation-error-handling"></a>

The following table describes common derivation errors and their resolution.

| Operation | Error | Resolution |
| --- | --- | --- |
|  `s3Lookup`  |  `AccessDenied` / `403`  | The assumed IAM role does not have `s3:GetObject` permission on the source file. Verify the role’s permissions policy. |
|  `s3Lookup`  |  `NoSuchKey` / `404`  | The S3 object does not exist at the configured key. Verify the `objectKey` and `${variable}` substitution values. |
|  `restLookup`  |  `401` / `403`  | Authentication failed. Verify the `securityConfig` credentials and Secrets Manager secret. |
|  `restLookup`  |  `404`  | The REST endpoint returned not found. Verify the `apiBase` and `path` configuration. |
|  `dynamodbLookup`  |  `AccessDeniedException`  | The assumed IAM role does not have `dynamodb:GetItem` permission on the target table. Verify the role’s permissions policy. |
|  `dynamodbLookup`  |  `ResourceNotFoundException`  | The configured DynamoDB table does not exist. Verify the `tableName` and `region`. |
| All | No matching records | When `applyTo.onNoMatch` is `skip` (default), unmatched records are silently skipped and processing continues with the next record. |
