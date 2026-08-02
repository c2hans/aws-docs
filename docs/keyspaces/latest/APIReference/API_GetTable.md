---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_GetTable.html
---

# GetTable
<a name="API_GetTable"></a>

Returns information about the table, including the table's name and current status, the keyspace name, configuration settings, and metadata.

To read table metadata using `GetTable`, the IAM principal needs `Select` action permissions for the table and the system keyspace.

## Request Syntax
<a name="API_GetTable_RequestSyntax"></a>

```
{
   "keyspaceName": "{{string}}",
   "tableName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTable_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [keyspaceName](#API_GetTable_RequestSyntax) **   <a name="keyspaces-GetTable-request-keyspaceName"></a>
The name of the keyspace that the table is stored in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** [tableName](#API_GetTable_RequestSyntax) **   <a name="keyspaces-GetTable-request-tableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

## Response Syntax
<a name="API_GetTable_ResponseSyntax"></a>

```
{
   "capacitySpecification": {
      "lastUpdateToPayPerRequestTimestamp": number,
      "readCapacityUnits": number,
      "throughputMode": "string",
      "writeCapacityUnits": number
   },
   "cdcSpecification": {
      "status": "string",
      "viewType": "string"
   },
   "clientSideTimestamps": {
      "status": "string"
   },
   "comment": {
      "message": "string"
   },
   "creationTimestamp": number,
   "defaultTimeToLive": number,
   "encryptionSpecification": {
      "kmsKeyIdentifier": "string",
      "type": "string"
   },
   "keyspaceName": "string",
   "latestStreamArn": "string",
   "pointInTimeRecovery": {
      "earliestRestorableTimestamp": number,
      "status": "string"
   },
   "replicaSpecifications": [
      {
         "capacitySpecification": {
            "lastUpdateToPayPerRequestTimestamp": number,
            "readCapacityUnits": number,
            "throughputMode": "string",
            "writeCapacityUnits": number
         },
         "region": "string",
         "status": "string",
         "warmThroughputSpecification": {
            "readUnitsPerSecond": number,
            "status": "string",
            "writeUnitsPerSecond": number
         }
      }
   ],
   "resourceArn": "string",
   "schemaDefinition": {
      "allColumns": [
         {
            "name": "string",
            "type": "string"
         }
      ],
      "clusteringKeys": [
         {
            "name": "string",
            "orderBy": "string"
         }
      ],
      "partitionKeys": [
         {
            "name": "string"
         }
      ],
      "staticColumns": [
         {
            "name": "string"
         }
      ]
   },
   "status": "string",
   "tableName": "string",
   "ttl": {
      "status": "string"
   },
   "warmThroughputSpecification": {
      "readUnitsPerSecond": number,
      "status": "string",
      "writeUnitsPerSecond": number
   }
}
```

## Response Elements
<a name="API_GetTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [capacitySpecification](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-capacitySpecification"></a>
The read/write throughput capacity mode for a table. The options are:
+  `throughputMode:PAY_PER_REQUEST`
+  `throughputMode:PROVISIONED`
Type: [CapacitySpecificationSummary](API_CapacitySpecificationSummary.md) object

 ** [cdcSpecification](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-cdcSpecification"></a>
The CDC stream settings of the table.
Type: [CdcSpecificationSummary](API_CdcSpecificationSummary.md) object

 ** [clientSideTimestamps](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-clientSideTimestamps"></a>
 The client-side timestamps setting of the table.
Type: [ClientSideTimestamps](API_ClientSideTimestamps.md) object

 ** [comment](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-comment"></a>
The the description of the specified table.
Type: [Comment](API_Comment.md) object

 ** [creationTimestamp](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-creationTimestamp"></a>
The creation timestamp of the specified table.
Type: Timestamp

 ** [defaultTimeToLive](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-defaultTimeToLive"></a>
The default Time to Live settings in seconds of the specified table.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 630720000.

 ** [encryptionSpecification](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-encryptionSpecification"></a>
The encryption settings of the specified table.
Type: [EncryptionSpecification](API_EncryptionSpecification.md) object

 ** [keyspaceName](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-keyspaceName"></a>
The name of the keyspace that the specified table is stored in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`

 ** [latestStreamArn](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-latestStreamArn"></a>
The Amazon Resource Name (ARN) of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`

 ** [pointInTimeRecovery](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-pointInTimeRecovery"></a>
The point-in-time recovery status of the specified table.
Type: [PointInTimeRecoverySummary](API_PointInTimeRecoverySummary.md) object

 ** [replicaSpecifications](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-replicaSpecifications"></a>
Returns the AWS Region specific settings of all Regions a multi-Region table is replicated in.
Type: Array of [ReplicaSpecificationSummary](API_ReplicaSpecificationSummary.md) objects
Array Members: Minimum number of 0 items.

 ** [resourceArn](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-resourceArn"></a>
The Amazon Resource Name (ARN) of the specified table.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1000.
Pattern: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`

 ** [schemaDefinition](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-schemaDefinition"></a>
The schema definition of the specified table.
Type: [SchemaDefinition](API_SchemaDefinition.md) object

 ** [status](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-status"></a>
The current status of the specified table.
Type: String
Valid Values: `ACTIVE | CREATING | UPDATING | DELETING | DELETED | RESTORING | INACCESSIBLE_ENCRYPTION_CREDENTIALS`

 ** [tableName](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-tableName"></a>
The name of the specified table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`

 ** [ttl](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-ttl"></a>
The custom Time to Live settings of the specified table.
Type: [TimeToLive](API_TimeToLive.md) object

 ** [warmThroughputSpecification](#API_GetTable_ResponseSyntax) **   <a name="keyspaces-GetTable-response-warmThroughputSpecification"></a>
The warm throughput settings for the table, including the current status and configured read and write capacity units.
Type: [WarmThroughputSpecificationSummary](API_WarmThroughputSpecificationSummary.md) object

## Errors
<a name="API_GetTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have sufficient access permissions to perform this action.
 ** message **
You don't have the required permissions to perform this operation. Verify your IAM permissions and try again.
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
<a name="API_GetTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/keyspaces-2022-02-10/GetTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/keyspaces-2022-02-10/GetTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/GetTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/keyspaces-2022-02-10/GetTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/GetTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/keyspaces-2022-02-10/GetTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/keyspaces-2022-02-10/GetTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/keyspaces-2022-02-10/GetTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/keyspaces-2022-02-10/GetTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/GetTable)
