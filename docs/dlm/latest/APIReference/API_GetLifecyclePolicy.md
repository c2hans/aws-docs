---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_GetLifecyclePolicy.html
---

# GetLifecyclePolicy
<a name="API_GetLifecyclePolicy"></a>

Gets detailed information about the specified lifecycle policy.

## Request Syntax
<a name="API_GetLifecyclePolicy_RequestSyntax"></a>

```
GET /policies/{{policyId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLifecyclePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyId](#API_GetLifecyclePolicy_RequestSyntax) **   <a name="dlm-GetLifecyclePolicy-request-uri-PolicyId"></a>
The identifier of the lifecycle policy.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `policy-[a-f0-9]+`
Required: Yes

## Request Body
<a name="API_GetLifecyclePolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetLifecyclePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Policy": {
      "DateCreated": "string",
      "DateModified": "string",
      "DefaultPolicy": boolean,
      "Description": "string",
      "ExecutionRoleArn": "string",
      "PolicyArn": "string",
      "PolicyDetails": {
         "Actions": [
            {
               "CrossRegionCopy": [
                  {
                     "EncryptionConfiguration": {
                        "CmkArn": "string",
                        "Encrypted": boolean
                     },
                     "RetainRule": {
                        "Interval": number,
                        "IntervalUnit": "string"
                     },
                     "Target": "string"
                  }
               ],
               "Name": "string"
            }
         ],
         "CopyTags": boolean,
         "CreateInterval": number,
         "CrossRegionCopyTargets": [
            {
               "TargetRegion": "string"
            }
         ],
         "EventSource": {
            "Parameters": {
               "DescriptionRegex": "string",
               "EventType": "string",
               "SnapshotOwner": [ "string" ]
            },
            "Type": "string"
         },
         "Exclusions": {
            "ExcludeBootVolumes": boolean,
            "ExcludeTags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "ExcludeVolumeTypes": [ "string" ]
         },
         "ExtendDeletion": boolean,
         "Parameters": {
            "ExcludeBootVolume": boolean,
            "ExcludeDataVolumeTags": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "NoReboot": boolean
         },
         "PolicyLanguage": "string",
         "PolicyType": "string",
         "ResourceLocations": [ "string" ],
         "ResourceType": "string",
         "ResourceTypes": [ "string" ],
         "RetainInterval": number,
         "Schedules": [
            {
               "ArchiveRule": {
                  "RetainRule": {
                     "RetentionArchiveTier": {
                        "Count": number,
                        "Interval": number,
                        "IntervalUnit": "string"
                     }
                  }
               },
               "CopyTags": boolean,
               "CreateRule": {
                  "CronExpression": "string",
                  "Interval": number,
                  "IntervalUnit": "string",
                  "Location": "string",
                  "Scripts": [
                     {
                        "ExecuteOperationOnScriptFailure": boolean,
                        "ExecutionHandler": "string",
                        "ExecutionHandlerService": "string",
                        "ExecutionTimeout": number,
                        "MaximumRetryCount": number,
                        "Stages": [ "string" ]
                     }
                  ],
                  "Times": [ "string" ]
               },
               "CrossRegionCopyRules": [
                  {
                     "CmkArn": "string",
                     "CopyTags": boolean,
                     "DeprecateRule": {
                        "Interval": number,
                        "IntervalUnit": "string"
                     },
                     "Encrypted": boolean,
                     "RetainRule": {
                        "Interval": number,
                        "IntervalUnit": "string"
                     },
                     "Target": "string",
                     "TargetRegion": "string"
                  }
               ],
               "DeprecateRule": {
                  "Count": number,
                  "Interval": number,
                  "IntervalUnit": "string"
               },
               "FastRestoreRule": {
                  "AvailabilityZoneIds": [ "string" ],
                  "AvailabilityZones": [ "string" ],
                  "Count": number,
                  "Interval": number,
                  "IntervalUnit": "string"
               },
               "Name": "string",
               "RetainRule": {
                  "Count": number,
                  "Interval": number,
                  "IntervalUnit": "string"
               },
               "ShareRules": [
                  {
                     "TargetAccounts": [ "string" ],
                     "UnshareInterval": number,
                     "UnshareIntervalUnit": "string"
                  }
               ],
               "TagsToAdd": [
                  {
                     "Key": "string",
                     "Value": "string"
                  }
               ],
               "VariableTags": [
                  {
                     "Key": "string",
                     "Value": "string"
                  }
               ]
            }
         ],
         "TargetTags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ]
      },
      "PolicyId": "string",
      "State": "string",
      "StatusMessage": "string",
      "Tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_GetLifecyclePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_GetLifecyclePolicy_ResponseSyntax) **   <a name="dlm-GetLifecyclePolicy-response-Policy"></a>
Detailed information about the lifecycle policy.
Type: [LifecyclePolicy](API_LifecyclePolicy.md) object

## Errors
<a name="API_GetLifecyclePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service failed in an unexpected way.
HTTP Status Code: 500

 ** LimitExceededException **
The request failed because a limit was exceeded.
 ** ResourceType **
Value is the type of resource for which a limit was exceeded.
HTTP Status Code: 429

 ** ResourceNotFoundException **
A requested resource was not found.
 ** ResourceIds **
Value is a list of resource IDs that were not found.
 ** ResourceType **
Value is the type of resource that was not found.
HTTP Status Code: 404

## See Also
<a name="API_GetLifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dlm-2018-01-12/GetLifecyclePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dlm-2018-01-12/GetLifecyclePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/GetLifecyclePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dlm-2018-01-12/GetLifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/GetLifecyclePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dlm-2018-01-12/GetLifecyclePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dlm-2018-01-12/GetLifecyclePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dlm-2018-01-12/GetLifecyclePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dlm-2018-01-12/GetLifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/GetLifecyclePolicy)
