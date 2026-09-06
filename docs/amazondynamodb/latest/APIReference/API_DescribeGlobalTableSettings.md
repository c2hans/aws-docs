---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeGlobalTableSettings.html
---

# DescribeGlobalTableSettings
<a name="API_DescribeGlobalTableSettings"></a>

Describes Region-specific settings for a global table.

**Important**
This documentation is for version 2017.11.29 (Legacy) of global tables, which should be avoided for new global tables. Customers should use [Global Tables version 2019.11.21 (Current)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) when possible, because it provides greater flexibility, higher efficiency, and consumes less write capacity than 2017.11.29 (Legacy).
To determine which version you're using, see [Determining the global table version you are using](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.DetermineVersion.html). To update existing global tables from version 2017.11.29 (Legacy) to version 2019.11.21 (Current), see [Upgrading global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_upgrade.html).

## Request Syntax
<a name="API_DescribeGlobalTableSettings_RequestSyntax"></a>

```
{
   "GlobalTableName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeGlobalTableSettings_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GlobalTableName](#API_DescribeGlobalTableSettings_RequestSyntax) **   <a name="DDB-DescribeGlobalTableSettings-request-GlobalTableName"></a>
The name of the global table to describe.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeGlobalTableSettings_ResponseSyntax"></a>

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
<a name="API_DescribeGlobalTableSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GlobalTableName](#API_DescribeGlobalTableSettings_ResponseSyntax) **   <a name="DDB-DescribeGlobalTableSettings-response-GlobalTableName"></a>
The name of the global table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [ReplicaSettings](#API_DescribeGlobalTableSettings_ResponseSyntax) **   <a name="DDB-DescribeGlobalTableSettings-response-ReplicaSettings"></a>
The Region-specific settings for the global table.
Type: Array of [ReplicaSettingsDescription](API_ReplicaSettingsDescription.md) objects

## Errors
<a name="API_DescribeGlobalTableSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** GlobalTableNotFoundException **
The specified global table does not exist.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

## See Also
<a name="API_DescribeGlobalTableSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/DescribeGlobalTableSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/DescribeGlobalTableSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/DescribeGlobalTableSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/DescribeGlobalTableSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/DescribeGlobalTableSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/DescribeGlobalTableSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/DescribeGlobalTableSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/DescribeGlobalTableSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/DescribeGlobalTableSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/DescribeGlobalTableSettings)
