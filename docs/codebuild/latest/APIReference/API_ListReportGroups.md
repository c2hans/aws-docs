---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListReportGroups.html
---

# ListReportGroups
<a name="API_ListReportGroups"></a>

 Gets a list ARNs for the report groups in the current AWS account.

## Request Syntax
<a name="API_ListReportGroups_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sortBy": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListReportGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [maxResults](#API_ListReportGroups_RequestSyntax) **   <a name="CodeBuild-ListReportGroups-request-maxResults"></a>
 The maximum number of paginated report groups returned per response. Use `nextToken` to iterate pages in the list of returned `ReportGroup` objects. The default value is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListReportGroups_RequestSyntax) **   <a name="CodeBuild-ListReportGroups-request-nextToken"></a>
 During a previous call, the maximum number of items that can be returned is the value specified in `maxResults`. If there more items in the list, then a unique string called a *nextToken* is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.
Type: String
Required: No

 ** [sortBy](#API_ListReportGroups_RequestSyntax) **   <a name="CodeBuild-ListReportGroups-request-sortBy"></a>
 The criterion to be used to list build report groups. Valid values include:
+  `CREATED_TIME`: List based on when each report group was created.
+  `LAST_MODIFIED_TIME`: List based on when each report group was last changed.
+  `NAME`: List based on each report group's name.
Type: String
Valid Values: `NAME | CREATED_TIME | LAST_MODIFIED_TIME`
Required: No

 ** [sortOrder](#API_ListReportGroups_RequestSyntax) **   <a name="CodeBuild-ListReportGroups-request-sortOrder"></a>
 Used to specify the order to sort the list of returned report groups. Valid values are `ASCENDING` and `DESCENDING`.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_ListReportGroups_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "reportGroups": [ "string" ]
}
```

## Response Elements
<a name="API_ListReportGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListReportGroups_ResponseSyntax) **   <a name="CodeBuild-ListReportGroups-response-nextToken"></a>
 During a previous call, the maximum number of items that can be returned is the value specified in `maxResults`. If there more items in the list, then a unique string called a *nextToken* is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.
Type: String

 ** [reportGroups](#API_ListReportGroups_ResponseSyntax) **   <a name="CodeBuild-ListReportGroups-response-reportGroups"></a>
 The list of ARNs for the report groups in the current AWS account.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListReportGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListReportGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/ListReportGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/ListReportGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ListReportGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/ListReportGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ListReportGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/ListReportGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/ListReportGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/ListReportGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/ListReportGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ListReportGroups)
