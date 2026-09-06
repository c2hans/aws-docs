---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteReportGroup.html
---

# DeleteReportGroup
<a name="API_DeleteReportGroup"></a>

Deletes a report group. Before you delete a report group, you must delete its reports.

## Request Syntax
<a name="API_DeleteReportGroup_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "deleteReports": {{boolean}}
}
```

## Request Parameters
<a name="API_DeleteReportGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [arn](#API_DeleteReportGroup_RequestSyntax) **   <a name="CodeBuild-DeleteReportGroup-request-arn"></a>
The ARN of the report group to delete.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [deleteReports](#API_DeleteReportGroup_RequestSyntax) **   <a name="CodeBuild-DeleteReportGroup-request-deleteReports"></a>
If `true`, deletes any reports that belong to a report group before deleting the report group.
If `false`, you must delete any reports in the report group. Use [ListReportsForReportGroup](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListReportsForReportGroup.html) to get the reports in a report group. Use [DeleteReport](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteReport.html) to delete the reports. If you call `DeleteReportGroup` for a report group that contains one or more reports, an exception is thrown.
Type: Boolean
Required: No

## Response Elements
<a name="API_DeleteReportGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteReportGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteReportGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/DeleteReportGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/DeleteReportGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/DeleteReportGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/DeleteReportGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/DeleteReportGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/DeleteReportGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/DeleteReportGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/DeleteReportGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/DeleteReportGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/DeleteReportGroup)
