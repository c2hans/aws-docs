---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListLongTermPricing.html
---

# ListLongTermPricing
<a name="API_ListLongTermPricing"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Lists all long-term pricing types.

## Request Syntax
<a name="API_ListLongTermPricing_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListLongTermPricing_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListLongTermPricing_RequestSyntax) **   <a name="Snowball-ListLongTermPricing-request-MaxResults"></a>
The maximum number of `ListLongTermPricing` objects to return.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListLongTermPricing_RequestSyntax) **   <a name="Snowball-ListLongTermPricing-request-NextToken"></a>
Because HTTP requests are stateless, this is the starting point for your next list of `ListLongTermPricing` to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListLongTermPricing_ResponseSyntax"></a>

```
{
   "LongTermPricingEntries": [
      {
         "CurrentActiveJob": "string",
         "IsLongTermPricingAutoRenew": boolean,
         "JobIds": [ "string" ],
         "LongTermPricingEndDate": number,
         "LongTermPricingId": "string",
         "LongTermPricingStartDate": number,
         "LongTermPricingStatus": "string",
         "LongTermPricingType": "string",
         "ReplacementJob": "string",
         "SnowballType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLongTermPricing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LongTermPricingEntries](#API_ListLongTermPricing_ResponseSyntax) **   <a name="Snowball-ListLongTermPricing-response-LongTermPricingEntries"></a>
Each `LongTermPricingEntry` object contains a status, ID, and other information about the `LongTermPricing` type.
Type: Array of [LongTermPricingListEntry](API_LongTermPricingListEntry.md) objects

 ** [NextToken](#API_ListLongTermPricing_ResponseSyntax) **   <a name="Snowball-ListLongTermPricing-response-NextToken"></a>
Because HTTP requests are stateless, this is the starting point for your next list of returned `ListLongTermPricing` list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

## Errors
<a name="API_ListLongTermPricing_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The `NextToken` string was altered unexpectedly, and the operation has stopped. Run the operation without changing the `NextToken` string, and try again.
HTTP Status Code: 400

 ** InvalidResourceException **
The specified resource can't be found. Check the information you provided in your last request, and try again.
 ** ResourceType **
The provided resource value is invalid.
HTTP Status Code: 400

## See Also
<a name="API_ListLongTermPricing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/ListLongTermPricing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/ListLongTermPricing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/ListLongTermPricing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/ListLongTermPricing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/ListLongTermPricing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/ListLongTermPricing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/ListLongTermPricing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/ListLongTermPricing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/ListLongTermPricing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/ListLongTermPricing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
