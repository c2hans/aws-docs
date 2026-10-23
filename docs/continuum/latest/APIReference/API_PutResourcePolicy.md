---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_PutResourcePolicy.html
---

# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

Creates or replaces the resource policy attached to a Continuum resource.

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
PUT /resourcepolicy HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}",
   "expectedRevisionId": "{{string}}",
   "policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutResourcePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_PutResourcePolicy_RequestSyntax) **   <a name="continuum-PutResourcePolicy-request-arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:[a-z-]+/[a-z0-9]+(/[a-z-]+/[a-z0-9]+)*`
Required: Yes

 ** [expectedRevisionId](#API_PutResourcePolicy_RequestSyntax) **   <a name="continuum-PutResourcePolicy-request-expectedRevisionId"></a>
The identifier of the expected Revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [policy](#API_PutResourcePolicy_RequestSyntax) **   <a name="continuum-PutResourcePolicy-request-policy"></a>
The policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Required: No

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "policy": "string",
   "revisionId": "string"
}
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_PutResourcePolicy_ResponseSyntax) **   <a name="continuum-PutResourcePolicy-response-arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:[a-z-]+/[a-z0-9]+(/[a-z-]+/[a-z0-9]+)*`

 ** [policy](#API_PutResourcePolicy_ResponseSyntax) **   <a name="continuum-PutResourcePolicy-response-policy"></a>
The policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.

 ** [revisionId](#API_PutResourcePolicy_ResponseSyntax) **   <a name="continuum-PutResourcePolicy-response-revisionId"></a>
The identifier of the revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/PutResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/PutResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/PutResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/PutResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/PutResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/PutResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/PutResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/PutResourcePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/PutResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/PutResourcePolicy)
