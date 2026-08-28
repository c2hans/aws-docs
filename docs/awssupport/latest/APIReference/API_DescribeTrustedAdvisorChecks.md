---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorChecks.html
---

# DescribeTrustedAdvisorChecks
<a name="API_DescribeTrustedAdvisorChecks"></a>

Returns information about all available AWS Trusted Advisor checks, including the name, ID, category, description, and metadata. You must specify a language code.

The response contains a [TrustedAdvisorCheckDescription](API_TrustedAdvisorCheckDescription.md) object for each check. You must set the AWS Region to us-east-1.

**Note**
You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the AWS Support API.
If you call the AWS Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).
The names and descriptions for Trusted Advisor checks are subject to change. We recommend that you specify the check ID in your code to uniquely identify a check.

To call the AWS Trusted Advisor operations in the AWS Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don't support the Trusted Advisor operations. For more information, see [About the AWS Support API](https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint) in the * AWS Support User Guide*.

## Request Syntax
<a name="API_DescribeTrustedAdvisorChecks_RequestSyntax"></a>

```
{
   "language": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTrustedAdvisorChecks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [language](#API_DescribeTrustedAdvisorChecks_RequestSyntax) **   <a name="AWSSupport-DescribeTrustedAdvisorChecks-request-language"></a>
The ISO 639-1 code for the language that you want your checks to appear in.
The Support API currently supports the following languages for Trusted Advisor:
+ Chinese, Simplified - `zh`
+ Chinese, Traditional - `zh_TW`
+ English - `en`
+ French - `fr`
+ German - `de`
+ Indonesian - `id`
+ Italian - `it`
+ Japanese - `ja`
+ Korean - `ko`
+ Portuguese, Brazilian - `pt_BR`
+ Spanish - `es`
Type: String

## Response Syntax
<a name="API_DescribeTrustedAdvisorChecks_ResponseSyntax"></a>

```
{
   "checks": [
      {
         "category": "string",
         "description": "string",
         "id": "string",
         "metadata": [ "string" ],
         "name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeTrustedAdvisorChecks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [checks](#API_DescribeTrustedAdvisorChecks_ResponseSyntax) **   <a name="AWSSupport-DescribeTrustedAdvisorChecks-response-checks"></a>
Information about all available Trusted Advisor checks.
Type: Array of [TrustedAdvisorCheckDescription](API_TrustedAdvisorCheckDescription.md) objects

## Errors
<a name="API_DescribeTrustedAdvisorChecks_Errors"></a>

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
<a name="API_DescribeTrustedAdvisorChecks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/DescribeTrustedAdvisorChecks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/DescribeTrustedAdvisorChecks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/DescribeTrustedAdvisorChecks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/DescribeTrustedAdvisorChecks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/DescribeTrustedAdvisorChecks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/DescribeTrustedAdvisorChecks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/DescribeTrustedAdvisorChecks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/DescribeTrustedAdvisorChecks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/DescribeTrustedAdvisorChecks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/DescribeTrustedAdvisorChecks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
