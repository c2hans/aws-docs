---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/connector-dynamodb.html
---

# Amazon DynamoDB connector
<a name="connector-dynamodb"></a>

The Amazon DynamoDB connector performs single-record lookups by partition key and writes the result as metadata attributes on matched files or assets. It can also serve values from a DynamoDB table as selectable field values during template authoring and metadata entry.

DynamoDB connectors are well suited for per-file metadata enrichment where each file maps to a single record in an external table — for example, looking up quality scores, processing status, or classification data by filename.

DynamoDB is a derive-only connector type. It does not yet have a step type in the trigger\+steps model and cannot be used as a publisher.

## Roles
<a name="dynamodb-roles"></a>

| Role | Description |
| --- | --- |
| Metadata lookup | Performs a `GetItem` on a DynamoDB table, matches the result to an SDMA file or asset by a key field, and writes mapped values as metadata attributes. Uses the `dynamodbLookup` operation in the lookup-derivation model. |
| Field provider for templates | Serves values from a DynamoDB table as selectable options in the Spatial Data Portal during template authoring and metadata entry. Uses the connector-level `fieldMappings` \+ `ddbConfig` shorthand without triggers. |

## Prerequisites
<a name="dynamodb-prerequisites"></a>

1. Create a DynamoDB table with the metadata to derive.

1. Create an IAM role:
   +  **Role name** must start with `SpatialDataManagementContentDerivation-`.
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

## Using DynamoDB for metadata lookup
<a name="dynamodb-as-lookup"></a>

A DynamoDB derive connector performs a `GetItem` on a table using a partition key derived from the file or asset being processed. The result is matched to the SDMA resource and written as metadata attributes.

### Partition key resolution
<a name="_partition-key-resolution"></a>

The partition key value can be resolved in two ways:
+  **Explicit** — set `dynamodbConfig.partitionKeyValue` to a template string (for example, `${asset.assetId}`).
+  **From match config** — if `partitionKeyValue` is omitted, the value is derived from the `applyTo.match.target` field. For example, if `match.target` is `file.path:basename`, the file’s basename is used as the partition key value.

### Example: enrich file metadata from a DynamoDB table
<a name="_example-enrich-file-metadata-from-a-dynamodb-table"></a>

```
{
  "dynamodbConfig": {
    "tableName": "<TABLE_NAME>",
    "partitionKey": "filename",
    "region": "us-west-2",
    "securityConfig": {
      "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentDerivation-DynamoDBLookup",
      "type": "AssumeRole"
    }
  },
  "fieldMappings": [
    { "source": "processing_notes", "target": "file.processing_notes" },
    { "source": "skus", "target": "file.skus" }
  ],
  "triggers": [
    {
      "description": "Enrich files with metadata from DynamoDB",
      "resources": ["asset"],
      "events": ["uploadComplete", "onDemand"],
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
          "onNoMatch": "skip"
        }
      }
    }
  ]
}
```

The `dynamodbConfig` at the trigger’s `derivation` level is merged with the connector-level `dynamodbConfig`. Use the trigger-level config to override specific fields like `consistentRead` per trigger.

For full details on the lookup-derivation model and `applyTo` matching, see [Metadata lookup and enrichment](connector-derivation.md).

## Using DynamoDB as a field provider for templates
<a name="dynamodb-as-field-provider"></a>

A DynamoDB connector can serve values from a table as selectable options in the Spatial Data Portal. This uses the connector-level `fieldMappings` \+ `ddbConfig` shorthand — no triggers, no `resources` block.

### Example: serve classification values from DynamoDB for template authoring
<a name="_example-serve-classification-values-from-dynamodb-for-template-authoring"></a>

```
{
  "ddbConfig": {
    "tableName": "<TABLE_NAME>",
    "partitionKey": "category",
    "region": "us-west-2",
    "securityConfig": {
      "assumeRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/SpatialDataManagementContentDerivation-FieldProvider",
      "type": "AssumeRole"
    }
  },
  "fieldMappings": [
    { "source": "classification", "target": "asset.classification" },
    { "source": "sub_category", "target": "asset.sub_category" }
  ]
}
```

This connector has no triggers. When a template references this connector, the Portal queries the DynamoDB table and presents the distinct values of `classification` and `sub_category` as selectable options during metadata entry.

Field mappings can include an `options` object to declare cascading dependencies between fields — for example, selecting a classification can filter the available sub-categories.

## Configuration fields
<a name="dynamodb-config-fields"></a>

### Connector-level fields
<a name="_connector-level-fields"></a>

| Field | Required | Description |
| --- | --- | --- |
|  `dynamodbConfig.tableName` (or `ddbConfig.tableName`) | Yes | DynamoDB table name. |
|  `dynamodbConfig.partitionKey` (or `ddbConfig.partitionKey`) | Yes | Partition key attribute name. |
|  `dynamodbConfig.region` (or `ddbConfig.region`) | No | AWS Region of the DynamoDB table. |
|  `dynamodbConfig.securityConfig` (or `ddbConfig.securityConfig`) | Yes | Authentication configuration. Must use `AssumeRole` type. |

### Trigger-level derivation fields
<a name="_trigger-level-derivation-fields"></a>

| Field | Required | Description |
| --- | --- | --- |
|  `derivation.op`  | Yes | Must be `dynamodbLookup`. |
|  `derivation.dynamodbConfig.partitionKeyValue`  | No | Partition key value template with `${variable}` support. If omitted, derived from `applyTo.match`. |
|  `derivation.dynamodbConfig.consistentRead`  | No | Use strongly consistent reads. Defaults to `false`. |
|  `derivation.applyTo.resource`  | Yes | Target resource type: `file` or `asset`. |
|  `derivation.applyTo.match.source`  | Yes | External record field used for matching. |
|  `derivation.applyTo.match.target`  | Yes | Resource field to match against. Supports `:basename`, `:ext`, `:tolower` transforms. |
|  `derivation.applyTo.onNoMatch`  | No | Behavior on no match. Currently only `skip` (default) is supported. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
