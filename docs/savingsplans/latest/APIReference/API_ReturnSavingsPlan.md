---
source_url: https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_ReturnSavingsPlan.html
---

# ReturnSavingsPlan
<a name="API_ReturnSavingsPlan"></a>

Returns the specified Savings Plan.

## Request Syntax
<a name="API_ReturnSavingsPlan_RequestSyntax"></a>

```
POST /ReturnSavingsPlan HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "savingsPlanId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ReturnSavingsPlan_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ReturnSavingsPlan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_ReturnSavingsPlan_RequestSyntax) **   <a name="savingsplans-ReturnSavingsPlan-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: No

 ** [savingsPlanId](#API_ReturnSavingsPlan_RequestSyntax) **   <a name="savingsplans-ReturnSavingsPlan-request-savingsPlanId"></a>
The ID of the Savings Plan.
Type: String
Required: Yes

## Response Syntax
<a name="API_ReturnSavingsPlan_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "savingsPlanId": "string"
}
```

## Response Elements
<a name="API_ReturnSavingsPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [savingsPlanId](#API_ReturnSavingsPlan_ResponseSyntax) **   <a name="savingsplans-ReturnSavingsPlan-response-savingsPlanId"></a>
The ID of the Savings Plan.
Type: String

## Errors
<a name="API_ReturnSavingsPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
A service quota has been exceeded.
HTTP Status Code: 402

 ** ValidationException **
One of the input parameters is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ReturnSavingsPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/savingsplans-2019-06-28/ReturnSavingsPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/savingsplans-2019-06-28/ReturnSavingsPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/savingsplans-2019-06-28/ReturnSavingsPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/savingsplans-2019-06-28/ReturnSavingsPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/savingsplans-2019-06-28/ReturnSavingsPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/savingsplans-2019-06-28/ReturnSavingsPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/savingsplans-2019-06-28/ReturnSavingsPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/savingsplans-2019-06-28/ReturnSavingsPlan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/savingsplans-2019-06-28/ReturnSavingsPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/savingsplans-2019-06-28/ReturnSavingsPlan)
