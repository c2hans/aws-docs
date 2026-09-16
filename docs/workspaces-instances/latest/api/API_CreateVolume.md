---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_CreateVolume.html
---

# CreateVolume
<a name="API_CreateVolume"></a>

Creates a new volume for WorkSpace Instances.

## Request Parameters
<a name="API_CreateVolume_RequestParameters"></a>

 ** AvailabilityZone **
Availability zone for the volume.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: Yes

 ** ClientToken **
Unique token to prevent duplicate volume creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x20-\x7E]+`
Required: No

 ** Encrypted **
Indicates if the volume should be encrypted.
Type: Boolean
Required: No

 ** Iops **
Input/output operations per second for the volume.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** KmsKeyId **
KMS key for volume encryption.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** SizeInGB **
Volume size in gigabytes.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** SnapshotId **
Source snapshot for volume creation.
Type: String
Pattern: `snap-[0-9a-zA-Z]{1,63}`
Required: No

 ** TagSpecifications **
Metadata tags for the volume.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

 ** Throughput **
Volume throughput performance.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** VolumeType **
Type of EBS volume.
Type: String
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
Required: No

## Response Elements
<a name="API_CreateVolume_ResponseElements"></a>

The following element is returned by the service.

 ** VolumeId **
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
HTTP Status Code: 403

 ** ConflictException **
Signals a conflict with the current state of the resource.
 ** Message **
Description of the conflict encountered.
 ** ResourceId **
Identifier of the conflicting resource.
 ** ResourceType **
Type of the conflicting resource.
HTTP Status Code: 409

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
HTTP Status Code: 402

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
HTTP Status Code: 429

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
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-instances-2022-07-26/CreateVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/CreateVolume)
