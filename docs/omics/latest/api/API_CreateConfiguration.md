---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_CreateConfiguration.html
---

# CreateConfiguration
<a name="API_CreateConfiguration"></a>

Create a new configuration.

## Request Syntax
<a name="API_CreateConfiguration_RequestSyntax"></a>

```
POST /configuration HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}",
   "requestId": "{{string}}",
   "runConfigurations": {
      "vpcConfig": {
         "securityGroupIds": [ "{{string}}" ],
         "subnetIds": [ "{{string}}" ]
      }
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateConfiguration_RequestSyntax) **   <a name="omics-CreateConfiguration-request-description"></a>
Optional description for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [name](#API_CreateConfiguration_RequestSyntax) **   <a name="omics-CreateConfiguration-request-name"></a>
User-friendly name for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`
Required: Yes

 ** [requestId](#API_CreateConfiguration_RequestSyntax) **   <a name="omics-CreateConfiguration-request-requestId"></a>
Optional request idempotency token. If not specified, a universally unique identifier (UUID) will be automatically generated for the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** [runConfigurations](#API_CreateConfiguration_RequestSyntax) **   <a name="omics-CreateConfiguration-request-runConfigurations"></a>
Required run-specific configurations.
Type: [RunConfigurations](API_RunConfigurations.md) object
Required: Yes

 ** [tags](#API_CreateConfiguration_RequestSyntax) **   <a name="omics-CreateConfiguration-request-tags"></a>
Optional tags for the configuration.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "creationTime": "string",
   "description": "string",
   "name": "string",
   "runConfigurations": {
      "vpcConfig": {
         "securityGroupIds": [ "string" ],
         "subnetIds": [ "string" ],
         "vpcId": "string"
      }
   },
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "uuid": "string"
}
```

## Response Elements
<a name="API_CreateConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateConfiguration_ResponseSyntax) **   <a name="omics-CreateConfiguration-response-arn"></a>
Unique resource identifier for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 190.
Pattern: `arn:.+`

 ** [creationTime](#API_CreateConfiguration_ResponseSyntax) **   <a name="omics-CreateConfiguration-response-creationTime"></a>
Configuration creation timestamp.
Type: Timestamp

 ** [description](#API_CreateConfiguration_ResponseSyntax) **   <a name="omics-CreateConfiguration-response-description"></a>
Description for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [name](#API_CreateConfiguration_ResponseSyntax) **   <a name="omics-CreateConfiguration-response-name"></a>
User-friendly name for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`

 ** [runConfigurations](#API_CreateConfiguration_ResponseSyntax) **   <a name="omics-CreateConfiguration-response-runConfigurations"></a>
Run-specific configurations.
Type: [RunConfigurationsResponse](API_RunConfigurationsResponse.md) object

 ** [status](#API_CreateConfiguration_ResponseSyntax) **   <a name="omics-CreateConfiguration-response-status"></a>
Current configuration status.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | DELETED | FAILED`

 ** [tags](#API_CreateConfiguration_ResponseSyntax) **   <a name="omics-CreateConfiguration-response-tags"></a>
Tags for the configuration.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [uuid](#API_CreateConfiguration_ResponseSyntax) **   <a name="omics-CreateConfiguration-response-uuid"></a>
Unique identifier for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_CreateConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/CreateConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/CreateConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/CreateConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/CreateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/CreateConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/CreateConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/CreateConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/CreateConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/CreateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/CreateConfiguration)
