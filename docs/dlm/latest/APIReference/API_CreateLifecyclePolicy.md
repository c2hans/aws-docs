---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_CreateLifecyclePolicy.html
---

# CreateLifecyclePolicy
<a name="API_CreateLifecyclePolicy"></a>

Creates an Amazon Data Lifecycle Manager lifecycle policy. Amazon Data Lifecycle Manager supports the following policy types:
+ Custom EBS snapshot policy
+ Custom EBS-backed AMI policy
+ Cross-account copy event policy
+ Default policy for EBS snapshots
+ Default policy for EBS-backed AMIs

For more information, see [ Default policies vs custom policies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/policy-differences.html).

**Important**
If you create a default policy, you can specify the request parameters either in the request body, or in the PolicyDetails request structure, but not both.

## Request Syntax
<a name="API_CreateLifecyclePolicy_RequestSyntax"></a>

```
POST /policies HTTP/1.1
Content-type: application/json

{
   "CopyTags": {{boolean}},
   "CreateInterval": {{number}},
   "CrossRegionCopyTargets": [
      {
         "TargetRegion": "{{string}}"
      }
   ],
   "DefaultPolicy": "{{string}}",
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
   "State": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateLifecyclePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateLifecyclePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CopyTags](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="dlm-CreateLifecyclePolicy-request-CopyTags"></a>
 **[Default policies only]** Indicates whether the policy should copy tags from the source resource to the snapshot or AMI. If you do not specify a value, the default is `false`.
Default: false
Type: Boolean
Required: No

 ** [CreateInterval](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="dlm-CreateLifecyclePolicy-request-CreateInterval"></a>
 **[Default policies only]** Specifies how often the policy should run and create snapshots or AMIs. The creation frequency can range from 1 to 7 days. If you do not specify a value, the default is 1.
Default: 1
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [CrossRegionCopyTargets](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="dlm-CreateLifecyclePolicy-request-CrossRegionCopyTargets"></a>
 **[Default policies only]** Specifies destination Regions for snapshot or AMI copies. You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.
Type: Array of [CrossRegionCopyTarget](API_CrossRegionCopyTarget.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

 ** [DefaultPolicy](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="dlm-CreateLifecyclePolicy-request-DefaultPolicy"></a>
 **[Default policies only]** Specify the type of default policy to create.
+ To create a default policy for EBS snapshots, that creates snapshots of all volumes in the Region that do not have recent backups, specify `VOLUME`.
+ To create a default policy for EBS-backed AMIs, that creates EBS-backed AMIs from all instances in the Region that do not have recent backups, specify `INSTANCE`.
Type: String
Valid Values: `VOLUME | INSTANCE`
Required: No

 ** [Description](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="dlm-CreateLifecyclePolicy-request-Description"></a>
A description of the lifecycle policy. The characters ^[0-9A-Za-z \_-]\+$ are supported.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[0-9A-Za-z _-]+`
Required: Yes

 ** [Exclusions](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="dlm-CreateLifecyclePolicy-request-Exclusions"></a>
 **[Default policies only]** Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.
Type: [Exclusions](API_Exclusions.md) object
Required: No

 ** [ExecutionRoleArn](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="dlm-CreateLifecyclePolicy-request-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]{1,4}){0,2}:iam::\d+:role/.*`
Required: Yes

 ** [ExtendDeletion](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="dlm-CreateLifecyclePolicy-request-ExtendDeletion"></a>
 **[Default policies only]** Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state.
By default (**ExtendDeletion=false**):
+ If a source resource is deleted, Amazon Data Lifecycle Manager will continue to delete previously created snapshots or AMIs, up to but not including the last one, based on the specified retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots or AMIs, including the last one, specify `true`.
+ If a policy enters the error, disabled, or deleted state, Amazon Data Lifecycle Manager stops deleting snapshots and AMIs. If you want Amazon Data Lifecycle Manager to continue deleting snapshots or AMIs, including the last one, if the policy enters one of these states, specify `true`.
If you enable extended deletion (**ExtendDeletion=true**), you override both default behaviors simultaneously.
If you do not specify a value, the default is `false`.
Default: false
Type: Boolean
Required: No

 ** [PolicyDetails](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="dlm-CreateLifecyclePolicy-request-PolicyDetails"></a>
The configuration details of the lifecycle policy.
If you create a default policy, you can specify the request parameters either in the request body, or in the PolicyDetails request structure, but not both.
Type: [PolicyDetails](API_PolicyDetails.md) object
Required: No

 ** [RetainInterval](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="dlm-CreateLifecyclePolicy-request-RetainInterval"></a>
 **[Default policies only]** Specifies how long the policy should retain snapshots or AMIs before deleting them. The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time. If you do not specify a value, the default is 7.
Default: 7
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [State](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="dlm-CreateLifecyclePolicy-request-State"></a>
The activation state of the lifecycle policy after creation.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** [Tags](#API_CreateLifecyclePolicy_RequestSyntax) **   <a name="dlm-CreateLifecyclePolicy-request-Tags"></a>
The tags to apply to the lifecycle policy during creation.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\p{all}]*`
Required: No

## Response Syntax
<a name="API_CreateLifecyclePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PolicyId": "string"
}
```

## Response Elements
<a name="API_CreateLifecyclePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PolicyId](#API_CreateLifecyclePolicy_ResponseSyntax) **   <a name="dlm-CreateLifecyclePolicy-response-PolicyId"></a>
The identifier of the lifecycle policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `policy-[a-f0-9]+`

## Errors
<a name="API_CreateLifecyclePolicy_Errors"></a>

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

## Examples
<a name="API_CreateLifecyclePolicy_Examples"></a>

### Example 1: Default policy for EBS snapshots
<a name="API_CreateLifecyclePolicy_Example_1"></a>

The following example creates a default policy for EBS snapshots that uses the default IAM role for managing EBS snapshots. The policy creates snapshots daily, retains snapshots for 3 days, and excludes `st1` volumes, boot volumes, and volumes tagged with `purpose=testing`.

#### Sample Request
<a name="API_CreateLifecyclePolicy_Example_1_Request"></a>

```
POST /policies HTTP/1.1
Content-type: application/json
{
   "CopyTags": true,
   "CreateInterval": 1,
   "CrossRegionCopyTargets": [
      {
         "TargetRegion": "us-east-1"
      }
   ],
   "DefaultPolicy": "VOLUME",
   "Description": "Daily default snapshot policy",
   "Exclusions": {
      "ExcludeBootVolumes": true,
      "ExcludeTags": [
         {
            "Key": "purpose",
            "Value": "testing"
         }
      ],
      "ExcludeVolumeTypes": [ "st1" ]
   },
   "ExecutionRoleArn": "arn:aws:iam::123456789012:role/AWSDataLifecycleManagerDefaultRole",
   "ExtendDeletion": true,
   "RetainInterval": 3,
   "State": "ENABLED",
   "Tags": {
      "environment" : "prod"
   }
}
```

### Example 2: Default policy for EBS snapshots with default settings
<a name="API_CreateLifecyclePolicy_Example_2"></a>

The example creates a default EBS snapshots policy using the default settings. The policy uses the default role for managing EBS snapshots, creates snapshots daily, and retains snapshots for 7 days.

#### Sample Request
<a name="API_CreateLifecyclePolicy_Example_2_Request"></a>

```
POST /policies HTTP/1.1
Content-type: application/json
{
   "DefaultPolicy": "VOLUME",
   "Description": "Daily default snapshot policy",
   "ExecutionRoleArn": "arn:aws:iam::123456789012:role/AWSDataLifecycleManagerDefaultRole",
   "State": "ENABLED"
}
```

### Example 3: Custom EBS-backed AMI policy
<a name="API_CreateLifecyclePolicy_Example_3"></a>

The following example creates a custom age-based EBS-backed AMI policy that targets instances tagged with `environment=prod`, but excludes volumes attached as boot volumes. The policy uses the default IAM role for managing EBS-backed AMIs. It creates AMIs every 12 hours, starting at 17:00 UTC, retains AMIs for 7 days, and deprecates the oldest AMI after 2 days. The policy also copies encrypted AMIs to the `us-east-1` Region, and retains those copies for 2 days.

#### Sample Request
<a name="API_CreateLifecyclePolicy_Example_3_Request"></a>

```
POST /policies HTTP/1.1
Content-type: application/json

{
   "Description": "Custom AMI policy",
   "ExecutionRoleArn": "arn:aws:iam::12345678910:role/AWSDataLifecycleManagerDefaultRoleForAMIManagement",
   "PolicyDetails": {
      "Parameters": {
         "ExcludeBootVolume": false,
         "NoReboot": false
      },
      "PolicyType": "IMAGE_MANAGEMENT",
      "ResourceTypes": [ "INSTANCE" ],
      "Schedules": [
         {
            "CopyTags": true,
            "CreateRule": {
               "Interval": 12,
               "IntervalUnit": "HOURS",
               "Times": [ "17:30" ]
            },
            "CrossRegionCopyRules": [
               {
                  "CopyTags": true,
                  "Encrypted": true,
                  "RetainRule": {
                     "Interval": 2,
                     "IntervalUnit": "DAYS"
                  },
                  "Target": "us-east-1"
               }
            ],
            "DeprecateRule": {
               "Interval": 2,
               "IntervalUnit": "DAYS"
            },
            "Name": "Schedule1",
            "RetainRule": {
               "Interval": 7,
               "IntervalUnit": "DAYS"
            }
         }
      ],
      "TargetTags": [
         {
            "Key": "environment",
            "Value": "prod"
         }
      ]
   },
   "State": "ENABLED"
}
```

## See Also
<a name="API_CreateLifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dlm-2018-01-12/CreateLifecyclePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dlm-2018-01-12/CreateLifecyclePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/CreateLifecyclePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dlm-2018-01-12/CreateLifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/CreateLifecyclePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dlm-2018-01-12/CreateLifecyclePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dlm-2018-01-12/CreateLifecyclePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dlm-2018-01-12/CreateLifecyclePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dlm-2018-01-12/CreateLifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/CreateLifecyclePolicy)
