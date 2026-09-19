---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StopComposition.html
---

# StopComposition
<a name="API_StopComposition"></a>

Stops and deletes a Composition resource. Any broadcast from the Composition resource is stopped.

## Request Syntax
<a name="API_StopComposition_RequestSyntax"></a>

```
POST /StopComposition HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StopComposition_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StopComposition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_StopComposition_RequestSyntax) **   <a name="ivsrealtimeeapireference-StopComposition-request-arn"></a>
ARN of the Composition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:composition/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_StopComposition_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StopComposition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopComposition_Errors"></a>

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

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StopComposition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/StopComposition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/StopComposition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/StopComposition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/StopComposition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/StopComposition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/StopComposition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/StopComposition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/StopComposition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/StopComposition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/StopComposition)
