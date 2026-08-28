---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeSeverityLevels.html
---

# DescribeSeverityLevels
<a name="API_DescribeSeverityLevels"></a>

Returns the list of severity levels that you can assign to a support case. The severity level for a case is also a field in the [CaseDetails](API_CaseDetails.md) data type that you include for a [CreateCase](API_CreateCase.md) request.

**Note**
You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the AWS Support API.
If you call the AWS Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

## Request Syntax
<a name="API_DescribeSeverityLevels_RequestSyntax"></a>

```
{
   "language": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSeverityLevels_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [language](#API_DescribeSeverityLevels_RequestSyntax) **   <a name="AWSSupport-DescribeSeverityLevels-request-language"></a>
The language in which AWS Support handles the case. AWS Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the `language` parameter if you want support in that language.
Type: String

## Response Syntax
<a name="API_DescribeSeverityLevels_ResponseSyntax"></a>

```
{
   "severityLevels": [
      {
         "code": "string",
         "name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSeverityLevels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [severityLevels](#API_DescribeSeverityLevels_ResponseSyntax) **   <a name="AWSSupport-DescribeSeverityLevels-response-severityLevels"></a>
The available severity levels for the support case. Available severity levels are defined by your service level agreement with AWS.
Type: Array of [SeverityLevel](API_SeverityLevel.md) objects

## Errors
<a name="API_DescribeSeverityLevels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An internal server error occurred.
 ** message **
An internal server error occurred.
HTTP Status Code: 500

## See Also
<a name="API_DescribeSeverityLevels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/DescribeSeverityLevels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/DescribeSeverityLevels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/DescribeSeverityLevels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/DescribeSeverityLevels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/DescribeSeverityLevels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/DescribeSeverityLevels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/DescribeSeverityLevels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/DescribeSeverityLevels)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/DescribeSeverityLevels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/DescribeSeverityLevels)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
