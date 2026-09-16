---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_DisassociateMember.html
---

# DisassociateMember
<a name="API_DisassociateMember"></a>

Disassociates a member account from an Amazon Inspector delegated administrator.

## Request Syntax
<a name="API_DisassociateMember_RequestSyntax"></a>

```
POST /members/disassociate HTTP/1.1
Content-type: application/json

{
   "accountId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DisassociateMember_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DisassociateMember_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountId](#API_DisassociateMember_RequestSyntax) **   <a name="inspector2-DisassociateMember-request-accountId"></a>
The AWS account ID of the member account to disassociate.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

## Response Syntax
<a name="API_DisassociateMember_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accountId": "string"
}
```

## Response Elements
<a name="API_DisassociateMember_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountId](#API_DisassociateMember_ResponseSyntax) **   <a name="inspector2-DisassociateMember-response-accountId"></a>
The AWS account ID of the successfully disassociated member.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

## Errors
<a name="API_DisassociateMember_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/DisassociateMember)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/DisassociateMember)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/DisassociateMember)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/DisassociateMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/DisassociateMember)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/DisassociateMember)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/DisassociateMember)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/DisassociateMember)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/DisassociateMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/DisassociateMember)
