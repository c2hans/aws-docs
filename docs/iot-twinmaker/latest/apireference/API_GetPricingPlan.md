---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetPricingPlan.html
---

# GetPricingPlan
<a name="API_GetPricingPlan"></a>

Gets the pricing plan.

## Request Syntax
<a name="API_GetPricingPlan_RequestSyntax"></a>

```
GET /pricingplan HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPricingPlan_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetPricingPlan_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPricingPlan_ResponseSyntax"></a>

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
<a name="API_GetPricingPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [currentPricingPlan](#API_GetPricingPlan_ResponseSyntax) **   <a name="tm-GetPricingPlan-response-currentPricingPlan"></a>
The chosen pricing plan for the current billing cycle.
Type: [PricingPlan](API_PricingPlan.md) object

 ** [pendingPricingPlan](#API_GetPricingPlan_ResponseSyntax) **   <a name="tm-GetPricingPlan-response-pendingPricingPlan"></a>
The pending pricing plan.
Type: [PricingPlan](API_PricingPlan.md) object

## Errors
<a name="API_GetPricingPlan_Errors"></a>

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
<a name="API_GetPricingPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/GetPricingPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/GetPricingPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/GetPricingPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/GetPricingPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/GetPricingPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/GetPricingPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/GetPricingPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/GetPricingPlan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/GetPricingPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/GetPricingPlan)
