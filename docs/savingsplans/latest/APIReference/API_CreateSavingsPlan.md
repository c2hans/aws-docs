---
source_url: https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_CreateSavingsPlan.html
---

# CreateSavingsPlan
<a name="API_CreateSavingsPlan"></a>

Creates a Savings Plan.

## Request Syntax
<a name="API_CreateSavingsPlan_RequestSyntax"></a>

```
POST /CreateSavingsPlan HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "commitment": "{{string}}",
   "purchaseTime": {{number}},
   "savingsPlanOfferingId": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "upfrontPaymentAmount": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateSavingsPlan_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSavingsPlan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateSavingsPlan_RequestSyntax) **   <a name="savingsplans-CreateSavingsPlan-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: No

 ** [commitment](#API_CreateSavingsPlan_RequestSyntax) **   <a name="savingsplans-CreateSavingsPlan-request-commitment"></a>
The hourly commitment, in the same currency of the `savingsPlanOfferingId`. This is a value between 0.001 and 1 million. You cannot specify more than five digits after the decimal point.
Type: String
Required: Yes

 ** [purchaseTime](#API_CreateSavingsPlan_RequestSyntax) **   <a name="savingsplans-CreateSavingsPlan-request-purchaseTime"></a>
The purchase time of the Savings Plan in UTC format (YYYY-MM-DDTHH:MM:SSZ).
Type: Timestamp
Required: No

 ** [savingsPlanOfferingId](#API_CreateSavingsPlan_RequestSyntax) **   <a name="savingsplans-CreateSavingsPlan-request-savingsPlanOfferingId"></a>
The ID of the offering.
Type: String
Required: Yes

 ** [tags](#API_CreateSavingsPlan_RequestSyntax) **   <a name="savingsplans-CreateSavingsPlan-request-tags"></a>
One or more tags.
Type: String to string map
Required: No

 ** [upfrontPaymentAmount](#API_CreateSavingsPlan_RequestSyntax) **   <a name="savingsplans-CreateSavingsPlan-request-upfrontPaymentAmount"></a>
The up-front payment amount. This is a whole number between 50 and 99 percent of the total value of the Savings Plan. This parameter is only supported if the payment option is `Partial Upfront`.
Type: String
Required: No

## Response Syntax
<a name="API_CreateSavingsPlan_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "savingsPlanId": "string"
}
```

## Response Elements
<a name="API_CreateSavingsPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [savingsPlanId](#API_CreateSavingsPlan_ResponseSyntax) **   <a name="savingsplans-CreateSavingsPlan-response-savingsPlanId"></a>
The ID of the Savings Plan.
Type: String

## Errors
<a name="API_CreateSavingsPlan_Errors"></a>

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
<a name="API_CreateSavingsPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/savingsplans-2019-06-28/CreateSavingsPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/savingsplans-2019-06-28/CreateSavingsPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/savingsplans-2019-06-28/CreateSavingsPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/savingsplans-2019-06-28/CreateSavingsPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/savingsplans-2019-06-28/CreateSavingsPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/savingsplans-2019-06-28/CreateSavingsPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/savingsplans-2019-06-28/CreateSavingsPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/savingsplans-2019-06-28/CreateSavingsPlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/savingsplans-2019-06-28/CreateSavingsPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/savingsplans-2019-06-28/CreateSavingsPlan)
