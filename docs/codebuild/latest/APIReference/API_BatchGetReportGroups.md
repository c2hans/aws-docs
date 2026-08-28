---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetReportGroups.html
---

# BatchGetReportGroups
<a name="API_BatchGetReportGroups"></a>

 Returns an array of report groups.

## Request Syntax
<a name="API_BatchGetReportGroups_RequestSyntax"></a>

```
{
   "reportGroupArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetReportGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [reportGroupArns](#API_BatchGetReportGroups_RequestSyntax) **   <a name="CodeBuild-BatchGetReportGroups-request-reportGroupArns"></a>
 An array of report group ARNs that identify the report groups to return.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.
Required: Yes

## Response Syntax
<a name="API_BatchGetReportGroups_ResponseSyntax"></a>

```
{
   "reportGroups": [
      {
         "arn": "string",
         "created": number,
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
         "lastModified": number,
         "name": "string",
         "status": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "type": "string"
      }
   ],
   "reportGroupsNotFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetReportGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [reportGroups](#API_BatchGetReportGroups_ResponseSyntax) **   <a name="CodeBuild-BatchGetReportGroups-response-reportGroups"></a>
 The array of report groups returned by `BatchGetReportGroups`.
Type: Array of [ReportGroup](API_ReportGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [reportGroupsNotFound](#API_BatchGetReportGroups_ResponseSyntax) **   <a name="CodeBuild-BatchGetReportGroups-response-reportGroupsNotFound"></a>
 An array of ARNs passed to `BatchGetReportGroups` that are not associated with a `ReportGroup`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.

## Errors
<a name="API_BatchGetReportGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetReportGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/BatchGetReportGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/BatchGetReportGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/BatchGetReportGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/BatchGetReportGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/BatchGetReportGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/BatchGetReportGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/BatchGetReportGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/BatchGetReportGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/BatchGetReportGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/BatchGetReportGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
