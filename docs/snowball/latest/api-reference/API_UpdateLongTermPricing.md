---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_UpdateLongTermPricing.html
---

# UpdateLongTermPricing
<a name="API_UpdateLongTermPricing"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Updates the long-term pricing type.

## Request Syntax
<a name="API_UpdateLongTermPricing_RequestSyntax"></a>

```
{
   "IsLongTermPricingAutoRenew": {{boolean}},
   "LongTermPricingId": "{{string}}",
   "ReplacementJob": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateLongTermPricing_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IsLongTermPricingAutoRenew](#API_UpdateLongTermPricing_RequestSyntax) **   <a name="Snowball-UpdateLongTermPricing-request-IsLongTermPricingAutoRenew"></a>
If set to `true`, specifies that the current long-term pricing type for the device should be automatically renewed before the long-term pricing contract expires.
Type: Boolean
Required: No

 ** [LongTermPricingId](#API_UpdateLongTermPricing_RequestSyntax) **   <a name="Snowball-UpdateLongTermPricing-request-LongTermPricingId"></a>
The ID of the long-term pricing type for the device.
Type: String
Length Constraints: Fixed length of 41.
Pattern: `LTPID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [ReplacementJob](#API_UpdateLongTermPricing_RequestSyntax) **   <a name="Snowball-UpdateLongTermPricing-request-ReplacementJob"></a>
Specifies that a device that is ordered with long-term pricing should be replaced with a new device.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `(M|J)ID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## Response Elements
<a name="API_UpdateLongTermPricing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLongTermPricing_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceException **
The specified resource can't be found. Check the information you provided in your last request, and try again.
 ** ResourceType **
The provided resource value is invalid.
HTTP Status Code: 400

## See Also
<a name="API_UpdateLongTermPricing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/UpdateLongTermPricing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/UpdateLongTermPricing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/UpdateLongTermPricing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/UpdateLongTermPricing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/UpdateLongTermPricing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/UpdateLongTermPricing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/UpdateLongTermPricing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/UpdateLongTermPricing)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/UpdateLongTermPricing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/UpdateLongTermPricing)
