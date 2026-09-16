---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_GetTableAutoScalingSettings.html
---

# GetTableAutoScalingSettings
<a name="API_GetTableAutoScalingSettings"></a>

Returns auto scaling related settings of the specified table in JSON format. If the table is a multi-Region table, the AWS Region specific auto scaling settings of the table are included.

Amazon Keyspaces auto scaling helps you provision throughput capacity for variable workloads efficiently by increasing and decreasing your table's read and write capacity automatically in response to application traffic. For more information, see [Managing throughput capacity automatically with Amazon Keyspaces auto scaling](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html) in the *Amazon Keyspaces Developer Guide*.

**Important**
 `GetTableAutoScalingSettings` can't be used as an action in an IAM policy.

To define permissions for `GetTableAutoScalingSettings`, you must allow the following two actions in the IAM policy statement's `Action` element:
+  `application-autoscaling:DescribeScalableTargets`
+  `application-autoscaling:DescribeScalingPolicies`

## Request Syntax
<a name="API_GetTableAutoScalingSettings_RequestSyntax"></a>

```
{
   "keyspaceName": "{{string}}",
   "tableName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTableAutoScalingSettings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [keyspaceName](#API_GetTableAutoScalingSettings_RequestSyntax) **   <a name="keyspaces-GetTableAutoScalingSettings-request-keyspaceName"></a>
The name of the keyspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** [tableName](#API_GetTableAutoScalingSettings_RequestSyntax) **   <a name="keyspaces-GetTableAutoScalingSettings-request-tableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

## Response Syntax
<a name="API_GetTableAutoScalingSettings_ResponseSyntax"></a>

```
{
   "autoScalingSpecification": {
      "readCapacityAutoScaling": {
         "autoScalingDisabled": boolean,
         "maximumUnits": number,
         "minimumUnits": number,
         "scalingPolicy": {
            "targetTrackingScalingPolicyConfiguration": {
               "disableScaleIn": boolean,
               "scaleInCooldown": number,
               "scaleOutCooldown": number,
               "targetValue": number
            }
         }
      },
      "writeCapacityAutoScaling": {
         "autoScalingDisabled": boolean,
         "maximumUnits": number,
         "minimumUnits": number,
         "scalingPolicy": {
            "targetTrackingScalingPolicyConfiguration": {
               "disableScaleIn": boolean,
               "scaleInCooldown": number,
               "scaleOutCooldown": number,
               "targetValue": number
            }
         }
      }
   },
   "keyspaceName": "string",
   "replicaSpecifications": [
      {
         "autoScalingSpecification": {
            "readCapacityAutoScaling": {
               "autoScalingDisabled": boolean,
               "maximumUnits": number,
               "minimumUnits": number,
               "scalingPolicy": {
                  "targetTrackingScalingPolicyConfiguration": {
                     "disableScaleIn": boolean,
                     "scaleInCooldown": number,
                     "scaleOutCooldown": number,
                     "targetValue": number
                  }
               }
            },
            "writeCapacityAutoScaling": {
               "autoScalingDisabled": boolean,
               "maximumUnits": number,
               "minimumUnits": number,
               "scalingPolicy": {
                  "targetTrackingScalingPolicyConfiguration": {
                     "disableScaleIn": boolean,
                     "scaleInCooldown": number,
                     "scaleOutCooldown": number,
                     "targetValue": number
                  }
               }
            }
         },
         "region": "string"
      }
   ],
   "resourceArn": "string",
   "tableName": "string"
}
```

## Response Elements
<a name="API_GetTableAutoScalingSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autoScalingSpecification](#API_GetTableAutoScalingSettings_ResponseSyntax) **   <a name="keyspaces-GetTableAutoScalingSettings-response-autoScalingSpecification"></a>
The auto scaling settings of the table.
Type: [AutoScalingSpecification](API_AutoScalingSpecification.md) object

 ** [keyspaceName](#API_GetTableAutoScalingSettings_ResponseSyntax) **   <a name="keyspaces-GetTableAutoScalingSettings-response-keyspaceName"></a>
The name of the keyspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`

 ** [replicaSpecifications](#API_GetTableAutoScalingSettings_ResponseSyntax) **   <a name="keyspaces-GetTableAutoScalingSettings-response-replicaSpecifications"></a>
The AWS Region specific settings of a multi-Region table. Returns the settings for all Regions the table is replicated in.
Type: Array of [ReplicaAutoScalingSpecification](API_ReplicaAutoScalingSpecification.md) objects
Array Members: Minimum number of 0 items.

 ** [resourceArn](#API_GetTableAutoScalingSettings_ResponseSyntax) **   <a name="keyspaces-GetTableAutoScalingSettings-response-resourceArn"></a>
The Amazon Resource Name (ARN) of the table.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1000.
Pattern: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`

 ** [tableName](#API_GetTableAutoScalingSettings_ResponseSyntax) **   <a name="keyspaces-GetTableAutoScalingSettings-response-tableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`

## Errors
<a name="API_GetTableAutoScalingSettings_Errors"></a>

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
<a name="API_GetTableAutoScalingSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/keyspaces-2022-02-10/GetTableAutoScalingSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/keyspaces-2022-02-10/GetTableAutoScalingSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/GetTableAutoScalingSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/keyspaces-2022-02-10/GetTableAutoScalingSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/GetTableAutoScalingSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/keyspaces-2022-02-10/GetTableAutoScalingSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/keyspaces-2022-02-10/GetTableAutoScalingSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/keyspaces-2022-02-10/GetTableAutoScalingSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/keyspaces-2022-02-10/GetTableAutoScalingSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/GetTableAutoScalingSettings)
