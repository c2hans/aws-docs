---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeSupportedLanguages.html
---

# DescribeSupportedLanguages
<a name="API_DescribeSupportedLanguages"></a>

Returns a list of supported languages for a specified `categoryCode`, `issueType` and `serviceCode`. The returned supported languages will include a ISO 639-1 code for the `language`, and the language display name.

**Note**
You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the AWS Support API.
If you call the AWS Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

## Request Syntax
<a name="API_DescribeSupportedLanguages_RequestSyntax"></a>

```
{
   "categoryCode": "{{string}}",
   "issueType": "{{string}}",
   "serviceCode": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSupportedLanguages_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [categoryCode](#API_DescribeSupportedLanguages_RequestSyntax) **   <a name="AWSSupport-DescribeSupportedLanguages-request-categoryCode"></a>
The category of problem for the support case. You also use the [DescribeServices](API_DescribeServices.md) operation to get the category code for a service. Each AWS service defines its own set of category codes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.

 ** [issueType](#API_DescribeSupportedLanguages_RequestSyntax) **   <a name="AWSSupport-DescribeSupportedLanguages-request-issueType"></a>
The type of issue for the case. You can specify `customer-service` or `technical`.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 22.

 ** [serviceCode](#API_DescribeSupportedLanguages_RequestSyntax) **   <a name="AWSSupport-DescribeSupportedLanguages-request-serviceCode"></a>
The code for the AWS service. You can use the [DescribeServices](API_DescribeServices.md) operation to get the possible `serviceCode` values.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.

## Response Syntax
<a name="API_DescribeSupportedLanguages_ResponseSyntax"></a>

```
{
   "supportedLanguages": [
      {
         "code": "string",
         "display": "string",
         "language": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSupportedLanguages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [supportedLanguages](#API_DescribeSupportedLanguages_ResponseSyntax) **   <a name="AWSSupport-DescribeSupportedLanguages-response-supportedLanguages"></a>
 A JSON-formatted array that contains the available ISO 639-1 language codes.
Type: Array of [SupportedLanguage](API_SupportedLanguage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_DescribeSupportedLanguages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An internal server error occurred.
 ** message **
An internal server error occurred.
HTTP Status Code: 500

 ** ThrottlingException **
 You have exceeded the maximum allowed TPS (Transactions Per Second) for the operations.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSupportedLanguages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/DescribeSupportedLanguages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/DescribeSupportedLanguages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/DescribeSupportedLanguages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/DescribeSupportedLanguages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/DescribeSupportedLanguages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/DescribeSupportedLanguages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/DescribeSupportedLanguages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/DescribeSupportedLanguages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/DescribeSupportedLanguages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/DescribeSupportedLanguages)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
