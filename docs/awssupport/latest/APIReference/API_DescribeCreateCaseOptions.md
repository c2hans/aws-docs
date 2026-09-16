---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCreateCaseOptions.html
---

# DescribeCreateCaseOptions
<a name="API_DescribeCreateCaseOptions"></a>

Returns a list of CreateCaseOption types along with the corresponding supported hours and language availability. You can specify the `language` `categoryCode`, `issueType` and `serviceCode` used to retrieve the CreateCaseOptions.

**Note**
You must have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan to use the AWS Support API. If you're in an AWS Region that doesn't offer one of these AWS Support plans, or if you haven't transitioned to one of these plans, you can use the AWS Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.
If you call the AWS Support API from an account that doesn't have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

## Request Syntax
<a name="API_DescribeCreateCaseOptions_RequestSyntax"></a>

```
{
   "categoryCode": "{{string}}",
   "dryRun": {{boolean}},
   "issueType": "{{string}}",
   "language": "{{string}}",
   "serviceCode": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCreateCaseOptions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [categoryCode](#API_DescribeCreateCaseOptions_RequestSyntax) **   <a name="AWSSupport-DescribeCreateCaseOptions-request-categoryCode"></a>
The category of problem for the support case. You also use the [DescribeServices](API_DescribeServices.md) operation to get the category code for a service. Each AWS service defines its own set of category codes.
Type: String

 ** [dryRun](#API_DescribeCreateCaseOptions_RequestSyntax) **   <a name="AWSSupport-DescribeCreateCaseOptions-request-dryRun"></a>
Specifies whether to validate the request without actually returning case option data. When set to `true`, the request is validated but no options are returned, and the operation returns a `DryRunOperationException`. When omitted or set to `false`, the request runs normally.
Type: Boolean

 ** [issueType](#API_DescribeCreateCaseOptions_RequestSyntax) **   <a name="AWSSupport-DescribeCreateCaseOptions-request-issueType"></a>
The type of issue for the case. You can specify `customer-service` or `technical`. If you don't specify a value, the default is `technical`.
Type: String

 ** [language](#API_DescribeCreateCaseOptions_RequestSyntax) **   <a name="AWSSupport-DescribeCreateCaseOptions-request-language"></a>
The language in which AWS Support handles the case. AWS Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the `language` parameter if you want support in that language.
Type: String

 ** [serviceCode](#API_DescribeCreateCaseOptions_RequestSyntax) **   <a name="AWSSupport-DescribeCreateCaseOptions-request-serviceCode"></a>
The code for the AWS service. You can use the [DescribeServices](API_DescribeServices.md) operation to get the possible `serviceCode` values.
Type: String

## Response Syntax
<a name="API_DescribeCreateCaseOptions_ResponseSyntax"></a>

```
{
   "communicationTypes": [
      {
         "datesWithoutSupport": [
            {
               "endDateTime": "string",
               "startDateTime": "string"
            }
         ],
         "supportedHours": [
            {
               "endTime": "string",
               "startTime": "string"
            }
         ],
         "type": "string"
      }
   ],
   "languageAvailability": "string"
}
```

## Response Elements
<a name="API_DescribeCreateCaseOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [communicationTypes](#API_DescribeCreateCaseOptions_ResponseSyntax) **   <a name="AWSSupport-DescribeCreateCaseOptions-response-communicationTypes"></a>
 A JSON-formatted array that contains the available communication type options, along with the available support timeframes for the given inputs.
Type: Array of [CommunicationTypeOptions](API_CommunicationTypeOptions.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [languageAvailability](#API_DescribeCreateCaseOptions_ResponseSyntax) **   <a name="AWSSupport-DescribeCreateCaseOptions-response-languageAvailability"></a>
Language availability can be any of the following:
+  available
+  best\_effort
+  unavailable
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.

## Errors
<a name="API_DescribeCreateCaseOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DryRunOperationException **
The request was valid, but the operation wasn't performed because `dryRun` was set to `true`.
HTTP Status Code: 400

 ** InternalServerError **
An internal server error occurred.
 ** message **
An internal server error occurred.
HTTP Status Code: 500

 ** ThrottlingException **
 You have exceeded the maximum allowed TPS (Transactions Per Second) for the operations.
HTTP Status Code: 400

## See Also
<a name="API_DescribeCreateCaseOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/DescribeCreateCaseOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/DescribeCreateCaseOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/DescribeCreateCaseOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/DescribeCreateCaseOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/DescribeCreateCaseOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/DescribeCreateCaseOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/DescribeCreateCaseOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/DescribeCreateCaseOptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/DescribeCreateCaseOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/DescribeCreateCaseOptions)
