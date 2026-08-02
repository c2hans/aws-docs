---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateOdbNetwork.html
---

# UpdateOdbNetwork
<a name="API_UpdateOdbNetwork"></a>

Updates properties of a specified ODB network.

## Request Syntax
<a name="API_UpdateOdbNetwork_RequestSyntax"></a>

```
{
   "crossRegionS3RestoreSourcesToDisable": [ "{{string}}" ],
   "crossRegionS3RestoreSourcesToEnable": [ "{{string}}" ],
   "displayName": "{{string}}",
   "kmsAccess": "{{string}}",
   "kmsPolicyDocument": "{{string}}",
   "odbNetworkId": "{{string}}",
   "peeredCidrsToBeAdded": [ "{{string}}" ],
   "peeredCidrsToBeRemoved": [ "{{string}}" ],
   "s3Access": "{{string}}",
   "s3PolicyDocument": "{{string}}",
   "stsAccess": "{{string}}",
   "stsPolicyDocument": "{{string}}",
   "zeroEtlAccess": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateOdbNetwork_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [crossRegionS3RestoreSourcesToDisable](#API_UpdateOdbNetwork_RequestSyntax) **   <a name="odb-UpdateOdbNetwork-request-crossRegionS3RestoreSourcesToDisable"></a>
The cross-Region Amazon S3 restore sources to disable for the ODB network.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** [crossRegionS3RestoreSourcesToEnable](#API_UpdateOdbNetwork_RequestSyntax) **   <a name="odb-UpdateOdbNetwork-request-crossRegionS3RestoreSourcesToEnable"></a>
The cross-Region Amazon S3 restore sources to enable for the ODB network.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** [displayName](#API_UpdateOdbNetwork_RequestSyntax) **   <a name="odb-UpdateOdbNetwork-request-displayName"></a>
The new user-friendly name of the ODB network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: No

 ** [kmsAccess](#API_UpdateOdbNetwork_RequestSyntax) **   <a name="odb-UpdateOdbNetwork-request-kmsAccess"></a>
The AWS Key Management Service (KMS) access configuration for the ODB network.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [kmsPolicyDocument](#API_UpdateOdbNetwork_RequestSyntax) **   <a name="odb-UpdateOdbNetwork-request-kmsPolicyDocument"></a>
The AWS Key Management Service (KMS) policy document that defines permissions for key usage within the ODB network.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 20480.
Required: No

 ** [odbNetworkId](#API_UpdateOdbNetwork_RequestSyntax) **   <a name="odb-UpdateOdbNetwork-request-odbNetworkId"></a>
The unique identifier of the ODB network to update.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [peeredCidrsToBeAdded](#API_UpdateOdbNetwork_RequestSyntax) **   <a name="odb-UpdateOdbNetwork-request-peeredCidrsToBeAdded"></a>
The list of CIDR ranges from the peered VPC that allow access to the ODB network.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** [peeredCidrsToBeRemoved](#API_UpdateOdbNetwork_RequestSyntax) **   <a name="odb-UpdateOdbNetwork-request-peeredCidrsToBeRemoved"></a>
The list of CIDR ranges from the peered VPC to remove from the ODB network.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** [s3Access](#API_UpdateOdbNetwork_RequestSyntax) **   <a name="odb-UpdateOdbNetwork-request-s3Access"></a>
Specifies the updated configuration for Amazon S3 access from the ODB network.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [s3PolicyDocument](#API_UpdateOdbNetwork_RequestSyntax) **   <a name="odb-UpdateOdbNetwork-request-s3PolicyDocument"></a>
Specifies the updated endpoint policy for Amazon S3 access from the ODB network.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 20480.
Required: No

 ** [stsAccess](#API_UpdateOdbNetwork_RequestSyntax) **   <a name="odb-UpdateOdbNetwork-request-stsAccess"></a>
The AWS Security Token Service (STS) access configuration for the ODB network.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [stsPolicyDocument](#API_UpdateOdbNetwork_RequestSyntax) **   <a name="odb-UpdateOdbNetwork-request-stsPolicyDocument"></a>
The AWS Security Token Service (STS) policy document that defines permissions for token service usage within the ODB network.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 20480.
Required: No

 ** [zeroEtlAccess](#API_UpdateOdbNetwork_RequestSyntax) **   <a name="odb-UpdateOdbNetwork-request-zeroEtlAccess"></a>
Specifies the updated configuration for Zero-ETL access from the ODB network.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## Response Syntax
<a name="API_UpdateOdbNetwork_ResponseSyntax"></a>

```
{
   "displayName": "string",
   "odbNetworkId": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_UpdateOdbNetwork_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [displayName](#API_UpdateOdbNetwork_ResponseSyntax) **   <a name="odb-UpdateOdbNetwork-response-displayName"></a>
The user-friendly name of the ODB network.
Type: String

 ** [odbNetworkId](#API_UpdateOdbNetwork_ResponseSyntax) **   <a name="odb-UpdateOdbNetwork-response-odbNetworkId"></a>
The unique identifier of the ODB network.
Type: String

 ** [status](#API_UpdateOdbNetwork_ResponseSyntax) **   <a name="odb-UpdateOdbNetwork-response-status"></a>
The current status of the ODB network.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_UpdateOdbNetwork_ResponseSyntax) **   <a name="odb-UpdateOdbNetwork-response-statusReason"></a>
Additional information about the status of the ODB network.
Type: String

## Errors
<a name="API_UpdateOdbNetwork_Errors"></a>

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
<a name="API_UpdateOdbNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/UpdateOdbNetwork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/UpdateOdbNetwork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/UpdateOdbNetwork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/UpdateOdbNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/UpdateOdbNetwork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/UpdateOdbNetwork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/UpdateOdbNetwork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/UpdateOdbNetwork)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/UpdateOdbNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/UpdateOdbNetwork)
