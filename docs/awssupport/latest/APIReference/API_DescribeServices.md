---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeServices.html
---

# DescribeServices
<a name="API_DescribeServices"></a>

Returns the current list of AWS services and a list of service categories for each service. You then use service names and categories in your [CreateCase](API_CreateCase.md) requests. Each AWS service has its own set of categories.

The service codes and category codes correspond to the values that appear in the **Service** and **Category** lists on the Support Center [Create Case](https://console.aws.amazon.com/support/home#/case/create) page. The values in those fields don't necessarily match the service codes and categories returned by the `DescribeServices` operation. Always use the service codes and categories that the `DescribeServices` operation returns, so that you have the most recent set of service and category codes.

**Note**
You must have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan to use the AWS Support API. If you're in an AWS Region that doesn't offer one of these AWS Support plans, or if you haven't transitioned to one of these plans, you can use the AWS Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.
If you call the AWS Support API from an account that doesn't have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

## Request Syntax
<a name="API_DescribeServices_RequestSyntax"></a>

```
{
   "dryRun": {{boolean}},
   "language": "{{string}}",
   "serviceCodeList": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeServices_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [dryRun](#API_DescribeServices_RequestSyntax) **   <a name="AWSSupport-DescribeServices-request-dryRun"></a>
Specifies whether to validate the request without actually returning the list of services. When set to `true`, the request is validated but no services are returned, and the operation returns a `DryRunOperationException`. When omitted or set to `false`, the request runs normally.
Type: Boolean

 ** [language](#API_DescribeServices_RequestSyntax) **   <a name="AWSSupport-DescribeServices-request-language"></a>
The language in which AWS Support handles the case. AWS Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the `language` parameter if you want support in that language.
Type: String

 ** [serviceCodeList](#API_DescribeServices_RequestSyntax) **   <a name="AWSSupport-DescribeServices-request-serviceCodeList"></a>
A JSON-formatted list of service codes available for AWS services.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Response Syntax
<a name="API_DescribeServices_ResponseSyntax"></a>

```
{
   "services": [
      {
         "categories": [
            {
               "code": "string",
               "name": "string"
            }
         ],
         "code": "string",
         "name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeServices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [services](#API_DescribeServices_ResponseSyntax) **   <a name="AWSSupport-DescribeServices-response-services"></a>
A JSON-formatted list of AWS services.
Type: Array of [Service](API_Service.md) objects

## Errors
<a name="API_DescribeServices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DryRunOperationException **
The request was valid, but the operation wasn't performed because `dryRun` was set to `true`.
HTTP Status Code: 400

 ** InternalServerError **
An internal server error occurred.
 ** message **
An internal server error occurred.
HTTP Status Code: 500

## See Also
<a name="API_DescribeServices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/DescribeServices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/DescribeServices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/DescribeServices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/DescribeServices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/DescribeServices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/DescribeServices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/DescribeServices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/DescribeServices)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/DescribeServices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/DescribeServices)
