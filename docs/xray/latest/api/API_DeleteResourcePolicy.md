---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_DeleteResourcePolicy.html
---

# DeleteResourcePolicy
<a name="API_DeleteResourcePolicy"></a>

Deletes a resource policy from the target AWS account.

## Request Syntax
<a name="API_DeleteResourcePolicy_RequestSyntax"></a>

```
POST /DeleteResourcePolicy HTTP/1.1
Content-type: application/json

{
   "PolicyName": "{{string}}",
   "PolicyRevisionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteResourcePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteResourcePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PolicyName](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="xray-DeleteResourcePolicy-request-PolicyName"></a>
The name of the resource policy to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** [PolicyRevisionId](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="xray-DeleteResourcePolicy-request-PolicyRevisionId"></a>
Specifies a specific policy revision to delete. Provide a `PolicyRevisionId` to ensure an atomic delete operation. If the provided revision id does not match the latest policy revision id, an `InvalidPolicyRevisionIdException` exception is returned.
Type: String
Required: No

## Response Syntax
<a name="API_DeleteResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidPolicyRevisionIdException **
A policy revision id was provided which does not match the latest policy revision. This exception is also if a policy revision id of 0 is provided via `PutResourcePolicy` and a policy with the same name already exists.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_DeleteResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/DeleteResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/DeleteResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/DeleteResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/DeleteResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/DeleteResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/DeleteResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/DeleteResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/DeleteResourcePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/DeleteResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/DeleteResourcePolicy)
