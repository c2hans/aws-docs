---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetReports.html
---

# BatchGetReports
<a name="API_BatchGetReports"></a>

 Returns an array of reports.

## Request Syntax
<a name="API_BatchGetReports_RequestSyntax"></a>

```
{
   "reportArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetReports_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [reportArns](#API_BatchGetReports_RequestSyntax) **   <a name="CodeBuild-BatchGetReports-request-reportArns"></a>
 An array of ARNs that identify the `Report` objects to return.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.
Required: Yes

## Response Syntax
<a name="API_BatchGetReports_ResponseSyntax"></a>

```
{
   "reports": [
      {
         "arn": "string",
         "codeCoverageSummary": {
            "branchCoveragePercentage": number,
            "branchesCovered": number,
            "branchesMissed": number,
            "lineCoveragePercentage": number,
            "linesCovered": number,
            "linesMissed": number
         },
         "created": number,
         "executionId": "string",
         "expired": number,
         "exportConfig": {
            "exportConfigType": "string",
            "s3Destination": {
               "bucket": "string",
               "bucketOwner": "string",
               "encryptionDisabled": boolean,
               "encryptionKey": "string",
               "packaging": "string",
               "path": "string"
            }
         },
         "name": "string",
         "reportGroupArn": "string",
         "status": "string",
         "testSummary": {
            "durationInNanoSeconds": number,
            "statusCounts": {
               "string" : number
            },
            "total": number
         },
         "truncated": boolean,
         "type": "string"
      }
   ],
   "reportsNotFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetReports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [reports](#API_BatchGetReports_ResponseSyntax) **   <a name="CodeBuild-BatchGetReports-response-reports"></a>
 The array of `Report` objects returned by `BatchGetReports`.
Type: Array of [Report](API_Report.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [reportsNotFound](#API_BatchGetReports_ResponseSyntax) **   <a name="CodeBuild-BatchGetReports-response-reportsNotFound"></a>
 An array of ARNs passed to `BatchGetReportGroups` that are not associated with a `Report`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.

## Errors
<a name="API_BatchGetReports_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetReports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/BatchGetReports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/BatchGetReports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/BatchGetReports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/BatchGetReports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/BatchGetReports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/BatchGetReports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/BatchGetReports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/BatchGetReports)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/BatchGetReports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/BatchGetReports)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
