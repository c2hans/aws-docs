---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_CreateLongTermPricing.html
---

# CreateLongTermPricing
<a name="API_CreateLongTermPricing"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Creates a job with the long-term usage option for a device. The long-term usage is a 1-year or 3-year long-term pricing type for the device. You are billed upfront, and AWS provides discounts for long-term pricing.

## Request Syntax
<a name="API_CreateLongTermPricing_RequestSyntax"></a>

```
{
   "IsLongTermPricingAutoRenew": {{boolean}},
   "LongTermPricingType": "{{string}}",
   "SnowballType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateLongTermPricing_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IsLongTermPricingAutoRenew](#API_CreateLongTermPricing_RequestSyntax) **   <a name="Snowball-CreateLongTermPricing-request-IsLongTermPricingAutoRenew"></a>
Specifies whether the current long-term pricing type for the device should be renewed.
Type: Boolean
Required: No

 ** [LongTermPricingType](#API_CreateLongTermPricing_RequestSyntax) **   <a name="Snowball-CreateLongTermPricing-request-LongTermPricingType"></a>
The type of long-term pricing option you want for the device, either 1-year or 3-year long-term pricing.
Type: String
Valid Values: `OneYear | ThreeYear | OneMonth`
Required: Yes

 ** [SnowballType](#API_CreateLongTermPricing_RequestSyntax) **   <a name="Snowball-CreateLongTermPricing-request-SnowballType"></a>
The type of Snow Family devices to use for the long-term pricing job.
Type: String
Valid Values: `STANDARD | EDGE | EDGE_C | EDGE_CG | EDGE_S | SNC1_HDD | SNC1_SSD | V3_5C | V3_5S | RACK_5U_C`
Required: Yes

## Response Syntax
<a name="API_CreateLongTermPricing_ResponseSyntax"></a>

```
{
   "LongTermPricingId": "string"
}
```

## Response Elements
<a name="API_CreateLongTermPricing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LongTermPricingId](#API_CreateLongTermPricing_ResponseSyntax) **   <a name="Snowball-CreateLongTermPricing-response-LongTermPricingId"></a>
The ID of the long-term pricing type for the device.
Type: String
Length Constraints: Fixed length of 41.
Pattern: `LTPID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Errors
<a name="API_CreateLongTermPricing_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceException **
The specified resource can't be found. Check the information you provided in your last request, and try again.
 ** ResourceType **
The provided resource value is invalid.
HTTP Status Code: 400

## See Also
<a name="API_CreateLongTermPricing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/CreateLongTermPricing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/CreateLongTermPricing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/CreateLongTermPricing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/CreateLongTermPricing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/CreateLongTermPricing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/CreateLongTermPricing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/CreateLongTermPricing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/CreateLongTermPricing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/CreateLongTermPricing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/CreateLongTermPricing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
