---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateExascaleDbStorageVault.html
---

# CreateExascaleDbStorageVault
<a name="API_CreateExascaleDbStorageVault"></a>

Creates an Exascale storage vault.

To create the Exascale storage vault on dedicated Exadata infrastructure, specify `cloudExadataInfrastructureId`.

## Request Syntax
<a name="API_CreateExascaleDbStorageVault_RequestSyntax"></a>

```
{
   "additionalFlashCacheInPercent": {{number}},
   "autoscaleLimitInGBs": {{number}},
   "availabilityZone": "{{string}}",
   "availabilityZoneId": "{{string}}",
   "clientToken": "{{string}}",
   "cloudExadataInfrastructureId": "{{string}}",
   "description": "{{string}}",
   "displayName": "{{string}}",
   "highCapacityDatabaseStorageTotalSizeInGBs": {{number}},
   "isAutoscaleEnabled": {{boolean}},
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "timeZone": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateExascaleDbStorageVault_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [additionalFlashCacheInPercent](#API_CreateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-CreateExascaleDbStorageVault-request-additionalFlashCacheInPercent"></a>
The additional flash cache percentage for the Exascale storage vault.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [autoscaleLimitInGBs](#API_CreateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-CreateExascaleDbStorageVault-request-autoscaleLimitInGBs"></a>
The autoscale limit in gigabytes (GB) for the Exascale storage vault.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [availabilityZone](#API_CreateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-CreateExascaleDbStorageVault-request-availabilityZone"></a>
The Availability Zone for the Exascale storage vault.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [availabilityZoneId](#API_CreateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-CreateExascaleDbStorageVault-request-availabilityZoneId"></a>
The Availability Zone ID for the Exascale storage vault.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [clientToken](#API_CreateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-CreateExascaleDbStorageVault-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you submit the same request twice with the same client token, the service ignores the second request and returns the result of the first. If you don't specify a client token, the AWS SDK automatically generates one. The client token is valid for up to 24 hours after it's first used.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `[a-zA-Z0-9_\/.=-]+`
Required: No

 ** [cloudExadataInfrastructureId](#API_CreateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-CreateExascaleDbStorageVault-request-cloudExadataInfrastructureId"></a>
The unique identifier or Amazon Resource Name (ARN) of the Exadata infrastructure on which to create the Exascale storage vault. Specify this value to create the Exascale storage vault on dedicated Exadata infrastructure that has Exascale storage configured. If you specify `availabilityZone` or `availabilityZoneId`, the value must match the Availability Zone of the Exadata infrastructure. If you specify neither, the service uses the Availability Zone of the Exadata infrastructure.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: No

 ** [description](#API_CreateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-CreateExascaleDbStorageVault-request-description"></a>
A description of the Exascale storage vault.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: No

 ** [displayName](#API_CreateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-CreateExascaleDbStorageVault-request-displayName"></a>
A user-friendly name for the Exascale storage vault.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: Yes

 ** [highCapacityDatabaseStorageTotalSizeInGBs](#API_CreateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-CreateExascaleDbStorageVault-request-highCapacityDatabaseStorageTotalSizeInGBs"></a>
The total size of the high-capacity database storage, in gigabytes (GB), for the Exascale storage vault.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** [isAutoscaleEnabled](#API_CreateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-CreateExascaleDbStorageVault-request-isAutoscaleEnabled"></a>
Specifies whether autoscaling is enabled for the Exascale storage vault.
Type: Boolean
Required: No

 ** [tags](#API_CreateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-CreateExascaleDbStorageVault-request-tags"></a>
The list of resource tags to apply to the Exascale storage vault.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [timeZone](#API_CreateExascaleDbStorageVault_RequestSyntax) **   <a name="odb-CreateExascaleDbStorageVault-request-timeZone"></a>
The time zone for the Exascale storage vault.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## Response Syntax
<a name="API_CreateExascaleDbStorageVault_ResponseSyntax"></a>

```
{
   "displayName": "string",
   "exascaleDbStorageVaultId": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_CreateExascaleDbStorageVault_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [displayName](#API_CreateExascaleDbStorageVault_ResponseSyntax) **   <a name="odb-CreateExascaleDbStorageVault-response-displayName"></a>
The user-friendly name for the Exascale storage vault.
Type: String

 ** [exascaleDbStorageVaultId](#API_CreateExascaleDbStorageVault_ResponseSyntax) **   <a name="odb-CreateExascaleDbStorageVault-response-exascaleDbStorageVaultId"></a>
The unique identifier of the Exascale storage vault.
Type: String

 ** [status](#API_CreateExascaleDbStorageVault_ResponseSyntax) **   <a name="odb-CreateExascaleDbStorageVault-response-status"></a>
The current status of the Exascale storage vault.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_CreateExascaleDbStorageVault_ResponseSyntax) **   <a name="odb-CreateExascaleDbStorageVault-response-statusReason"></a>
Additional information about the status of the Exascale storage vault.
Type: String

## Errors
<a name="API_CreateExascaleDbStorageVault_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of resource that caused the conflict.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of resource that was not found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
You have exceeded the service quota.
 ** quotaCode **
The unqiue identifier of the service quota that was exceeded.
 ** resourceId **
The identifier of the resource that exceeded the service quota.
 ** resourceType **
The type of resource that exceeded the service quota.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_CreateExascaleDbStorageVault_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/CreateExascaleDbStorageVault)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/CreateExascaleDbStorageVault)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CreateExascaleDbStorageVault)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/CreateExascaleDbStorageVault)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CreateExascaleDbStorageVault)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/CreateExascaleDbStorageVault)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/CreateExascaleDbStorageVault)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/CreateExascaleDbStorageVault)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/CreateExascaleDbStorageVault)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CreateExascaleDbStorageVault)
