---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListEncoderConfigurations.html
---

# ListEncoderConfigurations
<a name="API_ListEncoderConfigurations"></a>

Gets summary information about all EncoderConfigurations in your account, in the AWS region where the API request is processed.

## Request Syntax
<a name="API_ListEncoderConfigurations_RequestSyntax"></a>

```
POST /ListEncoderConfigurations HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListEncoderConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListEncoderConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListEncoderConfigurations_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListEncoderConfigurations-request-maxResults"></a>
Maximum number of results to return. Default: 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListEncoderConfigurations_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListEncoderConfigurations-request-nextToken"></a>
The first encoder configuration to retrieve. This is used for pagination; see the `nextToken` response field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`
Required: No

## Response Syntax
<a name="API_ListEncoderConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "encoderConfigurations": [
      {
         "arn": "string",
         "name": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEncoderConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [encoderConfigurations](#API_ListEncoderConfigurations_ResponseSyntax) **   <a name="ivsrealtimeeapireference-ListEncoderConfigurations-response-encoderConfigurations"></a>
List of the matching EncoderConfigurations (summary information only).
Type: Array of [EncoderConfigurationSummary](API_EncoderConfigurationSummary.md) objects

 ** [nextToken](#API_ListEncoderConfigurations_ResponseSyntax) **   <a name="ivsrealtimeeapireference-ListEncoderConfigurations-response-nextToken"></a>
If there are more encoder configurations than `maxResults`, use `nextToken` in the request to get the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`

## Errors
<a name="API_ListEncoderConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** exceptionMessage **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **

 ** exceptionMessage **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **

 ** exceptionMessage **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **

 ** exceptionMessage **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ValidationException **

 ** exceptionMessage **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListEncoderConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/ListEncoderConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/ListEncoderConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/ListEncoderConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/ListEncoderConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/ListEncoderConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/ListEncoderConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/ListEncoderConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/ListEncoderConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/ListEncoderConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/ListEncoderConfigurations)
