---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableBaseline.html
---

# EnableBaseline
<a name="API_EnableBaseline"></a>

Enable (apply) a `Baseline` to a Target. This API starts an asynchronous operation to deploy resources specified by the `Baseline` to the specified Target. For usage examples, see [https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html](https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html).

## Request Syntax
<a name="API_EnableBaseline_RequestSyntax"></a>

```
POST /enable-baseline HTTP/1.1
Content-type: application/json

{
   "baselineIdentifier": "{{string}}",
   "baselineVersion": "{{string}}",
   "parameters": [
      {
         "key": "{{string}}",
         "value": {{JSON value}}
      }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "targetIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_EnableBaseline_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_EnableBaseline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [baselineIdentifier](#API_EnableBaseline_RequestSyntax) **   <a name="controltower-EnableBaseline-request-baselineIdentifier"></a>
The ARN of the baseline to be enabled.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: Yes

 ** [baselineVersion](#API_EnableBaseline_RequestSyntax) **   <a name="controltower-EnableBaseline-request-baselineVersion"></a>
The specific version to be enabled of the specified baseline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `\d+(?:\.\d+){0,2}`
Required: Yes

 ** [parameters](#API_EnableBaseline_RequestSyntax) **   <a name="controltower-EnableBaseline-request-parameters"></a>
A list of `key-value` objects that specify enablement parameters, where `key` is a string and `value` is a document of any type.
Type: Array of [EnabledBaselineParameter](API_EnabledBaselineParameter.md) objects
Required: No

 ** [tags](#API_EnableBaseline_RequestSyntax) **   <a name="controltower-EnableBaseline-request-tags"></a>
Tags associated with input to `EnableBaseline`.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [targetIdentifier](#API_EnableBaseline_RequestSyntax) **   <a name="controltower-EnableBaseline-request-targetIdentifier"></a>
The ARN of the target on which the baseline will be enabled. Only OUs are supported as targets.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: Yes

## Response Syntax
<a name="API_EnableBaseline_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "operationIdentifier": "string"
}
```

## Response Elements
<a name="API_EnableBaseline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_EnableBaseline_ResponseSyntax) **   <a name="controltower-EnableBaseline-response-arn"></a>
The ARN of the `EnabledBaseline` resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`

 ** [operationIdentifier](#API_EnableBaseline_ResponseSyntax) **   <a name="controltower-EnableBaseline-response-operationIdentifier"></a>
The ID (in UUID format) of the asynchronous `EnableBaseline` operation. This `operationIdentifier` is used to track status through calls to the `GetBaselineOperation` API.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_EnableBaseline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting the resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during processing of a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded. See [Service quotas](https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html).
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_EnableBaseline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controltower-2018-05-10/EnableBaseline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/EnableBaseline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/EnableBaseline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controltower-2018-05-10/EnableBaseline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/EnableBaseline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controltower-2018-05-10/EnableBaseline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controltower-2018-05-10/EnableBaseline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controltower-2018-05-10/EnableBaseline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/EnableBaseline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/EnableBaseline)
