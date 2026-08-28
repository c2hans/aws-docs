---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_CreateSpendingLimit.html
---

# CreateSpendingLimit
<a name="API_CreateSpendingLimit"></a>

Creates a spending limit for a specified quantum device. Spending limits help you control costs by setting maximum amounts that can be spent on quantum computing tasks within a specified time period. Simulators do not support spending limits.

## Request Syntax
<a name="API_CreateSpendingLimit_RequestSyntax"></a>

```
POST /spending-limit HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "deviceArn": "{{string}}",
   "spendingLimit": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "timePeriod": {
      "endAt": {{number}},
      "startAt": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_CreateSpendingLimit_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSpendingLimit_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateSpendingLimit_RequestSyntax) **   <a name="braket-CreateSpendingLimit-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Braket ignores the request, but does not return an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [deviceArn](#API_CreateSpendingLimit_RequestSyntax) **   <a name="braket-CreateSpendingLimit-request-deviceArn"></a>
The Amazon Resource Name (ARN) of the quantum device to apply the spending limit to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [spendingLimit](#API_CreateSpendingLimit_RequestSyntax) **   <a name="braket-CreateSpendingLimit-request-spendingLimit"></a>
The maximum amount that can be spent on the specified device, in USD.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `\d+(\.\d{1,2})?`
Required: Yes

 ** [tags](#API_CreateSpendingLimit_RequestSyntax) **   <a name="braket-CreateSpendingLimit-request-tags"></a>
The tags to apply to the spending limit. Each tag consists of a key and an optional value.
Type: String to string map
Required: No

 ** [timePeriod](#API_CreateSpendingLimit_RequestSyntax) **   <a name="braket-CreateSpendingLimit-request-timePeriod"></a>
The time period during which the spending limit is active, including start and end dates.
Type: [TimePeriod](API_TimePeriod.md) object
Required: No

## Response Syntax
<a name="API_CreateSpendingLimit_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "spendingLimitArn": "string"
}
```

## Response Elements
<a name="API_CreateSpendingLimit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [spendingLimitArn](#API_CreateSpendingLimit_ResponseSyntax) **   <a name="braket-CreateSpendingLimit-response-spendingLimitArn"></a>
The Amazon Resource Name (ARN) of the created spending limit.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:braket:[a-z0-9\-]+:[0-9]{12}:spending-limit/.*`

## Errors
<a name="API_CreateSpendingLimit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** DeviceRetiredException **
The specified device has been retired.
HTTP Status Code: 410

 ** InternalServiceException **
The request failed because of an unknown error.
HTTP Status Code: 500

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
<a name="API_CreateSpendingLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/braket-2019-09-01/CreateSpendingLimit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/braket-2019-09-01/CreateSpendingLimit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/CreateSpendingLimit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/braket-2019-09-01/CreateSpendingLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/CreateSpendingLimit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/braket-2019-09-01/CreateSpendingLimit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/braket-2019-09-01/CreateSpendingLimit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/braket-2019-09-01/CreateSpendingLimit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/braket-2019-09-01/CreateSpendingLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/CreateSpendingLimit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
