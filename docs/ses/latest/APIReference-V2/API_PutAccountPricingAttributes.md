---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutAccountPricingAttributes.html
---

# PutAccountPricingAttributes
<a name="API_PutAccountPricingAttributes"></a>

Set the pricing plan for your Amazon SES account.

## Request Syntax
<a name="API_PutAccountPricingAttributes_RequestSyntax"></a>

```
PUT /v2/email/account/pricing-attributes HTTP/1.1
Content-type: application/json

{
   "Plan": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutAccountPricingAttributes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutAccountPricingAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Plan](#API_PutAccountPricingAttributes_RequestSyntax) **   <a name="SES-PutAccountPricingAttributes-request-Plan"></a>
The pricing plan to apply to your Amazon SES account. For details about each plan, see [Amazon SES Pricing](http://aws.amazon.com/ses/pricing/). Can be one of the following:
+  `NONE`
+  `ESSENTIALS`
+  `PRO`
+  `ENTERPRISE`
Type: String
Valid Values: `NONE | ESSENTIALS | PRO | ENTERPRISE`
Required: Yes

## Response Syntax
<a name="API_PutAccountPricingAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutAccountPricingAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutAccountPricingAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** ConflictException **
If there is already an ongoing account details update under review.
HTTP Status Code: 409

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_PutAccountPricingAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutAccountPricingAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutAccountPricingAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutAccountPricingAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutAccountPricingAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutAccountPricingAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutAccountPricingAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutAccountPricingAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutAccountPricingAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutAccountPricingAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutAccountPricingAttributes)
