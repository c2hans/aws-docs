---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_UpdateSpendingLimit.html
---

# UpdateSpendingLimit
<a name="API_UpdateSpendingLimit"></a>

Updates an existing spending limit. You can modify the spending amount or time period. Changes take effect immediately.

## Request Syntax
<a name="API_UpdateSpendingLimit_RequestSyntax"></a>

```
PATCH /spending-limit/{{spendingLimitArn}}/update HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "spendingLimit": "{{string}}",
   "timePeriod": {
      "endAt": {{number}},
      "startAt": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateSpendingLimit_RequestParameters"></a>

The request uses the following URI parameters.

 ** [spendingLimitArn](#API_UpdateSpendingLimit_RequestSyntax) **   <a name="braket-UpdateSpendingLimit-request-uri-spendingLimitArn"></a>
The Amazon Resource Name (ARN) of the spending limit to update.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:braket:[a-z0-9\-]+:[0-9]{12}:spending-limit/.*`
Required: Yes

## Request Body
<a name="API_UpdateSpendingLimit_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateSpendingLimit_RequestSyntax) **   <a name="braket-UpdateSpendingLimit-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Braket ignores the request, but does not return an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [spendingLimit](#API_UpdateSpendingLimit_RequestSyntax) **   <a name="braket-UpdateSpendingLimit-request-spendingLimit"></a>
The new maximum amount that can be spent on the specified device, in USD.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `\d+(\.\d{1,2})?`
Required: No

 ** [timePeriod](#API_UpdateSpendingLimit_RequestSyntax) **   <a name="braket-UpdateSpendingLimit-request-timePeriod"></a>
The new time period during which the spending limit is active, including start and end dates.
Type: [TimePeriod](API_TimePeriod.md) object
Required: No

## Response Syntax
<a name="API_UpdateSpendingLimit_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateSpendingLimit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateSpendingLimit_Errors"></a>

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
<a name="API_UpdateSpendingLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/braket-2019-09-01/UpdateSpendingLimit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/braket-2019-09-01/UpdateSpendingLimit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/UpdateSpendingLimit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/braket-2019-09-01/UpdateSpendingLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/UpdateSpendingLimit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/braket-2019-09-01/UpdateSpendingLimit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/braket-2019-09-01/UpdateSpendingLimit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/braket-2019-09-01/UpdateSpendingLimit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/braket-2019-09-01/UpdateSpendingLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/UpdateSpendingLimit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
