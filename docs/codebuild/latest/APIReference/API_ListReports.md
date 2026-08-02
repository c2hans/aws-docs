---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListReports.html
---

# ListReports
<a name="API_ListReports"></a>

 Returns a list of ARNs for the reports in the current AWS account.

## Request Syntax
<a name="API_ListReports_RequestSyntax"></a>

```
{
   "filter": {
      "status": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListReports_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [filter](#API_ListReports_RequestSyntax) **   <a name="CodeBuild-ListReports-request-filter"></a>
 A `ReportFilter` object used to filter the returned reports.
Type: [ReportFilter](API_ReportFilter.md) object
Required: No

 ** [maxResults](#API_ListReports_RequestSyntax) **   <a name="CodeBuild-ListReports-request-maxResults"></a>
 The maximum number of paginated reports returned per response. Use `nextToken` to iterate pages in the list of returned `Report` objects. The default value is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListReports_RequestSyntax) **   <a name="CodeBuild-ListReports-request-nextToken"></a>
 During a previous call, the maximum number of items that can be returned is the value specified in `maxResults`. If there more items in the list, then a unique string called a *nextToken* is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.
Type: String
Required: No

 ** [sortOrder](#API_ListReports_RequestSyntax) **   <a name="CodeBuild-ListReports-request-sortOrder"></a>
 Specifies the sort order for the list of returned reports. Valid values are:
+  `ASCENDING`: return reports in chronological order based on their creation date.
+  `DESCENDING`: return reports in the reverse chronological order based on their creation date.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_ListReports_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "reports": [ "string" ]
}
```

## Response Elements
<a name="API_ListReports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListReports_ResponseSyntax) **   <a name="CodeBuild-ListReports-response-nextToken"></a>
 During a previous call, the maximum number of items that can be returned is the value specified in `maxResults`. If there more items in the list, then a unique string called a *nextToken* is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.
Type: String

 ** [reports](#API_ListReports_ResponseSyntax) **   <a name="CodeBuild-ListReports-response-reports"></a>
 The list of returned ARNs for the reports in the current AWS account.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListReports_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListReports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/ListReports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/ListReports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ListReports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/ListReports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ListReports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/ListReports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/ListReports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/ListReports)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/ListReports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ListReports)
