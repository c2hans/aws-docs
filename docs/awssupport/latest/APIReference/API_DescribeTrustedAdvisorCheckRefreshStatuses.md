---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorCheckRefreshStatuses.html
---

# DescribeTrustedAdvisorCheckRefreshStatuses
<a name="API_DescribeTrustedAdvisorCheckRefreshStatuses"></a>

Returns the refresh status of the AWS Trusted Advisor checks that have the specified check IDs. You can get the check IDs by calling the [DescribeTrustedAdvisorChecks](API_DescribeTrustedAdvisorChecks.md) operation.

Some checks are refreshed automatically, and you can't return their refresh statuses by using the `DescribeTrustedAdvisorCheckRefreshStatuses` operation. If you call this operation for these checks, you might see an `InvalidParameterValue` error.

**Note**
You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the AWS Support API.
If you call the AWS Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

To call the AWS Trusted Advisor operations in the AWS Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don't support the Trusted Advisor operations. For more information, see [About the AWS Support API](https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint) in the * AWS Support User Guide*.

## Request Syntax
<a name="API_DescribeTrustedAdvisorCheckRefreshStatuses_RequestSyntax"></a>

```
{
   "checkIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeTrustedAdvisorCheckRefreshStatuses_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [checkIds](#API_DescribeTrustedAdvisorCheckRefreshStatuses_RequestSyntax) **   <a name="AWSSupport-DescribeTrustedAdvisorCheckRefreshStatuses-request-checkIds"></a>
The IDs of the Trusted Advisor checks to get the status.
If you specify the check ID of a check that is automatically refreshed, you might see an `InvalidParameterValue` error.
Type: Array of strings

## Response Syntax
<a name="API_DescribeTrustedAdvisorCheckRefreshStatuses_ResponseSyntax"></a>

```
{
   "statuses": [
      {
         "checkId": "string",
         "millisUntilNextRefreshable": number,
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeTrustedAdvisorCheckRefreshStatuses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [statuses](#API_DescribeTrustedAdvisorCheckRefreshStatuses_ResponseSyntax) **   <a name="AWSSupport-DescribeTrustedAdvisorCheckRefreshStatuses-response-statuses"></a>
The refresh status of the specified Trusted Advisor checks.
Type: Array of [TrustedAdvisorCheckRefreshStatus](API_TrustedAdvisorCheckRefreshStatus.md) objects

## Errors
<a name="API_DescribeTrustedAdvisorCheckRefreshStatuses_Errors"></a>

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
<a name="API_DescribeTrustedAdvisorCheckRefreshStatuses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/DescribeTrustedAdvisorCheckRefreshStatuses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/DescribeTrustedAdvisorCheckRefreshStatuses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/DescribeTrustedAdvisorCheckRefreshStatuses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/DescribeTrustedAdvisorCheckRefreshStatuses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/DescribeTrustedAdvisorCheckRefreshStatuses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/DescribeTrustedAdvisorCheckRefreshStatuses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/DescribeTrustedAdvisorCheckRefreshStatuses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/DescribeTrustedAdvisorCheckRefreshStatuses)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/DescribeTrustedAdvisorCheckRefreshStatuses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/DescribeTrustedAdvisorCheckRefreshStatuses)
