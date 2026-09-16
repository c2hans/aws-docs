---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_UpdateLifecyclePolicy.html
---

# UpdateLifecyclePolicy
<a name="API_UpdateLifecyclePolicy"></a>

Updates the specified lifecycle policy.

For more information about updating a policy, see [Modify lifecycle policies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/view-modify-delete.html#modify).

## Request Syntax
<a name="API_UpdateLifecyclePolicy_RequestSyntax"></a>

```
PATCH /policies/{{policyId}} HTTP/1.1
Content-type: application/json

{
   "CopyTags": {{boolean}},
   "CreateInterval": {{number}},
   "CrossRegionCopyTargets": [
      {
         "TargetRegion": "{{string}}"
      }
   ],
   "Description": "{{string}}",
   "Exclusions": {
      "ExcludeBootVolumes": {{boolean}},
      "ExcludeTags": [
         {
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ExcludeVolumeTypes": [ "{{string}}" ]
   },
   "ExecutionRoleArn": "{{string}}",
   "ExtendDeletion": {{boolean}},
   "PolicyDetails": {
      "Actions": [
         {
            "CrossRegionCopy": [
               {
                  "EncryptionConfiguration": {
                     "CmkArn": "{{string}}",
                     "Encrypted": {{boolean}}
                  },
                  "RetainRule": {
                     "Interval": {{number}},
                     "IntervalUnit": "{{string}}"
                  },
                  "Target": "{{string}}"
               }
            ],
            "Name": "{{string}}"
         }
      ],
      "CopyTags": {{boolean}},
      "CreateInterval": {{number}},
      "CrossRegionCopyTargets": [
         {
            "TargetRegion": "{{string}}"
         }
      ],
      "EventSource": {
         "Parameters": {
            "DescriptionRegex": "{{string}}",
            "EventType": "{{string}}",
            "SnapshotOwner": [ "{{string}}" ]
         },
         "Type": "{{string}}"
      },
      "Exclusions": {
         "ExcludeBootVolumes": {{boolean}},
         "ExcludeTags": [
            {
               "Key": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "ExcludeVolumeTypes": [ "{{string}}" ]
      },
      "ExtendDeletion": {{boolean}},
      "Parameters": {
         "ExcludeBootVolume": {{boolean}},
         "ExcludeDataVolumeTags": [
            {
               "Key": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "NoReboot": {{boolean}}
      },
      "PolicyLanguage": "{{string}}",
      "PolicyType": "{{string}}",
      "ResourceLocations": [ "{{string}}" ],
      "ResourceType": "{{string}}",
      "ResourceTypes": [ "{{string}}" ],
      "RetainInterval": {{number}},
      "Schedules": [
         {
            "ArchiveRule": {
               "RetainRule": {
                  "RetentionArchiveTier": {
                     "Count": {{number}},
                     "Interval": {{number}},
                     "IntervalUnit": "{{string}}"
                  }
               }
            },
            "CopyTags": {{boolean}},
            "CreateRule": {
               "CronExpression": "{{string}}",
               "Interval": {{number}},
               "IntervalUnit": "{{string}}",
               "Location": "{{string}}",
               "Scripts": [
                  {
                     "ExecuteOperationOnScriptFailure": {{boolean}},
                     "ExecutionHandler": "{{string}}",
                     "ExecutionHandlerService": "{{string}}",
                     "ExecutionTimeout": {{number}},
                     "MaximumRetryCount": {{number}},
                     "Stages": [ "{{string}}" ]
                  }
               ],
               "Times": [ "{{string}}" ]
            },
            "CrossRegionCopyRules": [
               {
                  "CmkArn": "{{string}}",
                  "CopyTags": {{boolean}},
                  "DeprecateRule": {
                     "Interval": {{number}},
                     "IntervalUnit": "{{string}}"
                  },
                  "Encrypted": {{boolean}},
                  "RetainRule": {
                     "Interval": {{number}},
                     "IntervalUnit": "{{string}}"
                  },
                  "Target": "{{string}}",
                  "TargetRegion": "{{string}}"
               }
            ],
            "DeprecateRule": {
               "Count": {{number}},
               "Interval": {{number}},
               "IntervalUnit": "{{string}}"
            },
            "FastRestoreRule": {
               "AvailabilityZoneIds": [ "{{string}}" ],
               "AvailabilityZones": [ "{{string}}" ],
               "Count": {{number}},
               "Interval": {{number}},
               "IntervalUnit": "{{string}}"
            },
            "Name": "{{string}}",
            "RetainRule": {
               "Count": {{number}},
               "Interval": {{number}},
               "IntervalUnit": "{{string}}"
            },
            "ShareRules": [
               {
                  "TargetAccounts": [ "{{string}}" ],
                  "UnshareInterval": {{number}},
                  "UnshareIntervalUnit": "{{string}}"
               }
            ],
            "TagsToAdd": [
               {
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ],
            "VariableTags": [
               {
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         }
      ],
      "TargetTags": [
         {
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ]
   },
   "RetainInterval": {{number}},
   "State": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateLifecyclePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyId](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="dlm-UpdateLifecyclePolicy-request-uri-PolicyId"></a>
The identifier of the lifecycle policy.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `policy-[a-f0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateLifecyclePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CopyTags](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="dlm-UpdateLifecyclePolicy-request-CopyTags"></a>
 **[Default policies only]** Indicates whether the policy should copy tags from the source resource to the snapshot or AMI.
Type: Boolean
Required: No

 ** [CreateInterval](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="dlm-UpdateLifecyclePolicy-request-CreateInterval"></a>
 **[Default policies only]** Specifies how often the policy should run and create snapshots or AMIs. The creation frequency can range from 1 to 7 days.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [CrossRegionCopyTargets](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="dlm-UpdateLifecyclePolicy-request-CrossRegionCopyTargets"></a>
 **[Default policies only]** Specifies destination Regions for snapshot or AMI copies. You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.
Type: Array of [CrossRegionCopyTarget](API_CrossRegionCopyTarget.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

 ** [Description](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="dlm-UpdateLifecyclePolicy-request-Description"></a>
A description of the lifecycle policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[0-9A-Za-z _-]+`
Required: No

 ** [Exclusions](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="dlm-UpdateLifecyclePolicy-request-Exclusions"></a>
 **[Default policies only]** Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.
Type: [Exclusions](API_Exclusions.md) object
Required: No

 ** [ExecutionRoleArn](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="dlm-UpdateLifecyclePolicy-request-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]{1,4}){0,2}:iam::\d+:role/.*`
Required: No

 ** [ExtendDeletion](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="dlm-UpdateLifecyclePolicy-request-ExtendDeletion"></a>
 **[Default policies only]** Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state.
By default (**ExtendDeletion=false**):
+ If a source resource is deleted, Amazon Data Lifecycle Manager will continue to delete previously created snapshots or AMIs, up to but not including the last one, based on the specified retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots or AMIs, including the last one, specify `true`.
+ If a policy enters the error, disabled, or deleted state, Amazon Data Lifecycle Manager stops deleting snapshots and AMIs. If you want Amazon Data Lifecycle Manager to continue deleting snapshots or AMIs, including the last one, if the policy enters one of these states, specify `true`.
If you enable extended deletion (**ExtendDeletion=true**), you override both default behaviors simultaneously.
Default: false
Type: Boolean
Required: No

 ** [PolicyDetails](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="dlm-UpdateLifecyclePolicy-request-PolicyDetails"></a>
The configuration of the lifecycle policy. You cannot update the policy type or the resource type.
Type: [PolicyDetails](API_PolicyDetails.md) object
Required: No

 ** [RetainInterval](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="dlm-UpdateLifecyclePolicy-request-RetainInterval"></a>
 **[Default policies only]** Specifies how long the policy should retain snapshots or AMIs before deleting them. The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [State](#API_UpdateLifecyclePolicy_RequestSyntax) **   <a name="dlm-UpdateLifecyclePolicy-request-State"></a>
The desired activation state of the lifecycle policy after creation.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## Response Syntax
<a name="API_UpdateLifecyclePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateLifecyclePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLifecyclePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service failed in an unexpected way.
HTTP Status Code: 500

 ** InvalidRequestException **
Bad request. The request is missing required parameters or has invalid parameters.
 ** MutuallyExclusiveParameters **
The request included parameters that cannot be provided together.
 ** RequiredParameters **
The request omitted one or more required parameters.
HTTP Status Code: 400

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
<a name="API_UpdateLifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dlm-2018-01-12/UpdateLifecyclePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dlm-2018-01-12/UpdateLifecyclePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/UpdateLifecyclePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dlm-2018-01-12/UpdateLifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/UpdateLifecyclePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dlm-2018-01-12/UpdateLifecyclePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dlm-2018-01-12/UpdateLifecyclePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dlm-2018-01-12/UpdateLifecyclePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dlm-2018-01-12/UpdateLifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/UpdateLifecyclePolicy)
