---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_CreateTable.html
---

# CreateTable
<a name="API_CreateTable"></a>

The `CreateTable` operation adds a new table to the specified keyspace. Within a keyspace, table names must be unique.

 `CreateTable` is an asynchronous operation. When the request is received, the status of the table is set to `CREATING`. You can monitor the creation status of the new table by using the `GetTable` operation, which returns the current `status` of the table. You can start using a table when the status is `ACTIVE`.

For more information, see [Create a table](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.tables.html) in the *Amazon Keyspaces Developer Guide*.

## Request Syntax
<a name="API_CreateTable_RequestSyntax"></a>

```
{
   "autoScalingSpecification": {
      "readCapacityAutoScaling": {
         "autoScalingDisabled": {{boolean}},
         "maximumUnits": {{number}},
         "minimumUnits": {{number}},
         "scalingPolicy": {
            "targetTrackingScalingPolicyConfiguration": {
               "disableScaleIn": {{boolean}},
               "scaleInCooldown": {{number}},
               "scaleOutCooldown": {{number}},
               "targetValue": {{number}}
            }
         }
      },
      "writeCapacityAutoScaling": {
         "autoScalingDisabled": {{boolean}},
         "maximumUnits": {{number}},
         "minimumUnits": {{number}},
         "scalingPolicy": {
            "targetTrackingScalingPolicyConfiguration": {
               "disableScaleIn": {{boolean}},
               "scaleInCooldown": {{number}},
               "scaleOutCooldown": {{number}},
               "targetValue": {{number}}
            }
         }
      }
   },
   "capacitySpecification": {
      "readCapacityUnits": {{number}},
      "throughputMode": "{{string}}",
      "writeCapacityUnits": {{number}}
   },
   "cdcSpecification": {
      "propagateTags": "{{string}}",
      "status": "{{string}}",
      "tags": [
         {
            "key": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "viewType": "{{string}}"
   },
   "clientSideTimestamps": {
      "status": "{{string}}"
   },
   "comment": {
      "message": "{{string}}"
   },
   "defaultTimeToLive": {{number}},
   "encryptionSpecification": {
      "kmsKeyIdentifier": "{{string}}",
      "type": "{{string}}"
   },
   "keyspaceName": "{{string}}",
   "pointInTimeRecovery": {
      "status": "{{string}}"
   },
   "replicaSpecifications": [
      {
         "readCapacityAutoScaling": {
            "autoScalingDisabled": {{boolean}},
            "maximumUnits": {{number}},
            "minimumUnits": {{number}},
            "scalingPolicy": {
               "targetTrackingScalingPolicyConfiguration": {
                  "disableScaleIn": {{boolean}},
                  "scaleInCooldown": {{number}},
                  "scaleOutCooldown": {{number}},
                  "targetValue": {{number}}
               }
            }
         },
         "readCapacityUnits": {{number}},
         "region": "{{string}}"
      }
   ],
   "schemaDefinition": {
      "allColumns": [
         {
            "name": "{{string}}",
            "type": "{{string}}"
         }
      ],
      "clusteringKeys": [
         {
            "name": "{{string}}",
            "orderBy": "{{string}}"
         }
      ],
      "partitionKeys": [
         {
            "name": "{{string}}"
         }
      ],
      "staticColumns": [
         {
            "name": "{{string}}"
         }
      ]
   },
   "tableName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "ttl": {
      "status": "{{string}}"
   },
   "warmThroughputSpecification": {
      "readUnitsPerSecond": {{number}},
      "writeUnitsPerSecond": {{number}}
   }
}
```

