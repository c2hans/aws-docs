---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_UpdatePricingPlan.html
---

# UpdatePricingPlan
<a name="API_UpdatePricingPlan"></a>

Update the pricing plan.

## Request Syntax
<a name="API_UpdatePricingPlan_RequestSyntax"></a>

```
POST /pricingplan HTTP/1.1
Content-type: application/json

{
   "bundleNames": [ "{{string}}" ],
   "pricingMode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePricingPlan_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdatePricingPlan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [bundleNames](#API_UpdatePricingPlan_RequestSyntax) **   <a name="tm-UpdatePricingPlan-request-bundleNames"></a>
The bundle names.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

 ** [pricingMode](#API_UpdatePricingPlan_RequestSyntax) **   <a name="tm-UpdatePricingPlan-request-pricingMode"></a>
The pricing mode.
Type: String
Valid Values: `BASIC | STANDARD | TIERED_BUNDLE`
Required: Yes

## Response Syntax
<a name="API_UpdatePricingPlan_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "currentPricingPlan": {
      "billableEntityCount": number,
      "bundleInformation": {
         "bundleNames": [ "string" ],
         "pricingTier": "string"
      },
      "effectiveDateTime": number,
      "pricingMode": "string",
      "updateDateTime": number,
      "updateReason": "string"
   },
   "pendingPricingPlan": {
      "billableEntityCount": number,
      "bundleInformation": {
         "bundleNames": [ "string" ],
         "pricingTier": "string"
      },
      "effectiveDateTime": number,
      "pricingMode": "string",
      "updateDateTime": number,
      "updateReason": "string"
   }
}
```

## Response Elements
<a name="API_UpdatePricingPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [currentPricingPlan](#API_UpdatePricingPlan_ResponseSyntax) **   <a name="tm-UpdatePricingPlan-response-currentPricingPlan"></a>
Update the current pricing plan.
Type: [PricingPlan](API_PricingPlan.md) object

 ** [pendingPricingPlan](#API_UpdatePricingPlan_ResponseSyntax) **   <a name="tm-UpdatePricingPlan-response-pendingPricingPlan"></a>
Update the pending pricing plan.
Type: [PricingPlan](API_PricingPlan.md) object

## Errors
<a name="API_UpdatePricingPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_UpdatePricingPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/UpdatePricingPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/UpdatePricingPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/UpdatePricingPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/UpdatePricingPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/UpdatePricingPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/UpdatePricingPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/UpdatePricingPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/UpdatePricingPlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/UpdatePricingPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/UpdatePricingPlan)
