---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_UpdateTable.html
---

# UpdateTable
<a name="API_UpdateTable"></a>

Adds new columns to the table or updates one of the table's settings, for example capacity mode, auto scaling, encryption, point-in-time recovery, or ttl settings. Note that you can only update one specific table setting per update operation.

## Request Syntax
<a name="API_UpdateTable_RequestSyntax"></a>

```
{
   "addColumns": [
      {
         "name": "{{string}}",
         "type": "{{string}}"
      }
   ],
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
   "tableName": "{{string}}",
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
<a name="API_UpdateTable_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [addColumns](#API_UpdateTable_RequestSyntax) **   <a name="keyspaces-UpdateTable-request-addColumns"></a>
For each column to be added to the specified table:
+  `name` - The name of the column.
+  `type` - An Amazon Keyspaces data type. For more information, see [Data types](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.data-types) in the *Amazon Keyspaces Developer Guide*.
Type: Array of [ColumnDefinition](API_ColumnDefinition.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [autoScalingSpecification](#API_UpdateTable_RequestSyntax) **   <a name="keyspaces-UpdateTable-request-autoScalingSpecification"></a>
The optional auto scaling settings to update for a table in provisioned capacity mode. Specifies if the service can manage throughput capacity of a provisioned table automatically on your behalf. Amazon Keyspaces auto scaling helps you provision throughput capacity for variable workloads efficiently by increasing and decreasing your table's read and write capacity automatically in response to application traffic.
If auto scaling is already enabled for the table, you can use `UpdateTable` to update the minimum and maximum values or the auto scaling policy settings independently.
For more information, see [Managing throughput capacity automatically with Amazon Keyspaces auto scaling](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html) in the *Amazon Keyspaces Developer Guide*.
Type: [AutoScalingSpecification](API_AutoScalingSpecification.md) object
Required: No

 ** [capacitySpecification](#API_UpdateTable_RequestSyntax) **   <a name="keyspaces-UpdateTable-request-capacitySpecification"></a>
Modifies the read/write throughput capacity mode for the table. The options are:
+  `throughputMode:PAY_PER_REQUEST` and
+  `throughputMode:PROVISIONED` - Provisioned capacity mode requires `readCapacityUnits` and `writeCapacityUnits` as input.
The default is `throughput_mode:PAY_PER_REQUEST`.
For more information, see [Read/write capacity modes](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html) in the *Amazon Keyspaces Developer Guide*.
Type: [CapacitySpecification](API_CapacitySpecification.md) object
Required: No

 ** [cdcSpecification](#API_UpdateTable_RequestSyntax) **   <a name="keyspaces-UpdateTable-request-cdcSpecification"></a>
The CDC stream settings of the table.
Type: [CdcSpecification](API_CdcSpecification.md) object
Required: No

 ** [clientSideTimestamps](#API_UpdateTable_RequestSyntax) **   <a name="keyspaces-UpdateTable-request-clientSideTimestamps"></a>
Enables client-side timestamps for the table. By default, the setting is disabled. You can enable client-side timestamps with the following option:
+  `status: "enabled"`
Once client-side timestamps are enabled for a table, this setting cannot be disabled.
Type: [ClientSideTimestamps](API_ClientSideTimestamps.md) object
Required: No

 ** [defaultTimeToLive](#API_UpdateTable_RequestSyntax) **   <a name="keyspaces-UpdateTable-request-defaultTimeToLive"></a>
The default Time to Live setting in seconds for the table.
For more information, see [Setting the default TTL value for a table](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-it-works.html#ttl-howitworks_default_ttl) in the *Amazon Keyspaces Developer Guide*.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 630720000.
Required: No

 ** [encryptionSpecification](#API_UpdateTable_RequestSyntax) **   <a name="keyspaces-UpdateTable-request-encryptionSpecification"></a>
Modifies the encryption settings of the table. You can choose one of the following KMS key (KMS key):
+  `type:AWS_OWNED_KMS_KEY` - This key is owned by Amazon Keyspaces.
+  `type:CUSTOMER_MANAGED_KMS_KEY` - This key is stored in your account and is created, owned, and managed by you. This option requires the `kms_key_identifier` of the KMS key in Amazon Resource Name (ARN) format as input.
The default is `AWS_OWNED_KMS_KEY`.
For more information, see [Encryption at rest](https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html) in the *Amazon Keyspaces Developer Guide*.
Type: [EncryptionSpecification](API_EncryptionSpecification.md) object
Required: No

 ** [keyspaceName](#API_UpdateTable_RequestSyntax) **   <a name="keyspaces-UpdateTable-request-keyspaceName"></a>
The name of the keyspace the specified table is stored in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** [pointInTimeRecovery](#API_UpdateTable_RequestSyntax) **   <a name="keyspaces-UpdateTable-request-pointInTimeRecovery"></a>
Modifies the `pointInTimeRecovery` settings of the table. The options are:
+  `status=ENABLED`
+  `status=DISABLED`
If it's not specified, the default is `status=DISABLED`.
For more information, see [Point-in-time recovery](https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery.html) in the *Amazon Keyspaces Developer Guide*.
Type: [PointInTimeRecovery](API_PointInTimeRecovery.md) object
Required: No

 ** [replicaSpecifications](#API_UpdateTable_RequestSyntax) **   <a name="keyspaces-UpdateTable-request-replicaSpecifications"></a>
The Region specific settings of a multi-Regional table.
Type: Array of [ReplicaSpecification](API_ReplicaSpecification.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [tableName](#API_UpdateTable_RequestSyntax) **   <a name="keyspaces-UpdateTable-request-tableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** [ttl](#API_UpdateTable_RequestSyntax) **   <a name="keyspaces-UpdateTable-request-ttl"></a>
Modifies Time to Live custom settings for the table. The options are:
+  `status:enabled`
+  `status:disabled`
The default is `status:disabled`. After `ttl` is enabled, you can't disable it for the table.
For more information, see [Expiring data by using Amazon Keyspaces Time to Live (TTL)](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL.html) in the *Amazon Keyspaces Developer Guide*.
Type: [TimeToLive](API_TimeToLive.md) object
Required: No

 ** [warmThroughputSpecification](#API_UpdateTable_RequestSyntax) **   <a name="keyspaces-UpdateTable-request-warmThroughputSpecification"></a>
Modifies the warm throughput settings for the table. You can update the read and write capacity units to adjust the pre-provisioned throughput.
Type: [WarmThroughputSpecification](API_WarmThroughputSpecification.md) object
Required: No

## Response Syntax
<a name="API_UpdateTable_ResponseSyntax"></a>

```
{
   "resourceArn": "string"
}
```

## Response Elements
<a name="API_UpdateTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resourceArn](#API_UpdateTable_ResponseSyntax) **   <a name="keyspaces-UpdateTable-response-resourceArn"></a>
The Amazon Resource Name (ARN) of the modified table.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1000.
Pattern: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`

## Errors
<a name="API_UpdateTable_Errors"></a>

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
<a name="API_UpdateTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/keyspaces-2022-02-10/UpdateTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/keyspaces-2022-02-10/UpdateTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/UpdateTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/keyspaces-2022-02-10/UpdateTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/UpdateTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/keyspaces-2022-02-10/UpdateTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/keyspaces-2022-02-10/UpdateTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/keyspaces-2022-02-10/UpdateTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/keyspaces-2022-02-10/UpdateTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/UpdateTable)
