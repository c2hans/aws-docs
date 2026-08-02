---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_CreateVolume.html
---

# CreateVolume
<a name="API_CreateVolume"></a>

Creates a new volume for WorkSpace Instances.

## Request Syntax
<a name="API_CreateVolume_RequestSyntax"></a>

```
{
   "AvailabilityZone": "{{string}}",
   "ClientToken": "{{string}}",
   "Encrypted": {{boolean}},
   "Iops": {{number}},
   "KmsKeyId": "{{string}}",
   "SizeInGB": {{number}},
   "SnapshotId": "{{string}}",
   "TagSpecifications": [
      {
         "ResourceType": "{{string}}",
         "Tags": [
            {
               "Key": "{{string}}",
               "Value": "{{string}}"
            }
         ]
      }
   ],
   "Throughput": {{number}},
   "VolumeType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateVolume_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AvailabilityZone](#API_CreateVolume_RequestSyntax) **   <a name="workspacesinstances-CreateVolume-request-AvailabilityZone"></a>
Availability zone for the volume.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: Yes

 ** [ClientToken](#API_CreateVolume_RequestSyntax) **   <a name="workspacesinstances-CreateVolume-request-ClientToken"></a>
Unique token to prevent duplicate volume creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [Encrypted](#API_CreateVolume_RequestSyntax) **   <a name="workspacesinstances-CreateVolume-request-Encrypted"></a>
Indicates if the volume should be encrypted.
Type: Boolean
Required: No

 ** [Iops](#API_CreateVolume_RequestSyntax) **   <a name="workspacesinstances-CreateVolume-request-Iops"></a>
Input/output operations per second for the volume.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [KmsKeyId](#API_CreateVolume_RequestSyntax) **   <a name="workspacesinstances-CreateVolume-request-KmsKeyId"></a>
KMS key for volume encryption.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [SizeInGB](#API_CreateVolume_RequestSyntax) **   <a name="workspacesinstances-CreateVolume-request-SizeInGB"></a>
Volume size in gigabytes.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [SnapshotId](#API_CreateVolume_RequestSyntax) **   <a name="workspacesinstances-CreateVolume-request-SnapshotId"></a>
Source snapshot for volume creation.
Type: String
Pattern: `snap-[0-9a-zA-Z]{1,63}`
Required: No

 ** [TagSpecifications](#API_CreateVolume_RequestSyntax) **   <a name="workspacesinstances-CreateVolume-request-TagSpecifications"></a>
Metadata tags for the volume.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

 ** [Throughput](#API_CreateVolume_RequestSyntax) **   <a name="workspacesinstances-CreateVolume-request-Throughput"></a>
Volume throughput performance.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [VolumeType](#API_CreateVolume_RequestSyntax) **   <a name="workspacesinstances-CreateVolume-request-VolumeType"></a>
Type of EBS volume.
Type: String
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
Required: No

## Response Syntax
<a name="API_CreateVolume_ResponseSyntax"></a>

```
{
   "VolumeId": "string"
}
```

## Response Elements
<a name="API_CreateVolume_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VolumeId](#API_CreateVolume_ResponseSyntax) **   <a name="workspacesinstances-CreateVolume-response-VolumeId"></a>
Unique identifier for the new volume.
Type: String
Pattern: `vol-[0-9a-zA-Z]{1,63}`

## Errors
<a name="API_CreateVolume_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Indicates insufficient permissions to perform the requested action.
 ** Message **
Detailed explanation of the access denial.
HTTP Status Code: 400

 ** ConflictException **
Signals a conflict with the current state of the resource.
 ** Message **
Description of the conflict encountered.
 ** ResourceId **
Identifier of the conflicting resource.
 ** ResourceType **
Type of the conflicting resource.
HTTP Status Code: 400

 ** InternalServerException **
Indicates an unexpected server-side error occurred.
 ** Message **
Description of the internal server error.
 ** RetryAfterSeconds **
Recommended wait time before retrying the request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
Indicates that a service quota has been exceeded.
 ** Message **
Description of the quota limitation.
 ** QuotaCode **
Specific code for the exceeded quota.
 ** ResourceId **
Identifier of the resource related to the quota.
 ** ResourceType **
Type of resource related to the quota.
 ** ServiceCode **
Code identifying the service with the quota limitation.
HTTP Status Code: 400

 ** ThrottlingException **
Indicates the request rate has exceeded limits.
 ** Message **
Description of the throttling event.
 ** QuotaCode **
Specific code for the throttling quota.
 ** RetryAfterSeconds **
Recommended wait time before retrying the request.
 ** ServiceCode **
Code identifying the service experiencing throttling.
HTTP Status Code: 400

 ** ValidationException **
Indicates invalid input parameters in the request.
 ** FieldList **
List of fields that failed validation.
 ** Message **
Overall description of validation failures.
 ** Reason **
Specific reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_CreateVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-instances-2022-07-26/CreateVolume)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-instances-2022-07-26/CreateVolume)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/CreateVolume)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-instances-2022-07-26/CreateVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/CreateVolume)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-instances-2022-07-26/CreateVolume)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-instances-2022-07-26/CreateVolume)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-instances-2022-07-26/CreateVolume)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-instances-2022-07-26/CreateVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/CreateVolume)
