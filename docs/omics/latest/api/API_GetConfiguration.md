---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetConfiguration.html
---

# GetConfiguration
<a name="API_GetConfiguration"></a>

Retrieve configuration details for specified name.

## Request Syntax
<a name="API_GetConfiguration_RequestSyntax"></a>

```
GET /configuration/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_GetConfiguration_RequestSyntax) **   <a name="omics-GetConfiguration-request-uri-name"></a>
Configuration name to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`
Required: Yes

## Request Body
<a name="API_GetConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetConfiguration_ResponseSyntax) **   <a name="omics-GetConfiguration-response-arn"></a>
Unique resource identifier for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 190.
Pattern: `arn:.+`

 ** [creationTime](#API_GetConfiguration_ResponseSyntax) **   <a name="omics-GetConfiguration-response-creationTime"></a>
Configuration creation timestamp.
Type: Timestamp

 ** [description](#API_GetConfiguration_ResponseSyntax) **   <a name="omics-GetConfiguration-response-description"></a>
Description for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [name](#API_GetConfiguration_ResponseSyntax) **   <a name="omics-GetConfiguration-response-name"></a>
User-friendly name for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`

 ** [runConfigurations](#API_GetConfiguration_ResponseSyntax) **   <a name="omics-GetConfiguration-response-runConfigurations"></a>
Run-specific configurations.
Type: [RunConfigurationsResponse](API_RunConfigurationsResponse.md) object

 ** [status](#API_GetConfiguration_ResponseSyntax) **   <a name="omics-GetConfiguration-response-status"></a>
Current configuration status.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | DELETED | FAILED`

 ** [tags](#API_GetConfiguration_ResponseSyntax) **   <a name="omics-GetConfiguration-response-tags"></a>
Tags for the configuration.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [uuid](#API_GetConfiguration_ResponseSyntax) **   <a name="omics-GetConfiguration-response-uuid"></a>
Unique identifier for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_GetConfiguration_Errors"></a>

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
<a name="API_GetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
