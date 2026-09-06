---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListApplicationVersions.html
---

# ListApplicationVersions
<a name="API_ListApplicationVersions"></a>

Lists all the versions for the specified application, including versions that were rolled back. The response also includes a summary of the configuration associated with each version.

To get the complete description of a specific application version, invoke the [DescribeApplicationVersion](API_DescribeApplicationVersion.md) operation.

**Note**
This operation is supported only for Managed Service for Apache Flink.

## Request Syntax
<a name="API_ListApplicationVersions_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListApplicationVersions_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_ListApplicationVersions_RequestSyntax) **   <a name="APIReference-ListApplicationVersions-request-ApplicationName"></a>
The name of the application for which you want to list all versions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [Limit](#API_ListApplicationVersions_RequestSyntax) **   <a name="APIReference-ListApplicationVersions-request-Limit"></a>
The maximum number of versions to list in this invocation of the operation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListApplicationVersions_RequestSyntax) **   <a name="APIReference-ListApplicationVersions-request-NextToken"></a>
If a previous invocation of this operation returned a pagination token, pass it into this value to retrieve the next set of results. For more information about pagination, see [Using the Amazon Command Line Interface's Pagination Options](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## Response Syntax
<a name="API_ListApplicationVersions_ResponseSyntax"></a>

```
{
   "ApplicationVersionSummaries": [
      {
         "ApplicationStatus": "string",
         "ApplicationVersionId": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListApplicationVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationVersionSummaries](#API_ListApplicationVersions_ResponseSyntax) **   <a name="APIReference-ListApplicationVersions-response-ApplicationVersionSummaries"></a>
A list of the application versions and the associated configuration summaries. The list includes application versions that were rolled back.
To get the complete description of a specific application version, invoke the [DescribeApplicationVersion](API_DescribeApplicationVersion.md) operation.
Type: Array of [ApplicationVersionSummary](API_ApplicationVersionSummary.md) objects

 ** [NextToken](#API_ListApplicationVersions_ResponseSyntax) **   <a name="APIReference-ListApplicationVersions-response-NextToken"></a>
The pagination token for the next set of results, or `null` if there are no additional results. To retrieve the next set of items, pass this token into a subsequent invocation of this operation. For more information about pagination, see [Using the Amazon Command Line Interface's Pagination Options](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

## Errors
<a name="API_ListApplicationVersions_Errors"></a>

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Specified application can't be found.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_ListApplicationVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/ListApplicationVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/ListApplicationVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ListApplicationVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/ListApplicationVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ListApplicationVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/ListApplicationVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/ListApplicationVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/ListApplicationVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/ListApplicationVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ListApplicationVersions)