## Request Parameters
<a name="API_CreateTable_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [autoScalingSpecification](#API_CreateTable_RequestSyntax) **   <a name="keyspaces-CreateTable-request-autoScalingSpecification"></a>
The optional auto scaling settings for a table in provisioned capacity mode. Specifies if the service can manage throughput capacity automatically on your behalf.
Auto scaling helps you provision throughput capacity for variable workloads efficiently by increasing and decreasing your table's read and write capacity automatically in response to application traffic. For more information, see [Managing throughput capacity automatically with Amazon Keyspaces auto scaling](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html) in the *Amazon Keyspaces Developer Guide*.
By default, auto scaling is disabled for a table.
Type: [AutoScalingSpecification](API_AutoScalingSpecification.md) object
Required: No

 ** [capacitySpecification](#API_CreateTable_RequestSyntax) **   <a name="keyspaces-CreateTable-request-capacitySpecification"></a>
Specifies the read/write throughput capacity mode for the table. The options are:
+  `throughputMode:PAY_PER_REQUEST` and
+  `throughputMode:PROVISIONED` - Provisioned capacity mode requires `readCapacityUnits` and `writeCapacityUnits` as input.
The default is `throughput_mode:PAY_PER_REQUEST`.
For more information, see [Read/write capacity modes](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html) in the *Amazon Keyspaces Developer Guide*.
Type: [CapacitySpecification](API_CapacitySpecification.md) object
Required: No

 ** [cdcSpecification](#API_CreateTable_RequestSyntax) **   <a name="keyspaces-CreateTable-request-cdcSpecification"></a>
The CDC stream settings of the table.
Type: [CdcSpecification](API_CdcSpecification.md) object
Required: No

 ** [clientSideTimestamps](#API_CreateTable_RequestSyntax) **   <a name="keyspaces-CreateTable-request-clientSideTimestamps"></a>
 Enables client-side timestamps for the table. By default, the setting is disabled. You can enable client-side timestamps with the following option:
+  `status: "enabled"`
Once client-side timestamps are enabled for a table, this setting cannot be disabled.
Type: [ClientSideTimestamps](API_ClientSideTimestamps.md) object
Required: No

 ** [comment](#API_CreateTable_RequestSyntax) **   <a name="keyspaces-CreateTable-request-comment"></a>
This parameter allows to enter a description of the table.
Type: [Comment](API_Comment.md) object
Required: No

 ** [defaultTimeToLive](#API_CreateTable_RequestSyntax) **   <a name="keyspaces-CreateTable-request-defaultTimeToLive"></a>
The default Time to Live setting in seconds for the table.
For more information, see [Setting the default TTL value for a table](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-it-works.html#ttl-howitworks_default_ttl) in the *Amazon Keyspaces Developer Guide*.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 630720000.
Required: No

 ** [encryptionSpecification](#API_CreateTable_RequestSyntax) **   <a name="keyspaces-CreateTable-request-encryptionSpecification"></a>
Specifies how the encryption key for encryption at rest is managed for the table. You can choose one of the following KMS key (KMS key):
+  `type:AWS_OWNED_KMS_KEY` - This key is owned by Amazon Keyspaces.
+  `type:CUSTOMER_MANAGED_KMS_KEY` - This key is stored in your account and is created, owned, and managed by you. This option requires the `kms_key_identifier` of the KMS key in Amazon Resource Name (ARN) format as input.
The default is `type:AWS_OWNED_KMS_KEY`.
For more information, see [Encryption at rest](https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html) in the *Amazon Keyspaces Developer Guide*.
Type: [EncryptionSpecification](API_EncryptionSpecification.md) object
Required: No

 ** [keyspaceName](#API_CreateTable_RequestSyntax) **   <a name="keyspaces-CreateTable-request-keyspaceName"></a>
The name of the keyspace that the table is going to be created in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** [pointInTimeRecovery](#API_CreateTable_RequestSyntax) **   <a name="keyspaces-CreateTable-request-pointInTimeRecovery"></a>
Specifies if `pointInTimeRecovery` is enabled or disabled for the table. The options are:
+  `status=ENABLED`
+  `status=DISABLED`
If it's not specified, the default is `status=DISABLED`.
For more information, see [Point-in-time recovery](https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery.html) in the *Amazon Keyspaces Developer Guide*.
Type: [PointInTimeRecovery](API_PointInTimeRecovery.md) object
Required: No

 ** [replicaSpecifications](#API_CreateTable_RequestSyntax) **   <a name="keyspaces-CreateTable-request-replicaSpecifications"></a>
The optional AWS Region specific settings of a multi-Region table. These settings overwrite the general settings of the table for the specified Region.
For a multi-Region table in provisioned capacity mode, you can configure the table's read capacity differently for each Region's replica. The write capacity, however, remains synchronized between all replicas to ensure that there's enough capacity to replicate writes across all Regions. To define the read capacity for a table replica in a specific Region, you can do so by configuring the following parameters.
+  `region`: The Region where these settings are applied. (Required)
+  `readCapacityUnits`: The provisioned read capacity units. (Optional)
+  `readCapacityAutoScaling`: The read capacity auto scaling settings for the table. (Optional)
Type: Array of [ReplicaSpecification](API_ReplicaSpecification.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [schemaDefinition](#API_CreateTable_RequestSyntax) **   <a name="keyspaces-CreateTable-request-schemaDefinition"></a>
The `schemaDefinition` consists of the following parameters.
For each column to be created:
+  `name` - The name of the column.
+  `type` - An Amazon Keyspaces data type. For more information, see [Data types](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.data-types) in the *Amazon Keyspaces Developer Guide*.
The primary key of the table consists of the following columns:
+  `partitionKeys` - The partition key can be a single column, or it can be a compound value composed of two or more columns. The partition key portion of the primary key is required and determines how Amazon Keyspaces stores your data.
+  `name` - The name of each partition key column.
+  `clusteringKeys` - The optional clustering column portion of your primary key determines how the data is clustered and sorted within each partition.
+  `name` - The name of the clustering column.
+  `orderBy` - Sets the ascendant (`ASC`) or descendant (`DESC`) order modifier.

  To define a column as static use `staticColumns` - Static columns store values that are shared by all rows in the same partition:
+  `name` - The name of the column.
+  `type` - An Amazon Keyspaces data type.
Type: [SchemaDefinition](API_SchemaDefinition.md) object
Required: Yes

 ** [tableName](#API_CreateTable_RequestSyntax) **   <a name="keyspaces-CreateTable-request-tableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** [tags](#API_CreateTable_RequestSyntax) **   <a name="keyspaces-CreateTable-request-tags"></a>
A list of key-value pair tags to be attached to the resource.
For more information, see [Adding tags and labels to Amazon Keyspaces resources](https://docs.aws.amazon.com/keyspaces/latest/devguide/tagging-keyspaces.html) in the *Amazon Keyspaces Developer Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 60 items.
Required: No

 ** [ttl](#API_CreateTable_RequestSyntax) **   <a name="keyspaces-CreateTable-request-ttl"></a>
Enables Time to Live custom settings for the table. The options are:
+  `status:enabled`
+  `status:disabled`
The default is `status:disabled`. After `ttl` is enabled, you can't disable it for the table.
For more information, see [Expiring data by using Amazon Keyspaces Time to Live (TTL)](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL.html) in the *Amazon Keyspaces Developer Guide*.
Type: [TimeToLive](API_TimeToLive.md) object
Required: No

 ** [warmThroughputSpecification](#API_CreateTable_RequestSyntax) **   <a name="keyspaces-CreateTable-request-warmThroughputSpecification"></a>
Specifies the warm throughput settings for the table. Pre-warming a table helps you avoid capacity exceeded exceptions by pre-provisioning read and write capacity units to reduce cold start latency when your table receives traffic.
For more information about pre-warming in Amazon Keyspaces, see [Pre-warm a table in Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/warm-throughput.html) in the *Amazon Keyspaces Developer Guide*.
Type: [WarmThroughputSpecification](API_WarmThroughputSpecification.md) object
Required: No

## Response Syntax
<a name="API_CreateTable_ResponseSyntax"></a>

```
{
   "resourceArn": "string"
}
```

## Response Elements
<a name="API_CreateTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resourceArn](#API_CreateTable_ResponseSyntax) **   <a name="keyspaces-CreateTable-response-resourceArn"></a>
The unique identifier of the table in the format of an Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1000.
Pattern: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`

## Errors
<a name="API_CreateTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have sufficient access permissions to perform this action.
 ** message **
You don't have the required permissions to perform this operation. Verify your IAM permissions and try again.
HTTP Status Code: 400

 [ConflictException](API_ConflictException.md)
Amazon Keyspaces couldn't complete the requested action. This error may occur if you try to perform an action and the same or a different action is already in progress, or if you try to create a resource that already exists.
 ** message **
The requested operation conflicts with the current state of the resource or another concurrent operation.
HTTP Status Code: 400

 [InternalServerException](API_InternalServerException.md)
Amazon Keyspaces was unable to fully process this request because of an internal server error.
 ** message **
An internal service error occurred. Retry your request. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The specified resource was not found. Verify the resource identifier and ensure the resource exists and is in an ACTIVE state.
 ** resourceArn **
The unique identifier in the format of Amazon Resource Name (ARN) for the resource couldn't be found.
HTTP Status Code: 400

 [ServiceQuotaExceededException](API_ServiceQuotaExceededException.md)
The operation exceeded the service quota for this resource. For more information on service quotas, see [Quotas](https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html) in the *Amazon Keyspaces Developer Guide*.
 ** message **
The requested operation would exceed the service quota for this resource. Review the service quotas and adjust your request accordingly.
HTTP Status Code: 400

 [ValidationException](API_ValidationException.md)
The operation failed due to an invalid or malformed request.
 ** message **
The request parameters are invalid or malformed. Review the API documentation and correct the request format.
HTTP Status Code: 400

## See Also
<a name="API_CreateTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/keyspaces-2022-02-10/CreateTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/keyspaces-2022-02-10/CreateTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/CreateTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/keyspaces-2022-02-10/CreateTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/CreateTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/keyspaces-2022-02-10/CreateTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/keyspaces-2022-02-10/CreateTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/keyspaces-2022-02-10/CreateTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/keyspaces-2022-02-10/CreateTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/CreateTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces (for Apache Cassandra). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
