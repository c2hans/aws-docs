---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTableReplicaAutoScaling.html
---

# UpdateTableReplicaAutoScaling
<a name="API_UpdateTableReplicaAutoScaling"></a>

Updates auto scaling settings on your global tables at once.

## Request Syntax
<a name="API_UpdateTableReplicaAutoScaling_RequestSyntax"></a>

```
{
   "GlobalSecondaryIndexUpdates": [
      {
         "IndexName": "{{string}}",
         "ProvisionedWriteCapacityAutoScalingUpdate": {
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
         }
      }
   ],
   "ProvisionedWriteCapacityAutoScalingUpdate": {
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
   "ReplicaUpdates": [
      {
         "RegionName": "{{string}}",
         "ReplicaGlobalSecondaryIndexUpdates": [
            {
               "IndexName": "{{string}}",
               "ProvisionedReadCapacityAutoScalingUpdate": {
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
               }
            }
         ],
         "ReplicaProvisionedReadCapacityAutoScalingUpdate": {
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
         }
      }
   ],
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateTableReplicaAutoScaling_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [TableName](#API_UpdateTableReplicaAutoScaling_RequestSyntax) **   <a name="DDB-UpdateTableReplicaAutoScaling-request-TableName"></a>
The name of the global table to be updated. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [GlobalSecondaryIndexUpdates](#API_UpdateTableReplicaAutoScaling_RequestSyntax) **   <a name="DDB-UpdateTableReplicaAutoScaling-request-GlobalSecondaryIndexUpdates"></a>
Represents the auto scaling settings of the global secondary indexes of the replica to be updated.
Type: Array of [GlobalSecondaryIndexAutoScalingUpdate](API_GlobalSecondaryIndexAutoScalingUpdate.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [ProvisionedWriteCapacityAutoScalingUpdate](#API_UpdateTableReplicaAutoScaling_RequestSyntax) **   <a name="DDB-UpdateTableReplicaAutoScaling-request-ProvisionedWriteCapacityAutoScalingUpdate"></a>
Represents the auto scaling settings to be modified for a global table or global secondary index.
Type: [AutoScalingSettingsUpdate](API_AutoScalingSettingsUpdate.md) object
Required: No

 ** [ReplicaUpdates](#API_UpdateTableReplicaAutoScaling_RequestSyntax) **   <a name="DDB-UpdateTableReplicaAutoScaling-request-ReplicaUpdates"></a>
Represents the auto scaling settings of replicas of the table that will be modified.
Type: Array of [ReplicaAutoScalingUpdate](API_ReplicaAutoScalingUpdate.md) objects
Array Members: Minimum number of 1 item.
Required: No

## Response Syntax
<a name="API_UpdateTableReplicaAutoScaling_ResponseSyntax"></a>

```
{
   "TableAutoScalingDescription": {
      "Replicas": [
         {
            "GlobalSecondaryIndexes": [
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
                  }
               }
            ],
            "RegionName": "string",
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
            "ReplicaStatus": "string"
         }
      ],
      "TableName": "string",
      "TableStatus": "string"
   }
}
```

## Response Elements
<a name="API_UpdateTableReplicaAutoScaling_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TableAutoScalingDescription](#API_UpdateTableReplicaAutoScaling_ResponseSyntax) **   <a name="DDB-UpdateTableReplicaAutoScaling-response-TableAutoScalingDescription"></a>
Returns information about the auto scaling settings of a table with replicas.
Type: [TableAutoScalingDescription](API_TableAutoScalingDescription.md) object

## Errors
<a name="API_UpdateTableReplicaAutoScaling_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceInUseException **
The operation conflicts with the resource's availability. For example:
+ You attempted to recreate an existing table.
+ You tried to delete a table currently in the `CREATING` state.
+ You tried to update a resource that was already being updated.
When appropriate, wait for the ongoing update to complete and attempt the request again.
 ** message **
The resource which is being attempted to be changed is in use.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The resource which is being requested does not exist.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTableReplicaAutoScaling_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/UpdateTableReplicaAutoScaling)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/UpdateTableReplicaAutoScaling)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/UpdateTableReplicaAutoScaling)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/UpdateTableReplicaAutoScaling)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/UpdateTableReplicaAutoScaling)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/UpdateTableReplicaAutoScaling)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/UpdateTableReplicaAutoScaling)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/UpdateTableReplicaAutoScaling)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/UpdateTableReplicaAutoScaling)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/UpdateTableReplicaAutoScaling)
