---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateFailoverSlateConfiguration.html
---

# CreateFailoverSlateConfiguration
<a name="API_CreateFailoverSlateConfiguration"></a>

Creates a new failover slate configuration.

## Request Syntax
<a name="API_CreateFailoverSlateConfiguration_RequestSyntax"></a>

```
POST /CreateFailoverSlateConfiguration HTTP/1.1
Content-type: application/json

{
   "activationThresholdSeconds": {{number}},
   "maxSlateDisplaySeconds": {{number}},
   "minSlateDisplaySeconds": {{number}},
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateFailoverSlateConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateFailoverSlateConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [activationThresholdSeconds](#API_CreateFailoverSlateConfiguration_RequestSyntax) **   <a name="ivs-CreateFailoverSlateConfiguration-request-activationThresholdSeconds"></a>
Number of seconds of ingest interruption before the failover slate activates. Default: `3`.
Type: Integer
Valid Range: Minimum value of 3. Maximum value of 5.
Required: No

 ** [maxSlateDisplaySeconds](#API_CreateFailoverSlateConfiguration_RequestSyntax) **   <a name="ivs-CreateFailoverSlateConfiguration-request-maxSlateDisplaySeconds"></a>
Maximum number of seconds that the failover slate displays. Default: `60`.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 180.
Required: No

 ** [minSlateDisplaySeconds](#API_CreateFailoverSlateConfiguration_RequestSyntax) **   <a name="ivs-CreateFailoverSlateConfiguration-request-minSlateDisplaySeconds"></a>
Minimum number of seconds that the failover slate displays after activation. Default: `3`.
Type: Integer
Valid Range: Minimum value of 3. Maximum value of 10.
Required: No

 ** [name](#API_CreateFailoverSlateConfiguration_RequestSyntax) **   <a name="ivs-CreateFailoverSlateConfiguration-request-name"></a>
Failover-slate-configuration name. The value does not need to be unique.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** [tags](#API_CreateFailoverSlateConfiguration_RequestSyntax) **   <a name="ivs-CreateFailoverSlateConfiguration-request-tags"></a>
Array of 1-50 maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_CreateFailoverSlateConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failoverSlateConfiguration": {
      "activationThresholdSeconds": number,
      "arn": "string",
      "maxSlateDisplaySeconds": number,
      "minSlateDisplaySeconds": number,
      "name": "string",
      "state": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateFailoverSlateConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failoverSlateConfiguration](#API_CreateFailoverSlateConfiguration_ResponseSyntax) **   <a name="ivs-CreateFailoverSlateConfiguration-response-failoverSlateConfiguration"></a>
The failover slate configuration that was created.
Type: [FailoverSlateConfiguration](API_FailoverSlateConfiguration.md) object

## Errors
<a name="API_CreateFailoverSlateConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateFailoverSlateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/CreateFailoverSlateConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/CreateFailoverSlateConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/CreateFailoverSlateConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/CreateFailoverSlateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/CreateFailoverSlateConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/CreateFailoverSlateConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/CreateFailoverSlateConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/CreateFailoverSlateConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/CreateFailoverSlateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/CreateFailoverSlateConfiguration)
