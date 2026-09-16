---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeUsageReportSubscriptions.html
---

# DescribeUsageReportSubscriptions
<a name="API_DescribeUsageReportSubscriptions"></a>

Retrieves a list that describes one or more usage report subscriptions.

## Request Syntax
<a name="API_DescribeUsageReportSubscriptions_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeUsageReportSubscriptions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeUsageReportSubscriptions_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeUsageReportSubscriptions-request-MaxResults"></a>
The maximum size of each page of results.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeUsageReportSubscriptions_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeUsageReportSubscriptions-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeUsageReportSubscriptions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "UsageReportSubscriptions": [
      {
         "LastGeneratedReportDate": number,
         "S3BucketName": "string",
         "Schedule": "string",
         "SubscriptionErrors": [
            {
               "ErrorCode": "string",
               "ErrorMessage": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_DescribeUsageReportSubscriptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeUsageReportSubscriptions_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeUsageReportSubscriptions-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Minimum length of 1.

 ** [UsageReportSubscriptions](#API_DescribeUsageReportSubscriptions_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeUsageReportSubscriptions-response-UsageReportSubscriptions"></a>
Information about the usage report subscription.
Type: Array of [UsageReportSubscription](API_UsageReportSubscription.md) objects

## Errors
<a name="API_DescribeUsageReportSubscriptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidAccountStatusException **
The resource cannot be created because your AWS account is suspended. For assistance, contact AWS Support.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeUsageReportSubscriptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeUsageReportSubscriptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeUsageReportSubscriptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeUsageReportSubscriptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeUsageReportSubscriptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeUsageReportSubscriptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeUsageReportSubscriptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeUsageReportSubscriptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeUsageReportSubscriptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeUsageReportSubscriptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeUsageReportSubscriptions)
