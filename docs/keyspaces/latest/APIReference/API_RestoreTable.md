---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_RestoreTable.html
---

# RestoreTable
<a name="API_RestoreTable"></a>

Restores the table to the specified point in time within the `earliest_restorable_timestamp` and the current time. For more information about restore points, see [ Time window for PITR continuous backups](https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery_HowItWorks.html#howitworks_backup_window) in the *Amazon Keyspaces Developer Guide*.

Any number of users can execute up to 4 concurrent restores (any type of restore) in a given account.

When you restore using point in time recovery, Amazon Keyspaces restores your source table's schema and data to the state based on the selected timestamp `(day:hour:minute:second)` to a new table. The Time to Live (TTL) settings are also restored to the state based on the selected timestamp.

In addition to the table's schema, data, and TTL settings, `RestoreTable` restores the capacity mode, auto scaling settings, encryption settings, and point-in-time recovery settings from the source table. Unlike the table's schema data and TTL settings, which are restored based on the selected timestamp, these settings are always restored based on the table's settings as of the current time or when the table was deleted.

You can also overwrite these settings during restore:
+ Read/write capacity mode
+ Provisioned throughput capacity units
+ Auto scaling settings
+ Point-in-time (PITR) settings
+ Tags

For more information, see [PITR restore settings](https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery_HowItWorks.html#howitworks_backup_settings) in the *Amazon Keyspaces Developer Guide*.

Note that the following settings are not restored, and you must configure them manually for the new table:
+  AWS Identity and Access Management (IAM) policies
+ Amazon CloudWatch metrics and alarms

## Request Syntax
<a name="API_RestoreTable_RequestSyntax"></a>

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
   "capacitySpecificationOverride": {
      "readCapacityUnits": {{number}},
      "throughputMode": "{{string}}",
      "writeCapacityUnits": {{number}}
   },
   "encryptionSpecificationOverride": {
      "kmsKeyIdentifier": "{{string}}",
      "type": "{{string}}"
   },
   "pointInTimeRecoveryOverride": {
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
   "restoreTimestamp": {{number}},
   "sourceKeyspaceName": "{{string}}",
   "sourceTableName": "{{string}}",
   "tagsOverride": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "targetKeyspaceName": "{{string}}",
   "targetTableName": "{{string}}"
}
```

## Request Parameters
<a name="API_RestoreTable_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [autoScalingSpecification](#API_RestoreTable_RequestSyntax) **   <a name="keyspaces-RestoreTable-request-autoScalingSpecification"></a>
The optional auto scaling settings for the restored table in provisioned capacity mode. Specifies if the service can manage throughput capacity of a provisioned table automatically on your behalf. Amazon Keyspaces auto scaling helps you provision throughput capacity for variable workloads efficiently by increasing and decreasing your table's read and write capacity automatically in response to application traffic.
For more information, see [Managing throughput capacity automatically with Amazon Keyspaces auto scaling](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html) in the *Amazon Keyspaces Developer Guide*.
Type: [AutoScalingSpecification](API_AutoScalingSpecification.md) object
Required: No

 ** [capacitySpecificationOverride](#API_RestoreTable_RequestSyntax) **   <a name="keyspaces-RestoreTable-request-capacitySpecificationOverride"></a>
Specifies the read/write throughput capacity mode for the target table. The options are:
+  `throughputMode:PAY_PER_REQUEST`
+  `throughputMode:PROVISIONED` - Provisioned capacity mode requires `readCapacityUnits` and `writeCapacityUnits` as input.
The default is `throughput_mode:PAY_PER_REQUEST`.
For more information, see [Read/write capacity modes](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html) in the *Amazon Keyspaces Developer Guide*.
Type: [CapacitySpecification](API_CapacitySpecification.md) object
Required: No

 ** [encryptionSpecificationOverride](#API_RestoreTable_RequestSyntax) **   <a name="keyspaces-RestoreTable-request-encryptionSpecificationOverride"></a>
Specifies the encryption settings for the target table. You can choose one of the following KMS key (KMS key):
+  `type:AWS_OWNED_KMS_KEY` - This key is owned by Amazon Keyspaces.
+  `type:CUSTOMER_MANAGED_KMS_KEY` - This key is stored in your account and is created, owned, and managed by you. This option requires the `kms_key_identifier` of the KMS key in Amazon Resource Name (ARN) format as input.
The default is `type:AWS_OWNED_KMS_KEY`.
For more information, see [Encryption at rest](https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html) in the *Amazon Keyspaces Developer Guide*.
Type: [EncryptionSpecification](API_EncryptionSpecification.md) object
Required: No

 ** [pointInTimeRecoveryOverride](#API_RestoreTable_RequestSyntax) **   <a name="keyspaces-RestoreTable-request-pointInTimeRecoveryOverride"></a>
Specifies the `pointInTimeRecovery` settings for the target table. The options are:
+  `status=ENABLED`
+  `status=DISABLED`
If it's not specified, the default is `status=DISABLED`.
For more information, see [Point-in-time recovery](https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery.html) in the *Amazon Keyspaces Developer Guide*.
Type: [PointInTimeRecovery](API_PointInTimeRecovery.md) object
Required: No

 ** [replicaSpecifications](#API_RestoreTable_RequestSyntax) **   <a name="keyspaces-RestoreTable-request-replicaSpecifications"></a>
The optional Region specific settings of a multi-Regional table.
Type: Array of [ReplicaSpecification](API_ReplicaSpecification.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [restoreTimestamp](#API_RestoreTable_RequestSyntax) **   <a name="keyspaces-RestoreTable-request-restoreTimestamp"></a>
The restore timestamp in ISO 8601 format.
Type: Timestamp
Required: No

 ** [sourceKeyspaceName](#API_RestoreTable_RequestSyntax) **   <a name="keyspaces-RestoreTable-request-sourceKeyspaceName"></a>
The keyspace name of the source table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** [sourceTableName](#API_RestoreTable_RequestSyntax) **   <a name="keyspaces-RestoreTable-request-sourceTableName"></a>
The name of the source table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** [tagsOverride](#API_RestoreTable_RequestSyntax) **   <a name="keyspaces-RestoreTable-request-tagsOverride"></a>
A list of key-value pair tags to be attached to the restored table.
For more information, see [Adding tags and labels to Amazon Keyspaces resources](https://docs.aws.amazon.com/keyspaces/latest/devguide/tagging-keyspaces.html) in the *Amazon Keyspaces Developer Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 60 items.
Required: No

 ** [targetKeyspaceName](#API_RestoreTable_RequestSyntax) **   <a name="keyspaces-RestoreTable-request-targetKeyspaceName"></a>
The name of the target keyspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** [targetTableName](#API_RestoreTable_RequestSyntax) **   <a name="keyspaces-RestoreTable-request-targetTableName"></a>
The name of the target table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

## Response Syntax
<a name="API_RestoreTable_ResponseSyntax"></a>

```
{
   "restoredTableARN": "string"
}
```

## Response Elements
<a name="API_RestoreTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [restoredTableARN](#API_RestoreTable_ResponseSyntax) **   <a name="keyspaces-RestoreTable-response-restoredTableARN"></a>
The Amazon Resource Name (ARN) of the restored table.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1000.
Pattern: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`

## Errors
<a name="API_RestoreTable_Errors"></a>

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
<a name="API_RestoreTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/keyspaces-2022-02-10/RestoreTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/keyspaces-2022-02-10/RestoreTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/RestoreTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/keyspaces-2022-02-10/RestoreTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/RestoreTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/keyspaces-2022-02-10/RestoreTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/keyspaces-2022-02-10/RestoreTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/keyspaces-2022-02-10/RestoreTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/keyspaces-2022-02-10/RestoreTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/RestoreTable)
