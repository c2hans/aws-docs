---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_DeleteSpendingLimit.html
---

# DeleteSpendingLimit
<a name="API_DeleteSpendingLimit"></a>

Deletes an existing spending limit. This operation permanently removes the spending limit and cannot be undone. After deletion, the associated device becomes unrestricted for spending.

## Request Syntax
<a name="API_DeleteSpendingLimit_RequestSyntax"></a>

```
DELETE /spending-limit/{{spendingLimitArn}}/delete HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteSpendingLimit_RequestParameters"></a>

The request uses the following URI parameters.

 ** [spendingLimitArn](#API_DeleteSpendingLimit_RequestSyntax) **   <a name="braket-DeleteSpendingLimit-request-uri-spendingLimitArn"></a>
The Amazon Resource Name (ARN) of the spending limit to delete.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:braket:[a-z0-9\-]+:[0-9]{12}:spending-limit/.*`
Required: Yes

## Request Body
<a name="API_DeleteSpendingLimit_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteSpendingLimit_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteSpendingLimit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteSpendingLimit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
The request failed because of an unknown error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The API throttling rate limit is exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input request failed to satisfy constraints expected by Amazon Braket.
 ** programSetValidationFailures **
The validation failures in the program set submitted in the request.
 ** reason **
The reason for validation failure.
HTTP Status Code: 400

## See Also
<a name="API_DeleteSpendingLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/braket-2019-09-01/DeleteSpendingLimit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/braket-2019-09-01/DeleteSpendingLimit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/DeleteSpendingLimit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/braket-2019-09-01/DeleteSpendingLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/DeleteSpendingLimit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/braket-2019-09-01/DeleteSpendingLimit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/braket-2019-09-01/DeleteSpendingLimit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/braket-2019-09-01/DeleteSpendingLimit)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/braket-2019-09-01/DeleteSpendingLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/DeleteSpendingLimit)
