---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateGlobalTableSettings.html
---

# UpdateGlobalTableSettings
<a name="API_UpdateGlobalTableSettings"></a>

Updates settings for a global table.

**Important**
This documentation is for version 2017.11.29 (Legacy) of global tables, which should be avoided for new global tables. Customers should use [Global Tables version 2019.11.21 (Current)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) when possible, because it provides greater flexibility, higher efficiency, and consumes less write capacity than 2017.11.29 (Legacy).
To determine which version you're using, see [Determining the global table version you are using](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.DetermineVersion.html). To update existing global tables from version 2017.11.29 (Legacy) to version 2019.11.21 (Current), see [Upgrading global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_upgrade.html).

## Request Syntax
<a name="API_UpdateGlobalTableSettings_RequestSyntax"></a>

```
{
   "GlobalTableBillingMode": "{{string}}",
   "GlobalTableGlobalSecondaryIndexSettingsUpdate": [
      {
         "IndexName": "{{string}}",
         "ProvisionedWriteCapacityAutoScalingSettingsUpdate": {
            "AutoScalingDisabled": {{boolean}},
            "AutoScalingRoleArn": "{{string}}",
            "MaximumUnits": {{number}},
            "MinimumUnits": {{number}},
            "ScalingPolicyUpdate": {
               "PolicyName": "{{string}}",
               "TargetTrackingScalingPolicyConfiguration": {
                  "DisableScaleIn": {{boolean}},
                  "ScaleInCooldown": {{number}},
                  "ScaleOutCooldown": {{number}},
                  "TargetValue": {{number}}
               }
            }
         },
         "ProvisionedWriteCapacityUnits": {{number}}
      }
   ],
   "GlobalTableName": "{{string}}",
   "GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate": {
      "AutoScalingDisabled": {{boolean}},
      "AutoScalingRoleArn": "{{string}}",
      "MaximumUnits": {{number}},
      "MinimumUnits": {{number}},
      "ScalingPolicyUpdate": {
         "PolicyName": "{{string}}",
         "TargetTrackingScalingPolicyConfiguration": {
            "DisableScaleIn": {{boolean}},
            "ScaleInCooldown": {{number}},
            "ScaleOutCooldown": {{number}},
            "TargetValue": {{number}}
         }
      }
   },
   "GlobalTableProvisionedWriteCapacityUnits": {{number}},
   "ReplicaSettingsUpdate": [
      {
         "RegionName": "{{string}}",
         "ReplicaGlobalSecondaryIndexSettingsUpdate": [
            {
               "IndexName": "{{string}}",
               "ProvisionedReadCapacityAutoScalingSettingsUpdate": {
                  "AutoScalingDisabled": {{boolean}},
                  "AutoScalingRoleArn": "{{string}}",
                  "MaximumUnits": {{number}},
                  "MinimumUnits": {{number}},
                  "ScalingPolicyUpdate": {
                     "PolicyName": "{{string}}",
                     "TargetTrackingScalingPolicyConfiguration": {
                        "DisableScaleIn": {{boolean}},
                        "ScaleInCooldown": {{number}},
                        "ScaleOutCooldown": {{number}},
                        "TargetValue": {{number}}
                     }
                  }
               },
               "ProvisionedReadCapacityUnits": {{number}}
            }
         ],
         "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate": {
            "AutoScalingDisabled": {{boolean}},
            "AutoScalingRoleArn": "{{string}}",
            "MaximumUnits": {{number}},
            "MinimumUnits": {{number}},
            "ScalingPolicyUpdate": {
               "PolicyName": "{{string}}",
               "TargetTrackingScalingPolicyConfiguration": {
                  "DisableScaleIn": {{boolean}},
                  "ScaleInCooldown": {{number}},
                  "ScaleOutCooldown": {{number}},
                  "TargetValue": {{number}}
               }
            }
         },
         "ReplicaProvisionedReadCapacityUnits": {{number}},
         "ReplicaTableClass": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateGlobalTableSettings_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GlobalTableName](#API_UpdateGlobalTableSettings_RequestSyntax) **   <a name="DDB-UpdateGlobalTableSettings-request-GlobalTableName"></a>
The name of the global table
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [GlobalTableBillingMode](#API_UpdateGlobalTableSettings_RequestSyntax) **   <a name="DDB-UpdateGlobalTableSettings-request-GlobalTableBillingMode"></a>
The billing mode of the global table. If `GlobalTableBillingMode` is not specified, the global table defaults to `PROVISIONED` capacity billing mode.
+  `PROVISIONED` - We recommend using `PROVISIONED` for predictable workloads. `PROVISIONED` sets the billing mode to [Provisioned capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html).
+  `PAY_PER_REQUEST` - We recommend using `PAY_PER_REQUEST` for unpredictable workloads. `PAY_PER_REQUEST` sets the billing mode to [On-demand capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html).
Type: String
Valid Values: `PROVISIONED | PAY_PER_REQUEST`
Required: No

 ** [GlobalTableGlobalSecondaryIndexSettingsUpdate](#API_UpdateGlobalTableSettings_RequestSyntax) **   <a name="DDB-UpdateGlobalTableSettings-request-GlobalTableGlobalSecondaryIndexSettingsUpdate"></a>
Represents the settings of a global secondary index for a global table that will be modified.
Type: Array of [GlobalTableGlobalSecondaryIndexSettingsUpdate](API_GlobalTableGlobalSecondaryIndexSettingsUpdate.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** [GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate](#API_UpdateGlobalTableSettings_RequestSyntax) **   <a name="DDB-UpdateGlobalTableSettings-request-GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate"></a>
Auto scaling settings for managing provisioned write capacity for the global table.
Type: [AutoScalingSettingsUpdate](API_AutoScalingSettingsUpdate.md) object
Required: No

 ** [GlobalTableProvisionedWriteCapacityUnits](#API_UpdateGlobalTableSettings_RequestSyntax) **   <a name="DDB-UpdateGlobalTableSettings-request-GlobalTableProvisionedWriteCapacityUnits"></a>
The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException.`
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** [ReplicaSettingsUpdate](#API_UpdateGlobalTableSettings_RequestSyntax) **   <a name="DDB-UpdateGlobalTableSettings-request-ReplicaSettingsUpdate"></a>
Represents the settings for a global table in a Region that will be modified.
Type: Array of [ReplicaSettingsUpdate](API_ReplicaSettingsUpdate.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_UpdateGlobalTableSettings_ResponseSyntax"></a>

```
{
   "GlobalTableName": "string",
   "ReplicaSettings": [
      {
         "RegionName": "string",
         "ReplicaBillingModeSummary": {
            "BillingMode": "string",
            "LastUpdateToPayPerRequestDateTime": number
         },
         "ReplicaGlobalSecondaryIndexSettings": [
            {
               "IndexName": "string",
               "IndexStatus": "string",
               "ProvisionedReadCapacityAutoScalingSettings": {
                  "AutoScalingDisabled": boolean,
                  "AutoScalingRoleArn": "string",
                  "MaximumUnits": number,
                  "MinimumUnits": number,
                  "ScalingPolicies": [
                     {
                        "PolicyName": "string",
                        "TargetTrackingScalingPolicyConfiguration": {
                           "DisableScaleIn": boolean,
                           "ScaleInCooldown": number,
                           "ScaleOutCooldown": number,
                           "TargetValue": number
                        }
                     }
                  ]
               },
               "ProvisionedReadCapacityUnits": number,
               "ProvisionedWriteCapacityAutoScalingSettings": {
                  "AutoScalingDisabled": boolean,
                  "AutoScalingRoleArn": "string",
                  "MaximumUnits": number,
                  "MinimumUnits": number,
                  "ScalingPolicies": [
                     {
                        "PolicyName": "string",
                        "TargetTrackingScalingPolicyConfiguration": {
                           "DisableScaleIn": boolean,
                           "ScaleInCooldown": number,
                           "ScaleOutCooldown": number,
                           "TargetValue": number
                        }
                     }
                  ]
               },
               "ProvisionedWriteCapacityUnits": number
            }
         ],
         "ReplicaProvisionedReadCapacityAutoScalingSettings": {
            "AutoScalingDisabled": boolean,
            "AutoScalingRoleArn": "string",
            "MaximumUnits": number,
            "MinimumUnits": number,
            "ScalingPolicies": [
               {
                  "PolicyName": "string",
                  "TargetTrackingScalingPolicyConfiguration": {
                     "DisableScaleIn": boolean,
                     "ScaleInCooldown": number,
                     "ScaleOutCooldown": number,
                     "TargetValue": number
                  }
               }
            ]
         },
         "ReplicaProvisionedReadCapacityUnits": number,
         "ReplicaProvisionedWriteCapacityAutoScalingSettings": {
            "AutoScalingDisabled": boolean,
            "AutoScalingRoleArn": "string",
            "MaximumUnits": number,
            "MinimumUnits": number,
            "ScalingPolicies": [
               {
                  "PolicyName": "string",
                  "TargetTrackingScalingPolicyConfiguration": {
                     "DisableScaleIn": boolean,
                     "ScaleInCooldown": number,
                     "ScaleOutCooldown": number,
                     "TargetValue": number
                  }
               }
            ]
         },
         "ReplicaProvisionedWriteCapacityUnits": number,
         "ReplicaStatus": "string",
         "ReplicaTableClassSummary": {
            "LastUpdateDateTime": number,
            "TableClass": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_UpdateGlobalTableSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GlobalTableName](#API_UpdateGlobalTableSettings_ResponseSyntax) **   <a name="DDB-UpdateGlobalTableSettings-response-GlobalTableName"></a>
The name of the global table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [ReplicaSettings](#API_UpdateGlobalTableSettings_ResponseSyntax) **   <a name="DDB-UpdateGlobalTableSettings-response-ReplicaSettings"></a>
The Region-specific settings for the global table.
Type: Array of [ReplicaSettingsDescription](API_ReplicaSettingsDescription.md) objects

## Errors
<a name="API_UpdateGlobalTableSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GlobalTableNotFoundException **
The specified global table does not exist.
HTTP Status Code: 400

 ** IndexNotFoundException **
The operation tried to access a nonexistent index.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

 ** LimitExceededException **
There is no limit to the number of daily on-demand backups that can be taken.
For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include `CreateTable`, `UpdateTable`, `DeleteTable`,`UpdateTimeToLive`, `RestoreTableFromBackup`, and `RestoreTableToPointInTime`.
When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.
When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.
There is a soft account quota of 2,500 tables.
GetRecords was called with a value of more than 1000 for the limit request parameter.
More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.
 ** message **
Too many operations for a given subscriber.
HTTP Status Code: 400

 ** ReplicaNotFoundException **
The specified replica is no longer part of the global table.
HTTP Status Code: 400

 ** ResourceInUseException **
The operation conflicts with the resource's availability. For example:
+ You attempted to recreate an existing table.
+ You tried to delete a table currently in the `CREATING` state.
+ You tried to update a resource that was already being updated.
When appropriate, wait for the ongoing update to complete and attempt the request again.
 ** message **
The resource which is being attempted to be changed is in use.
HTTP Status Code: 400

## See Also
<a name="API_UpdateGlobalTableSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/UpdateGlobalTableSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/UpdateGlobalTableSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/UpdateGlobalTableSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/UpdateGlobalTableSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/UpdateGlobalTableSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/UpdateGlobalTableSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/UpdateGlobalTableSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/UpdateGlobalTableSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/UpdateGlobalTableSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/UpdateGlobalTableSettings)
