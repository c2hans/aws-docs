---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListApplications.html
---

# ListApplications
<a name="API_ListApplications"></a>

Returns a list of Managed Service for Apache Flink applications in your account. For each application, the response includes the application name, Amazon Resource Name (ARN), and status.

If you want detailed information about a specific application, use [DescribeApplication](API_DescribeApplication.md).

## Request Syntax
<a name="API_ListApplications_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListApplications_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Limit](#API_ListApplications_RequestSyntax) **   <a name="APIReference-ListApplications-request-Limit"></a>
The maximum number of applications to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListApplications_RequestSyntax) **   <a name="APIReference-ListApplications-request-NextToken"></a>
If a previous command returned a pagination token, pass it into this value to retrieve the next set of results. For more information about pagination, see [Using the Amazon Command Line Interface's Pagination Options](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_ListApplications_ResponseSyntax"></a>

```
{
   "ApplicationSummaries": [
      {
         "ApplicationARN": "string",
         "ApplicationMode": "string",
         "ApplicationName": "string",
         "ApplicationStatus": "string",
         "ApplicationVersionId": number,
         "RuntimeEnvironment": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListApplications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationSummaries](#API_ListApplications_ResponseSyntax) **   <a name="APIReference-ListApplications-response-ApplicationSummaries"></a>
A list of `ApplicationSummary` objects.
Type: Array of [ApplicationSummary](API_ApplicationSummary.md) objects

 ** [NextToken](#API_ListApplications_ResponseSyntax) **   <a name="APIReference-ListApplications-response-NextToken"></a>
The pagination token for the next set of results, or `null` if there are no additional results. Pass this token into a subsequent command to retrieve the next set of items For more information about pagination, see [Using the Amazon Command Line Interface's Pagination Options](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_ListApplications_Errors"></a>

 ** InvalidRequestException **
The request JSON is not valid for the operation.
HTTP Status Code: 400

## See Also
<a name="API_ListApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/ListApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/ListApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ListApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/ListApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ListApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/ListApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/ListApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/ListApplications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/ListApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ListApplications)
